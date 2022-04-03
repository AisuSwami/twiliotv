import sys
import unittest

sys.path.append('../')

from src import add_channel 
from libs import util
from src import get_my_info



class TestGetMyInfo(unittest.TestCase):

    def setUp(self):
        self.sender = '8619451343'
        util.account_list = []

    # test case for one channel info
    def test_get_my_info(self):

        my_channel = '101'
        util.account_list.append(add_channel.Account(self.sender, my_channel))
        expected_output = 'AAJ_TAK'
        actual_output = get_my_info.getmyinfo(self.sender)
        self.assertIn(expected_output, actual_output)

    # test case for multi channel info
    def test_get_my_info_multi_channel(self):

        my_channel = '101,102,105'
        util.account_list.append(add_channel.Account(self.sender, my_channel))
        expected_output_list = ['AAJ_TAK', 'ABP News', 'Awaaz']
        actual_output = get_my_info.getmyinfo(self.sender)

        for expected_output in expected_output_list:
            self.assertIn(expected_output, actual_output)

    # test case for no channel info
    def test_get_my_info_no_channel(self):

        my_channel = ''
        util.account_list.append(add_channel.Account(self.sender, my_channel))
        expected_output = 'No channels subscribed'
        actual_output = get_my_info.getmyinfo(self.sender)
        self.assertIn(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()