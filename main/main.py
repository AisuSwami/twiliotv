from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import sys
sys.path.append('../')

from src import add_channel
from src import drop_channel
from src import get_all_info
from src import get_my_info
from libs import util 

app = Flask(__name__)


# Handles the incoming request from WhatsApp 
@app.route('/handle_message', methods=['POST'])
def handle_message():
    # To fetch the phone number
    sender = request.values.get('From').split(':')[1]
    
    # It takes the incoming message from the user
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()
    responded = False

    # Validates the incoming message from the user
    if incoming_msg in util.CHAT_KEYWORDS:
        msg.body(util.GREET_MSG)
        responded = True
    
    #  Validates the incoming message from the user for GET ALLINFO
    elif incoming_msg == 'get allinfo':    
        getallmessage = get_all_info.getallinfo()
        msg.body(getallmessage)
        responded = True
    
    # Validates the incoming message from the user for adding channel 
    elif incoming_msg.startswith('add '): 
        response_msg = add_channel.addchannel(incoming_msg,sender)
        msg.body(response_msg)
        responded = True

    # Validates the incoming message from the user for droping channel 
    elif incoming_msg.startswith('drop '): 
        response_msg = drop_channel.dropchannel(incoming_msg,sender)
        msg.body(response_msg)
        responded = True

    # Validates the incoming message from the user to get his/her channel's information 
    elif incoming_msg == 'get myinfo': 
        get_myinfo_message = get_my_info.getmyinfo(sender)
        msg.body(get_myinfo_message)
        responded = True

    # Invalidates the incoming message from the user  
    if not responded:
        msg.body(util.INVALID_REQUEST + '\n ' + util.GREET_MSG)
    return str(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')