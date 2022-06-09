import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

print('Hello, World!')


#--------------------------------------------------------------

import requests
import json

from time import sleep
import keyboard




import collections
import urllib, json

url = "http://127.0.0.1:8000/api/address"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

last =data[-1]

auth = last.get("auth")
#print(auth)    










keyboard.write(auth)
keyboard.press_and_release('enter')


#---------------------------------------------------------------

api_id      = '10038338'
api_hash    = '8db82f3b3b02df25b3dc1d47eb4e6651'
token       = 'bot token'
message     = "Are you getting my message? Again"
phone       = '+923352070087'


# creating a telegram session and assigning
# it to a variable client
print('before client')
client = TelegramClient('session', api_id, api_hash)
  
# connecting and building the session
client.connect()

print('client connected')

if not client.is_user_authorized():
    print('Not authorized!')
    client.send_code_request(phone)
    print('after send code!') 
    # signing in the client
    client.sign_in(phone, input('Enter the code: '))
    sleep(10)
    keyboard.write(auth)
    keyboard.press_and_release('enter')
    exit()
    
    print('after signin!')
    
  
try:
    # receiver user_id and access_hash, use
    # my user_id and access_hash for reference
    print('authorized!')
    #receiver = InputPeerUser(5328300653, -1521208174660976255)
    print('after send message!')
    # sending message using telegram client
    #client.send_message(receiver, message, parse_mode='html')
except Exception as e:
     
    # there may be many error coming in while like peer
    # error, wrong access_hash, flood_error, etc
    print(e);
 
# disconnecting the telegram session
client.disconnect()