# Test cases for get all channel information
import sys
import unittest

sys.path.append('../')

from src import get_all_info


class TestGetAllInfo(unittest.TestCase):

    # Setting up the expected list
    def setUp(self):
        self.expected_list = ['AAJ_TAK', 'ABP News', 'Aryan TV',
            'CNBC', 'Awaaz', 'DD News', 'Good News']

    # test get all info
    def test_get_all_info(self):
        actual_output = get_all_info.getallinfo()
        for channel in self.expected_list:
            self.assertIn(channel, actual_output)

if __name__ == '__main__':
    unittest.main()