import os
import aminofix
import pyfiglet
from os import path
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
init()
print(colorama.Fore.CYAN)
print(colorama.Style.BRIGHT)
f = pyfiglet.Figlet(font='slant')
print (f.renderText('private'))
f = pyfiglet.Figlet(font='slant')
print (f.renderText('chatId'))
print("\t\033[1;31m mad by Uzair_hacked\n\n")
print("\t\033[1;31m Insta id :- jiminieee_________\n\n")
print("\t\033[1;32m get private chatId\033[1;36m  \n\n")
client = aminofix.Client()
email = "bsqo@1secmail.com"
password = "1346"
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Select the community: "))-1]
sub_client = aminofix.SubClient(comId=communityid, profile=client.profile)
chats = sub_client.get_chat_threads(size=150)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chatx = chats.chatId[int(input("Select the chat: "))-1]
print(f"""
⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　
Community comId >> {communityid}

_________________________________

ChatId >> {chatx}
⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　
"""
)

print('''''
Any problems so contact :- http://aminoapps.com/c/vcs8979

telgrm :- https://t.me/Techvision_Ravi_victor_Scripts
''')