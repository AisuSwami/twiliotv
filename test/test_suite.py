# Test suite for all test cases
import unittest

import test_add_channel
import test_drop_channel
import test_get_all_info
import test_get_my_info
import test_main


# test suite function
def suite():

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_main.TestMainGreetFunction))
    suite.addTest(unittest.makeSuite(test_add_channel.TestAddChannel))
    suite.addTest(unittest.makeSuite(test_drop_channel.TestDropChannel))
    suite.addTest(unittest.makeSuite(test_get_all_info.TestGetAllInfo))
    suite.addTest(unittest.makeSuite(test_get_my_info.TestGetMyInfo))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)