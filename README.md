# twilio-tv

**Requirements**
* Python 3
* virtualenv
* Twilio account
* ngrok

**Local Development**
1. `git clone git@code.hq.twilio.com:hatch/twilio-tv.git`
2. `cd twilio-tv`
3. `virtualenv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`
6. `export PYTHONPATH=.`
7. `python main/main.py`
8. `python test/test_suite.py`

**Docker**
1. `docker build . -t hatch/twilio-tv`
2. `docker run -p 5000:5000 -e NAME=”hatch” hatch/twilio-tv:latest`

**Commands**
* 'ahoy/hi/Hi' : welcome message
* 'GET<space> ALLINFO' : To receive the information about all the channels.
* 'GET<space> MYINFO' : To receive the information about your channels.  
* 'ADD<space> Channel number' : To add the channel to your account.
* 'DROP<space> Channel number' : To drop the channel from your account.

**Twilio Setup**
1. Open a Twilio account.
2. Join the [Twilio WhatsApp sandbox](https://www.twilio.com/docs/whatsapp/sandbox).
3. Set up [ngrok](https://ngrok.com/) and start a tunnel to `localhost:5000`.
4. [Configure the WhatsApp sandbox](https://console.twilio.com/us1/develop/sms/settings/whatsapp-sandbox) to point to your ngrok tunnel.

**Access Required**

1. Buildkite
2. Admiral
3. Boxconfig
4. Twilio Engineering VPN




