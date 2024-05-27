#!/usr/bin/env python3

import unittest, logging

class TestTestCase(unittest.TestCase):
    def setUp(self):
        logging.info('Setup')
        logging.info('------------')

    def test_succeedingTest(self):
        logging.info('This test always succeeds')
        logging.info('------------')
        self.assertTrue(True);

    def test_failingTest(self):
        logging.info('This test always fails')
        logging.info('------------')
        self.assertTrue(False);


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
