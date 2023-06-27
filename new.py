import string
import collections

ALPHABET_SIZE = 26 

alphabet_dict = {char: i for i, char in enumerate(string.ascii_uppercase)}
numb_dic = {i: char for i, char in enumerate(string.ascii_uppercase)}

def count_chars(ciphertext, key_length, index):
    count = collections.Counter()
    for i, c in enumerate(ciphertext):
        if i % key_length == index:
            count[c] += 1
    return count

def count_unique_chars(ciphertext, key_length):
    count = collections.Counter()
    for i, c in enumerate(ciphertext):
        if i % key_length == 0:
            count[c] += 1
    return len(count)

def removeSpaces(text): 
    text = text.lower() 
    text = text.replace(" ","")
    return text

def enc(plainText, key):
    key = list(key)
    if len(plainText) == len(key): 
        return(key) 
    else: 
        for i in range(len(plainText) -len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key))

def encrypt(plainText, key):
    plainText=removeSpaces(plainText) 
    key=enc(plainText, key)
    cipherText = [] 
    for i in range(len(plainText)): 
        x = (alphabet_dict[plainText[i]] + alphabet_dict[key[i]]) % 26
        cipherText.append(numb_dic[x]) 
    return("" . join(cipherText))

def ioc(ciphertext):
    char_count = collections.Counter(ciphertext)
    N = len(ciphertext)
    numerator = sum(n * (n - 1) for n in char_count.values())
    denominator = N * (N - 1)
    ioc_value = numerator / denominator
    return ioc_value
def find_key_length(ciphertext):
    key_length = 2
    coincidence = 0.05
    while True:
        blocks = [ciphertext[i: i + key_length] for i in range(0, len(ciphertext), key_length)]
        block_star = ''.join([block[0] for block in blocks])
        ci = ioc(block_star)
        if ci > coincidence:
            return key_length
        key_length += 1

def find_key(ciphertext, key_length):
    key = ""
    for i in range(key_length):
        count = count_chars(ciphertext, key_length, i)
        sorted_items = sorted(count.items(), key=lambda x: -x[1])
        most_common_char = str(sorted_items[0][0])
        key_shift = char_to_num(most_common_char) - char_to_num("E")
        key += num_to_char(key_shift % ALPHABET_SIZE)
    return key

def char_to_num(char):
    return ord(char) - 65

def num_to_char(num):
    return chr(num + 65)

def decode_vigenere(ciphertext, key):
    plaintext = []
    key_len = len(key)
    for i, char in enumerate(ciphertext):
        if not char.isalpha():
            plaintext.append(char)
        else:
            shift = char_to_num(key[i % key_len])
            num = (char_to_num(char) - shift) % ALPHABET_SIZE
            plaintext.append(num_to_char(num))
    return ''.join(plaintext)

ciphertext = input("Enter ciphertext: ").upper()
key_length = find_key_length(ciphertext)
if key_length == -1:
    print("Could not find the key length")
else:
    print("Key length is: ", key_length)
    key = find_key(ciphertext, key_length)
    print("Key is: ", key)
    plaintext = decode_vigenere(ciphertext, key)
    print("Plaintext:", plaintext)
