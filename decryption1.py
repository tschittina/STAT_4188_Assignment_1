cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

encrypted_file = open("encrypted_message_one.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write code below
reverse_cipher = {y: x for x, y in cipher.items()}
decrypted_message = ""
for char in encrypted_message:
    new_char = reverse_cipher[char]
    decrypted_message += new_char
print(decrypted_message)