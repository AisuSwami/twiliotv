# Testing the drop channel
import sys
import unittest
sys.path.append('../')

from src import add_channel
from src import drop_channel   # Module
from libs import util


class TestDropChannel(unittest.TestCase):

    # setting sender and account_list
    def setUp(self):
        util.account_list = []
        self.sender = '8884104237'

    # test drop channel with lower case
    def test_drop_channel_lower(self):
        incoming_msg = 'drop 101'
        util.account_list.append(add_channel.Account(self.sender, '101'))
        expected_output = 'AAJ_TAK'
        actual_output = drop_channel.dropchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # test drop channel with multiple channel
    def test_drop_channel_with_multi_channel(self):
        incoming_msg = 'DROP 102'
        util.account_list.append(add_channel.Account(self.sender, '103'))
        util.account_list.append(add_channel.Account(self.sender, '102'))
        expected_output = 'ABP News'
        actual_output = drop_channel.dropchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # test drop channel when the channel not subscribed
    def test_drop_channel_channel_not_subscribed(self):
        incoming_msg = 'drop 105'
        expected_output = 'Requested channel is not subscribed'
        actual_output = drop_channel.dropchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # test drop channel with invalid channel number
    def test_drop_channel_invalid_channel_number(self):
        incoming_msg = 'drop 5000'
        expected_output = 'Requested channel is not part of subscription'
        actual_output = drop_channel.dropchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # test drop channel with invalid format with dot
    def test_drop_channel_with_dot(self):
        incoming_msg = 'drop .101'
        expected_output = 'Invalid Request'
        actual_output = drop_channel.dropchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # test drop channel with channel name
    def test_drop_channel_with_channel_name(self):
        incoming_msg = 'drop ABP News'
        expected_output = 'Invalid Request'
        actual_output = drop_channel.dropchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

    # test drop channel without channel number
    def test_drop_channel_with_no_channel_number(self):
        incoming_msg = 'drop'
        expected_output = 'Invalid Request'
        actual_output = drop_channel.dropchannel(incoming_msg, self.sender)
        self.assertIn(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()