password="aaaa5555"
from hmac import new
from os import urandom
from hashlib import sha1
from pyfiglet import figlet_format
from progress.bar import IncrementalBar
from base64 import b64decode
from io import BytesIO
import names
from hashlib import sha1
import names
import random
import hmac
import platform,socket,re,uuid 
import base64
import hmac
import time
import json
from hashlib import sha1
import secmail
import random
import platform,socket,re,uuid
import json
import requests
from time import sleep
from bs4 import BeautifulSoup
from time import time as timestamp
import json
from os import path
import amino
from colored import fg, bg, attr
from pyfiglet import Figlet



client=amino.Client()

def sig(data):
        #at=json.dumps(data)
        key='fbf98eb3a07a9042ee5593b10ce9f3286a69d4e2'
        mac = hmac.new(bytes.fromhex(key), data.encode("utf-8"), sha1)
        digest = bytes.fromhex("32") + mac.digest()
        return base64.b64encode(digest).decode("utf-8")


def device():
    b = requests.get("http://forevercynical.com/generate/deviceid")
    return b.text


 
def gen_email():
    mail = secmail.SecMail()
    email = mail.generate_email()
    return email
    


def get_message(email):
                try:
                    sleep(4)
                    f=email
                    mail = secmail.SecMail()
                    inbox = mail.get_messages(f)
                    for Id in inbox.id:
                        msg = mail.read_message(email=f, id=Id).htmlBody
                        bs = BeautifulSoup(msg, 'html.parser')
                        images = bs.find_all('a')[0]
                        url = (images['href']+'\n')
                        if url is not None:
                         print(url)
                         return url
                         #wget.download(url=url,out="code.png")
                except:
                    pass
                    
                    

def register(nickname: str, email: str, password: str,deviceId: str,verificationCode: str):
        """
        Register an account.

        **Parameters**
            - **nickname** : Nickname of the account.
            - **email** : Email of the account.
            - **password** : Password of the account.
            - **verificationCode** : Verification code.
            - **deviceId** : The device id being registered to.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <amino.lib.util.exceptions>`
        """

        data = {
            "secret": f"0 {password}",
            "deviceID": deviceId,
            "email": email,
            "clientType": 100,
            "nickname": nickname,
            "latitude": 0,
            "longitude": 0,
            "address": None,
            "clientCallbackURL": "narviiapp://relogin",
            "validationContext": {
                "data": {
                    "code": verificationCode
                },
                "type": 1,
                "identity": email
            },
            "type": 1,
            "identity": email,
            "timestamp": int(timestamp() * 1000)
        }
        heads={
    'Accept-Language': 'en-US', 
    'Content-Type': 'application/json; charset=utf-8', 
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)', 
    'Host': 'service.narvii.com', 
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
    }
        data=json.dumps(data)
        heads["NDC-MSG-SIG"]=sig(data)
        heads["Content-Length"] = str(len(data))
        heads["NDCDEVICEID"]=deviceId
        response = requests.post(f"https://service.narvii.com/api/v1/g/s/auth/register", data=data, headers=heads)
        if response.status_code != 200:
          print("Cannot create accounts, Use VPN")

        
def request_verify_code(email: str,deviceId: str):
        data = {
            "identity": email,
            "type": 1,
            "deviceID": deviceId
        }
        heads={
    'Accept-Language': 'en-US', 
    'Content-Type': 'application/json; charset=utf-8', 
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)', 
    'Host': 'service.narvii.com', 
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
        }
        data = json.dumps(data)
        heads["Content-Length"] = str(len(data))
        heads["NDCDEVICEID"]=deviceId
        heads["NDC-MSG-SIG"]=sig(data)
        response = requests.post(f"https://service.narvii.com/api/v1/g/s/auth/request-security-validation", data=data, headers=heads)
        
        

def fancy_name():
    nm=''
    for i in names.get_first_name():
        nm=nm+i
    return nm


def generation_process(count: int):
    progress_bar = IncrementalBar("Generated", max=count)
    for i in range(count):
      deviceid=device()
      values=gen_email()
      email=values
      nick = "CommunityBot"
      req=request_verify_code(email=email, deviceId=deviceid)
      get_message(values)
      vcode=input("Enter Code Here:  ")
      register(nickname=nick, email=email, password=password,deviceId=deviceid,verificationCode=vcode)
      progress_bar.next()
      progress_bar.finish()
      print(f"-- Generated {count} Accounts...")
      with open('accounts.json', 'a') as x:
        acc = f'\n{{\n"email": "{email}", \n"password":"{password}",\n"device": "{deviceid}"\n}},'
        x.write('['+acc+']')
        
      
generation_process(count=int(input("How much accounts to generate: ")))
