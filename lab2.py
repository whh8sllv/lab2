import sys

sys.stdout.write('Hello! \n'
                 'I am your text decoding assistant. \n'
                 'But I have to disappoint you with the fact that I can only decipher english letters, numbers, spaces and the character set - , . ! ? : ; * / \n'
                 'Also do not enter empty lines. \n'
                 'Enter your encrypted text: ')

def recode(txt):
    symbol_set = [',', '.', '!', '?', ':', ';', '*', '/', '-']
    normal_letters = 'abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.upper() + ' '
    coded_letters = 'nopqrstuvwxyzabcdefghijklm' + 'nopqrstuvwxyzabcdefghijklm'.upper() + ' '

    res = ''
    if txt.strip() == '':
        sys.stderr.write('Sorry but you entered an empty string :(')
        sys.exit(1)
    else:
        for i in txt:
            if i in normal_letters:
                char_index = coded_letters.index(i)
                res += normal_letters[char_index]
            elif i in symbol_set or i.isdigit():
                res += i
            else:
                sys.stderr.write(f'Sorry, your text contains a character that is contrary to the conditions: {i}')
                sys.exit(1)


    return res


if __name__ == '__main__':
    sys.stdout.write(f'Your decrypted text: {recode(sys.stdin.readline().strip())}')
