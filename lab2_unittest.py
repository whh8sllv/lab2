import unittest
import lab2
import sys
import io

class TestRecode(unittest.TestCase):

    def test_recode_lower_string_equal(self):
        self.assertEqual(lab2.recode('qngn fpvrapr'), 'data science')

    def test_recode_default_string_equal(self):
        self.assertEqual(lab2.recode('Anfgvn Xbinypuhx'), 'Nastia Kovalchuk')

    def test_recode_upper_string_equal(self):
        self.assertEqual(lab2.recode('FBSGJNER QRIRYBCZRAG'), 'SOFTWARE DEVELOPMENT')

    def test_recode_symbol_string_equal(self):
        self.assertEqual(lab2.recode(',.!?:;*/'), ',.!?:;*/')

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
            lab2.recode('привіт світ')
        self.assertEqual(cm.exception.code, 1)

    def test_code_successful(self):
        input_text = 'hello world'
        correct_output = 'Your decrypted text: uryyb jbeyq'
        sys.stdin = io.StringIO(input_text)
        sys.stdout = io.StringIO()

        with self.assertRaises(SystemExit) as cm:
            lab2.main()
        self.assertEqual(cm.exception.code, 0)
        self.assertEqual(sys.stdout.getvalue(), correct_output)


    def test_code_unsuccessful(self):
        invalid_input_and_errors = [['   ', 'Sorry but you entered an empty string :('],
                         [':-)', 'Sorry, your text contains a character that is contrary to the conditions'],
                         ['Перемога', 'Sorry, your text contains a character that is contrary to the conditions']]
        for user_txt, errors in invalid_input_and_errors:
            sys.stdin = io.StringIO(user_txt)
            sys.stdout = io.StringIO()
            sys.stderr = io.StringIO()

            with self.assertRaises(SystemExit) as cm:
                lab2.main()
            self.assertEqual(cm.exception.code, 1)
            self.assertEqual(sys.stderr.getvalue(), errors)


if __name__ == '__main__':
    unittest.main()