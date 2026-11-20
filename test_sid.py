import unittest
from sid import digit_sum, lucky_number

MY_SID4 = 1089


class TestSid(unittest.TestCase):
    def test_digit_sum(self):
        self.assertEqual(digit_sum(1234), 10)

    def test_lucky_number(self):
        self.assertEqual(lucky_number(1234), 1)

    def test_my_sid(self):
        self.assertEqual(lucky_number(MY_SID4), 9)
