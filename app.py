import random
import urllib3
from flask import Flask, jsonify, request
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import httpx
import asyncio
from byte import *
app = Flask(__name__)

async def like(token, id):
    url = 'https://202.81.99.18/LikeProfile'
    headers = {
        'X-Unity-Version': '2018.4.11f1',
        'ReleaseVersion': 'OB46',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-GA': 'v1 1',
        'Authorization': f'Bearer {token}',
        'Content-Length': '16',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)',
        'Host': 'clientbp.ggblueshark.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    data = bytes.fromhex(encrypt_api(f'08{Encrypt_ID(id)}12024d45'))
    async with httpx.AsyncClient(verify=False) as client:
        try:
            response = await client.post(url, headers=headers, data=data)
            print(response.status_code)
            print(response.text)
            return response.status_code
        except httpx.RequestError as e:
            print(f"An error occurred: {e}")
            return None
async def TOKEN_MAKER(OLD_ACCESS_TOKEN, NEW_ACCESS_TOKEN, OLD_OPEN_ID, NEW_OPEN_ID, uid, likes_uid):
    PYLOAD = b'C\xb9\xed\x02\xee;\xe0W6\xe1\xd6&\x9d4Q3\xb3\xb4\x92\xa6\xae\xcf\x16\xfe\xf4\x9e\xe3R\x99h%\xee~I_\x85\x99\xc8f\xf8\xb7/\xa7/k\xe2k\xb3\x92\xfd\xf6\xe3\x96\x1e[\xaae\x11d\x12\xda\xd8\xfb+\x82X\xf0gW\xae>\x0c\xdd\xda@\xa4\xa0]bW\xeb\xd2s>\xb1\x110\xe4os\x91\x98 \xe2\x9c\xed\xd5\xfavI\x8a\xadR\x1b\xe0g0f\xd3\x98Xc\x1fU\xd1!\x12!\'\x14\x85\xaf\x8c\x1d\x9a\x99\xdcS\x84\xbe\x82\xfd:.m\xc9\re6r\xb0\x81\xa8\xf3\xef\xb6?,\x1a\xbe1\xce\xf6\xebu{H\xe3\xdcQ \xac\xcd\x08\x01\x84qJk\x8f\x9dn\xe97\xd8&\x97\xdc_t3y\xd2\xccy\xd1z\x83\xae\xf8o\x84\xb2\xf4(ZH\xfa\'\xd6/\xad\x0b\x90\x99\xe5\xab\x00\xec\xd7rE\x90\x8b\x1f\xddA\xe3J2\xe0\xe9\xd8\x10I\x80\xdaJ^\xbc\x8b\xf1Q)c\x99\xc5>,b\x89w\xf6D\xbc\xdcg\xed\xeekI-\x1etX\xf8B<_\x1a\x1fo\x02\x81}\xe6\xe7\x95\xab^\t\xda\xc4\x18\x93\x16\x93T\x89-\x8f\xb9\x8al\x01\xa9\t\xd1\xb0s\x1d^\x021c \x91\xccc\x91\xec\xf5\xf3g\xdb\x11\x15JgYm7\xa1\x17\xc6U\xd4\xde\xb6v\x83\xf6\xb5Kg!q\xdf9l\xe4`H\xcf\xbc\xba\x93j6%hl\x9d\x0e\xbf\xb0\xd7\x0ff\xf0\xcf\x06P5\x8f\xe1\xb2\xfc\xadJ\xf5IY\x93\xd8\xd3\xee\x01\xb5\xa1\xbd\x03-n\xa2%I\x07\x15I\xe1\x19\xec\x14VF\x86\x99\xad\xd3\xcc\xe3\x07\xcb)\xa3\xaf\xf0J\x13W\x03\rI\xed\xfd!\x1b\x18\x87\xe1\xab\xb1\xde\xacj\x87\\\xa3v\xb9]\xa6\xd8\n:3[u\xd0\xf4y\xd9\xfa\n`\x9c\x19f#\xf8\xc4\xba\x12\xb4\xe5\x03;\x1c\xc3\xd6Q\xd3\xc7%\t\x7f\x93/\x82h\xbaO\xfd\xb9\xb1\x93W\xf8\\-\xa1L\x11\x9a\xd7\xcf\xb8%\x03+\x8a\xf1v\x80\xd6\x86 \x0b\x1at\xf6\xdf8\xf0W\xb3\x0cG\x8f\xb6\xcd\xf5\xb5\\/(-\xaeI\xa494c!\xce&g`\xf1F\x18V\x87-\xc4\x8efP\xaa\x91\xef\xe2\xf3"\xb6A\x00\xe7j\xa5~Dii\x8f\xe4\x93\xf0YM\xab\x07\x05d\xba\x01\xa6z\xff\xc9r\xd2\xf2<R,W \xf0\x97\xe6\xb9t\xf5l\xf7\x87\xc8\xb8\x16\xccy\xf7\xe9\x1b\x1d:\xad\xb2%\xec\xc2\xe8N\x12\xe5\xda\x08\xa9\xd2\x07j|\xc9\xad\xef\xed\r\xcfC2\xb6Ew\x94\xcb]\xa7\x94qVr\x8c=\xa0\x8d\xf8\x1a\xa6M\xd61y\xce%L\x95CK7\x03\xaeo\xa7u4\x82\xb7R\x83\xd0(<\x0e\x0f\xf7\xeb\xdb\x8e\xb8o)u\x9a\xd7\\/\x07*\xc9`\xd0\x9dtl\xf7\xefY\xf8\xb7\xbe\xa7q\xf5\xf6b\x11K\xf1\x96\xd4\xb6\xa3\xa1\xca\x9c\xef\xbb\xa4uq\xb5\xaf\xf4}\x07:T\xbd\xb3\xac\xd9yB\xb8\x80\x02\xa7\xcb:\xe3\x11\x07[\x127\xe1\xe2\x1e\xab!\x1f\xee\xec\x8b\x86\xc7\x82\x9ejj\xb0\x8dl\n\x1cTc \'v\xdf\n\x17\x9a\x95^\xaa#Z\xad\x12\xb4\xd3\xed\xa6q\x08\xab\x0e\xf3\x12\x06\xa2p\xf0\x1do\x01\x8c\xad\x87\x02\xb0I\x8d\xd6L(\xb3\x12~\xbc\xb2u$^\xb1\xbf\x98m\xd9\xd2\x02\xb2\xb3\xab\x1a\xc2 \x81X)a\x19\x84\xcc\xb3\x97FM\x0cSO\xce/\xbf+\xc1"V\xc1\xc1z\xd8\xb6\x08\x95\xd3\x85\xd5,\xba\x10\xc2\xb9}m\xc2,\xe1#MW\xe9\x93lc\x90\x02\xf3\x181\xde\x83\xcb\xc0]\xf8\xa8\xe8\xc4\xaf\xe4\xebI\xd3\xea\xad\x99\x10\xc3eX\x8da\xab\xd9\x0f\xe4\x98\xa2\xa7h<u\xcd\xbf\x1c\x15"\xd2Q\xfdU\x89\x8b\xefd\x87\xec'
    
    a = convert_to_hex(PYLOAD)
    data = bytes.fromhex(decrypt_api(a))
    data = data.replace(OLD_OPEN_ID.encode(), NEW_OPEN_ID.encode())
    data = data.replace(OLD_ACCESS_TOKEN.encode(), NEW_ACCESS_TOKEN.encode())
    
    d = encrypt_api(data.hex())
    Final_Payload = convert_to_bytes(d)

    URL = "https://loginbp.common.ggbluefox.com/MajorLogin"
    headers = {
        "Expect": "100-continue",
        "Authorization": "Bearer",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB46",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": str(len(Final_Payload)),
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-N975F Build/PI)",
        "Host": "loginbp.common.ggbluefox.com",
        "Connection": "close",
        "Accept-Encoding": "gzip, deflate, br"
    }

    async with httpx.AsyncClient(verify=False) as client:
        try:
            RESPONSE = await client.post(URL, headers=headers, data=Final_Payload)
            if RESPONSE.status_code == 200:
                if len(RESPONSE.text) < 10:
                    return False
                BASE64_TOKEN = RESPONSE.text[RESPONSE.text.find("eyJhbGciOiJIUzI1NiIsInN2ciI6IjEiLCJ0eXAiOiJKV1QifQ"):-1]
                second_dot_index = BASE64_TOKEN.find(".", BASE64_TOKEN.find(".") + 1)
                BASE64_TOKEN = BASE64_TOKEN[:second_dot_index+44]
                st = await like(BASE64_TOKEN, likes_uid)  # استخدام like بشكل غير متزامن
                if st != 200:
                    return False  
            else:
                return False
        except httpx.RequestError as e:
            print(f"An error occurred: {e}")
            return False
import httpx

async def guest_token(uid, password, likes_uid):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": "GarenaMSDK/4.0.19P4(G011A ;Android 9;en;US;)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close",
    }
    data = {
        "uid": f"{uid}",
        "password": f"{password}",
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, data=data)
            response.raise_for_status() 
            data = response.json()
            
            NEW_ACCESS_TOKEN = data['access_token']
            NEW_OPEN_ID = data['open_id']
            
            OLD_ACCESS_TOKEN = "37c00ba521e42f7fb8e374a2b5d07c2417e054abca6d7e0f25a83a8243f1d00a"
            OLD_OPEN_ID = "c5a8e6bfd6ff9246a9cc4e043f7f5753"
            
            result = await TOKEN_MAKER(OLD_ACCESS_TOKEN, NEW_ACCESS_TOKEN, OLD_OPEN_ID, NEW_OPEN_ID, uid, likes_uid)
            if not result:
                return False

        except httpx.RequestError as e:
            print(f"An error occurred: {e}")
            return False
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
    await asyncio.sleep(1)

  
async def start_likes(likes_uid):
    try:
        accounts = random_accounts(n=101)  
        tasks = []
        semaphore = asyncio.Semaphore(100000)  
        async def limited_task(account):
            async with semaphore:
                parts = account.split(":")
                if len(parts) >= 2:
                    uid, password = parts[0], parts[1]
                    return await guest_token(uid, password, likes_uid)
                else:
                    return None

        for account in accounts:
            task = asyncio.create_task(limited_task(account))
            tasks.append(task)

        results = await asyncio.gather(*tasks)


        results = [result for result in results if result]
        
        return jsonify({'msg': 'Done Sent Likes.', 'results': results})
    
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/getlikes/<int:id>')
async def checkband(id):
    likes_uid = id
    try:
        result = await start_likes(likes_uid)
        return result
    except Exception as e:return e

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
