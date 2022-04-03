# To test the add channel
import sys
import unittest

sys.path.append('../')

from src import add_channel
from libs import util


class TestAddChannel(unittest.TestCase):

    # Setting up sender number
    def setUp(self):
        self.sender = '8884104237'
        util.account_list = []

    # Test add channel lower case
    def test_add_channel_lower(self):
        incoming_msg = 'add 101'
        expected_output = 'AAJ_TAK'
        actual_output = add_channel.addchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # Test add channel upper case
    def test_add_channel_upper(self):
        incoming_msg = 'ADD 102'
        expected_output = 'ABP News'
        actual_output = add_channel.addchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # Test add channel same channel
    def test_add_channel_same_channel(self):
        incoming_msg = 'ADD 101'
        expected_output = 'already subscribed'
        add_channel.addchannel(incoming_msg, self.sender)
        # Adding the same channel again 
        actual_output = add_channel.addchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # Test add invalid channel number
    def test_add_channel_invalid_channel_number(self):
        incoming_msg = 'ADD 500'
        expected_output = 'Requested channel is not part of subscription'
        actual_output = add_channel.addchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # Test add channel with invalid formate
    def test_add_channel_with_dot(self):
        incoming_msg = 'add. 103'
        expected_output = 'Invalid Request'
        actual_output = add_channel.addchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # Test add channel with channel name
    def test_add_channel_with_channel_name(self):
        incoming_msg = 'add ABP News'
        expected_output = 'Invalid Request'
        actual_output = add_channel.addchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # Test add channel with no channel number
    def test_add_channel__with_no_channel_number(self):
        incoming_msg = 'add'
        expected_output = 'Invalid Request'
        actual_output = add_channel.addchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()