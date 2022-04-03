# This file contains all the messages and global variables

GREET_MSG = '''
            *Thank you for connecting with Twilio TV. You can do the following by just typing the messages in the required format:*

 > *GET*<space> *ALLINFO* : To receive the information about all the channels.
 > *GET*<space> *MYINFO* : To receive the information about your channels.  
 > *ADD*<space> *Channel number* : To add the channel to your account.
 > *DROP*<space> *Channel number* : To drop the channel from your account.

    *Note: Request is not case sensitive* '''

INVALID_REQUEST = ' *Invalid Request*'

ALL_INFO_HEADER = 'Thank you for your request. All channels Information are listed below:\n\n*CH.NO   CH.Name*\n'

CHAT_KEYWORDS = ['hello','hi','hey','start','hii','ahoy','ola']

ALL_CHANNELS = { '101':'AAJ_TAK',
 '102':'ABP News',
 '103':'Aryan TV','104':'CNBC','105':'Awaaz','106':'DD News','107':'Good News'}

MYINFO = 'Type *GET*<space> *MYINFO* to get the channel details.'

ALLINFO = 'Requested channel is not part of subscription.\n Type *GET*<space> *ALLINFO* to get all channels.'

ADDCHANNEL = 'Please subscribe to to the channel by Typing *ADD*<space> *Channel number*'

MYINFO_HEADER = 'Thank you for your request. Below you have your subscribed channels Information \n\n*CH.No*  *CH.Name* \n'

# creating list       
account_list = []

# Gets the channel name from ALL_CHANNELS for the channel number
def get_channelname(channel_number):
    return ALL_CHANNELS.get(channel_number)