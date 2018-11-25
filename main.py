from  startchat import start_chat
from getdetail import get_details
from pip._vendor.distlib.compat import raw_input
from spydetails import spy, friends
from steganography.steganography import Steganography
from datetime import datetime

print("Hello! Let\'s get started")
question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N)? "
existing = raw_input(question)

if existing == "Y"or existing=="y":
    start_chat(spy['name'], spy['age'], spy['rating'])
else:
    get_details()

