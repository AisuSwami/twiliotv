#addchannel.py program for adding the channels to account.
import re
from libs import util

#Class for Account with phone and channel 
class Account: 

    def __init__(self, phone, channel):
        self.phone = phone 
        self.channel = channel

#function for adding channels to the account
def addchannel(incoming_msg, sender):
    '''Function for adding channels to the account'''
    response = ''
    #regular exprestion for the request formate validation
    incomin_request_regex = re.compile(r'add \d\d\d')

    #Boolean variable for checking the user Input request with the regular exprestion
    valid_request = incomin_request_regex.match(incoming_msg.lower())

    #validating the user Input request format
    if not valid_request:
        response = util.INVALID_REQUEST + '\n ' + util.GREET_MSG
        return response

    elif valid_request:

        #retrieving the channel number to add from input request
        my_channel = incoming_msg.split(' ')[1]

        #validating the channel number
        if my_channel not in util.ALL_CHANNELS:
            response = util.INVALID_REQUEST + '\n '+util.ALLINFO
            return response
            
        else:
            #boolean variable for validating the user phone number exist or not 
            phonenumber_exist = False
            for obj in util.account_list:

                #validating the sender phone number already exits in account_list and 
                #the channel number user trying to add is not subscribed before.
                if obj.phone == sender and my_channel not in obj.channel:

                    #appending the channel to user account
                    obj.channel = obj.channel + ',' + my_channel
                    phonenumber_exist = True
                    response= 'Channel *' + util.get_channelname(my_channel) + '* added successfully.\n' + util.MYINFO
                    return response
                    
                elif obj.phone == sender and my_channel in obj.channel:
                    response = util.INVALID_REQUEST + '\n You are already subscribed to this channel \n ' + util.MYINFO
                    return response

            #valdating for new user and appending the user to to account_list 
            if not phonenumber_exist :    
                util.account_list.append(Account(sender, my_channel))
                response = 'Channel *' + util.get_channelname(my_channel) + '* added successfully.\n' + util.MYINFO
                return response
            
