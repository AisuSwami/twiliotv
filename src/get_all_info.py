from libs import util


# Gets all the channels information provided by network
def getallinfo():
        getallinfomsg = util.ALL_INFO_HEADER
        for key in util.ALL_CHANNELS:
            getallinfomsg += '*' + str(key) + '*' + '\t' + '-->' + '\t' + \
                str(util.ALL_CHANNELS[key]) + '\n'
        return getallinfomsg