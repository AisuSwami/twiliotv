from libs import util


#function to get all the subscribed channels.
def getmyinfo(sender):
    my_channels = False
    my_info = util.MYINFO_HEADER
    response = ''
    
    #validating the sender phone number already exits in account_list and 
    #getting the channel details subscribed.
    for obj in util.account_list:
        if obj.phone == sender:
            if obj.channel:
                my_channels = True
                for channel in obj.channel.split(','):
                    my_info += '*' + channel + '*' + ' --> ' + util.get_channelname(channel) +'\n'
                response = my_info
                return response
            
    if not my_channels:
        response = 'No channels subscribed ' + '\n ' +util.ADDCHANNEL
        return response
        