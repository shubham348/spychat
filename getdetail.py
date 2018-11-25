from startchat import start_chat
from pip._vendor.distlib.compat import raw_input
from spydetails import spy, friends
from steganography.steganography import Steganography
from datetime import datetime

def get_details():
    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    spy['salutation'] = raw_input("Should I call you Mr. or Ms.?: ")

    spy['age'] = raw_input("What is your age?")
    spy['age'] = int(spy['age'])

    spy['rating'] = raw_input("What is your spy rating?")
    spy['rating'] = float(spy['rating'])

    spy_is_online = True

    start_chat(spy['name'], spy['age'], spy['rating'])
