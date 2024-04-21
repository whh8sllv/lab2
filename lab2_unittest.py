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

    def test_recode_empty_input(self):
        with self.assertRaises(SystemExit) as cm:
            lab2.recode('             ')
        self.assertEqual(cm.exception.code, 1)

    def test_recode_wrong_symbols(self):
        with self.assertRaises(SystemExit) as cm:
            lab2.recode('_hello_world_')
        self.assertEqual(cm.exception.code, 1)

    def test_recode_wrong_alphabet(self):
        with self.assertRaises(SystemExit) as cm:
            lab2.recode('привіт світ!')
        self.assertEqual(cm.exception.code, 1)




if __name__ == '__main__':
    unittest.main()