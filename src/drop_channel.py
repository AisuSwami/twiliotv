import re
from libs import util

#function for droping channels from the account
def dropchannel(incoming_msg, sender):

    #regular exprestion for the request formate validation
    incomin_request_regex = re.compile(r'drop \d\d\d')

    #Boolean variable for checking the user Input request with the regular exprestion
    valid_request = incomin_request_regex.match(incoming_msg.lower())
    response = ''

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

             #boolean variable for validating the user channel number exist or not
            channelnumber_exist = False  
            for obj in util.account_list:

                #validating the sender phone number already exits in account_list and 
                #the channel number user trying to drop the channel number  which is subscribed before.
                if obj.phone == sender and my_channel in obj.channel:
                    obj.channel = __get_updated_channels(obj.channel, my_channel)
                    channelnumber_exist = True
                    response = 'Channel *' + util.ALL_CHANNELS.get(my_channel) + '* removed successfully.\n' + util.MYINFO
                    return response

            # user trying to drop the channel number which is not subscribed.
            if not channelnumber_exist:    
                response = util.INVALID_REQUEST + '\n ' + 'Requested channel is not subscribed.\n' + util.MYINFO
                return response 


def __get_updated_channels(mychannels,channel_number):
    channels_arr = list(mychannels.split(','))
    channels_arr.remove(channel_number)
    mychannel = '' 
    mychannel += ','.join(channels_arr)  
    # return string  
    return mychannel    
