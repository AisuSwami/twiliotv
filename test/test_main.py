import sys
import unittest
from  unittest import mock

sys.path.append('../')

# importing app for FlaskClient[Response]
from main import main 
from main.main import app
from libs import util
from src import add_channel

 
class TestMainGreetFunction(unittest.TestCase):

    # Setting up sender number
    def setUp(self):
        self.sender = 'ABC:8610898981'
        util.account_list = []

    # request handle message
    def request_handle_message(self, From , Body):
        with app.test_client() as client:
            return client.post('/handle_message', data=dict(
                From=From,
                Body=Body
            ), follow_redirects=True)

    # test handle valid request
    def test_handle_valid_request(self):
        expected_chat_keywords = ['hello','hi','hey','start','hii','ahoy','ola']
        for keyword in expected_chat_keywords:
            actual_output = self.request_handle_message(self.sender, keyword )
            self.assertNotIn(util.INVALID_REQUEST, str(actual_output.data)) 

    # test handle valid add request
    def test_handle_valid_add_request(self):

        incoming_msg = 'add 101'
        expected_output = 'AAJ_TAK'
        actual_output = self.request_handle_message(self.sender,incoming_msg)
        self.assertIn(expected_output, str(actual_output.data)) 

    # test handle valid drop request
    def test_handle_valid_drop_request(self):
        
        incoming_msg = 'drop 101'
        expected_output = 'AAJ_TAK'
        util.account_list.append(add_channel.Account('8610898981', '101'))
        actual_output = self.request_handle_message(self.sender,incoming_msg)
        self.assertIn(expected_output, str(actual_output.data)) 

    # test handle valid get my info request
    def test_handle_valid_get_my_info_request(self):
        
        incoming_msg = 'get myinfo'
        expected_output = 'AAJ_TAK'
        util.account_list.append(add_channel.Account('8610898981', '101'))
        actual_output = self.request_handle_message(self.sender,incoming_msg)
        self.assertIn(expected_output, str(actual_output.data)) 

    # test handle valid get all info request
    def test_handle_valid_get_all_info_request(self):
        
        incoming_msg = 'get allinfo'
        expected_list = ['AAJ_TAK', 'ABP News', 'Aryan TV',
            'CNBC', 'Awaaz', 'DD News', 'Good News']
        actual_output = self.request_handle_message(self.sender,incoming_msg)
        for channel in expected_list:
            self.assertIn(channel, str(actual_output.data))

    # test handle invalid request
    def test_handle_invalid_request(self):
      
        incoming_msg = 'bye'
        actual_output = self.request_handle_message(self.sender, incoming_msg)
        self.assertIn(util.INVALID_REQUEST, str(actual_output.data))


if __name__ == '__main__':
    unittest.main()