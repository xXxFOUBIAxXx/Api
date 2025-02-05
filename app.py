from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from apscheduler.schedulers.background import BackgroundScheduler
import bcrypt
import os

app = Flask(__name__)

# تهيئة قاعدة البيانات
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///game.db')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET', 'super-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 10800  # 3 ساعات بالثواني
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Rate Limiter
limiter = Limiter(
    app=app,
    key_func=lambda: get_jwt_identity() or get_remote_address(),
    default_limits=["100 per hour"]
)

# نموذج المستخدم
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(120))
    token_version = db.Column(db.Integer, default=0)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

# مهمة تجديد التوكنات كل 3 ساعات
def reset_token_versions():
    with app.app_context():
        users = User.query.all()
        for user in users:
            user.token_version += 1
        db.session.commit()

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(func=reset_token_versions, trigger='interval', hours=3)
scheduler.start()

# المسارات
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(message="تم التسجيل بنجاح"), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        token = create_access_token(identity={'id': user.id, 'version': user.token_version})
        return jsonify(access_token=token)
    return jsonify(error="بيانات خاطئة"), 401

@app.route('/profile', methods=['GET'])
@jwt_required()
@limiter.limit("100/hour")
def profile():
    current_user = get_jwt_identity()
    user = User.query.get(current_user['id'])
    return jsonify(username=user.username)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
