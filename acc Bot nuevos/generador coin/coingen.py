cid ="85624539"

#from keep_alive import keep_alive
import os
os.system("pip install Dick.py==1.2")
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet
from colorama import init, Fore, Back, Style
print("\n\n\33[48;5;5m\33[38;5;234m ❮ COIN GENERATOR 6.5 ❯ \33[0m\33[48;5;235m\33[38;5;5m \33[0m")
init()
print(Fore.GREEN + Style.BRIGHT)
print(pyfiglet.figlet_format("TECH", font="cybermedium"))
print(pyfiglet.figlet_format("VISION", font="cybermedium"))
import amino
from uuid import uuid4
import requests
import threading
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from os import path
import json
THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"accounts.json")
dictlist=[]

with open(emailfile) as f:
    dictlist = json.load(f)

headers={
        "cookies":"__cfduid=d0c98f07df2594b5f4aad802942cae1f01619569096",
        "authorization":"Basic NWJiNTM0OWUxYzlkNDQwMDA2NzUwNjgwOmM0ZDJmYmIxLTVlYjItNDM5MC05MDk3LTkxZjlmMjQ5NDI4OA=="
    }
 
def tapcoins(usrd:str):
    data = {
        "reward":{"ad_unit_id":"t00_tapjoy_android_master_checkinwallet_rewardedvideo_322","credentials_type":"publisher","custom_json":{"hashed_user_id":f"{usrd}"},"demand_type":"sdk_bidding","event_id":None,"network":"facebook","placement_tag":"default","reward_name":"Amino Coin","reward_valid":"true","reward_value":2,"shared_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f","version_id":"1569147951493","waterfall_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f"},
        "app":{"bundle_id":"com.narvii.amino.master","current_orientation":"portrait","release_version":"3.4.33567","user_agent":"Dalvik\/2.1.0 (Linux; U; Android 10; G8231 Build\/41.2.A.0.219; com.narvii.amino.master\/3.4.33567)"},"date_created":1620295485,"session_id":"49374c2c-1aa3-4094-b603-1cf2720dca67","device_user":{"country":"US","device":{"architecture":"aarch64","carrier":{"country_code":602,"name":"Vodafone","network_code":0},"is_phone":"true","model":"GT-S5360","model_type":"Samsung","operating_system":"android","operating_system_version":"29","screen_size":{"height":2260,"resolution":2.55,"width":1080}},"do_not_track":"false","idfa":"7495ec00-0490-4d53-8b9a-b5cc31ba885b","ip_address":"","locale":"en","timezone":{"location":"Asia\/Seoul","offset":"GMT+09:00"},"volume_enabled":"true"}
        }
    event=uuid4()
    data["reward"]["event_id"]=f"{event}"
    try:
        requests.post("https://ads.tapdaq.com/v4/analytics/reward",json=data, headers=headers)
    except:
    	pass

def magicnum():
    toime={"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300}
    return toime

def sendobj(sub : amino.SubClient):
    timer=[
    magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum()
    ]
    sub.send_active_obj(timers=timer)

def log(cli : amino.Client,email : str, password : str):
    try:
        cli.login(email=email,password=password)
        print(f"logged into {email}\n")
    except Exception as e:
        print(e)
        pass

def task(sub : amino.SubClient,email : str,i : int):
    try:
        sendobj(sub)
        print(f"Generated Coins for {email} times :- {i+1}")
    except:
        return None

def threadit(acc : dict):
    email=acc["email"]
    device=acc["device"]
    password=acc["password"]
    client=amino.Client(deviceId=device)
    log(cli=client,email=email,password=password)
    client.join_community(cid)
    subclient=amino.SubClient(comId=cid,profile=client.profile)
    usrd=client.userId
    with ThreadPoolExecutor(max_workers=1) as executorx:
        _ = [executorx.submit(task, subclient,email,i)for i in range(25)]
    for _ in range(150):
    	try:
    		threading.Thread(target=tapcoins,args=(usrd,)).start()
    	#	print("Generating")
    	except:
    		pass
    client.logout()
    print(f"Generated Coins with {email}")

def main():
    print(f"\n\33[93;5;5m\33[93;5;234m ❮ Total Accounts : {len(dictlist)} ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
    for amp in dictlist:
    	threadit(amp)
    print(f'Claimed coins from {len(dictlist)} accounts')
 
if __name__ == '__main__':
	main()


