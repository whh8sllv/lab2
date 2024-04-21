import sys
import unittest
import lab2
import io

class TestRecode(unittest.TestCase):

    def test_recode_lower_string_equal(self):
        self.assertEqual(lab2.recode('qngn fpvrapr'), 'data science')

    def test_recode_default_string_equal(self):
        self.assertEqual(lab2.recode('Anfgvn Xbinypuhx'), 'Nastia Kovalchuk')

    def test_recode_upper_string_equal(self):
        self.assertEqual(lab2.recode('FBSGJNER QRIRYBCZRAG'), 'SOFTWARE DEVELOPMENT')

    def test_recode_symbol_string_equal(self):
        self.assertEqual(lab2.recode('xcv/vcg/sv'), 'kpi/ipt/fi')

    def test_recode_digit_string_equal(self):
        self.assertEqual(lab2.recode('123456789'), '123456789')

    def test_recode_wrong_input(self):
        self.assertFalse(lab2.recode('             '))
        self.assertFalse(lab2.recode('_hello_world_'))
        self.assertFalse(lab2.recode('привіт світ!'))


if __name__ == '__main__':
    unittest.main()