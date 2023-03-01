import random

def seedEncrypt(string, key):
    random.seed(key)
    
    encrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    length = len(alphabet)
    for i in range(len(string)):
        num = int(random.random()*length)
        encrypted += alphabet[(alphabet.index(string[i]) + key*num) % length]

    return encrypted
def seedDecrypt(string, key):
    random.seed(key)

    decrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+{}|:\"<>?[]\;',./`~ "
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    length = len(alphabet)
    for i in range(len(string)):
        num = int(random.random() *length) 
        b = alphabet.index(string[i])
        x = num*key
        m = length
        num = m+b-x
        sc = int(num/length)
        decrypted += alphabet[m+b-x-length*sc]

    return decrypted

def caesar(string, shift, encrypted):
    returned = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(string)):
        try:
            b = alphabet.index((string[i]).lower())
            if encrypted:
                returned += alphabet[(b+shift) % 26]
            else:
                returned += alphabet[(b-shift) % 26]
        except:
            returned += " "

    return returned
def playfair(string, key, encrpyt):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_key = ""

    for letter in key:
        if letter not in final_key:
            final_key += letter

    letters = final_key
    string = string.replace(" ", "")
    if len(string) % 2 != 0: string += "x"

    strng = ""

    for i in range(len(string)):
        if i % 2 == 0: strng += " "
        strng += string[i]
    
    pairs = strng.strip().lower().split(" ")

    table = [ [""]*5 for i in range(5) ]
    h = len(table)
    w = len(table[0])

    shift = int(encrpyt == True) 
    for k in range(len(key)):
        i = int(k/w)
        j = k % h
        table[i][j] = key[k]

    for letter in alphabet:
        if letter not in final_key:
            k = len(letters)
            i = int(k/w)
            j = k % h
            if i < w:
                if (letter != 'j'):
                    table[i][j] = letter
                    letters += letter
        else:
            continue
    
    returned = ""

    for i in range(len(pairs)):
        letter = pairs[i]

        while True:
            try:
                k0 = letters.index(letter[0])
                pos0 = (int(k0/w), k0%w)

                k1 = letters.index(letter[1])
                pos1 = (int(k1/w), k1%w)

                # if same column
                if (pos0[1] == pos1[1]):
                    i0 = (pos0[0]-1 + 2*shift) % w
                    i1 = (pos1[0]-1 + 2*shift) % w
                    if(i0 < 0): i0 = w-1
                    if(i1 < 0): i1 = w-1
                    returned += table[i0][pos0[1]]
                    returned += table[i1][pos1[1]]
                # if same row
                elif (pos0[0] == pos1[0]):
                    i0 = (pos0[1]-1 + 2*shift) % h
                    i1 = (pos1[1]-1 + 2*shift) % h
                    if(i0 < 0): i0 = h-1
                    if(i1 < 0): i1 = h-1
                    returned += table[pos0[0]][i0]
                    returned += table[pos1[0]][i1]
                # if not in same column or row
                else:
                    returned += table[pos0[0]][pos1[1]]
                    returned += table[pos1[0]][pos0[1]]
                break
            except:
                if letter[0] == 'j': letter = 'i' + letter[1]
                if letter[1] == 'j': letter = letter[0] + 'i'
                continue
            
        # returned += " "

    return returned.strip()
def vignere(string, key, encrypted):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    returned = ""
    for i in range(len(string)):
        try:
            col = alphabet.index(key[i % len(key)])
            row = alphabet.index(string[i].lower())

            if encrypted:
                returned += alphabet[(col + row) % 26]
            else:
                returned += alphabet[row - col]
        except:
            returned += " "

    return returned
def atbash(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    first = alphabet[0:13]
    second = alphabet[13:][::-1]

    returned = ""
    for letter in string:
        letter = letter.lower()
        try:
            if letter in first:
                returned += second[first.index(letter)]
            elif letter in second:
                returned += first[second.index(letter)]
            else: returned += " "
        except:
            returned += " "
    return returned

message = "this is a cool test"
key = "heytasdf"
cipher = "playfair"

if cipher == 'caesar':
    encrypted = caesar(message, key, True)
    print("Encrypted: " + encrypted)
    print("Decrypted: " + caesar(encrypted, key, False))
elif cipher == 'playfair':
    encrypted = playfair(message, key, True)
    print("Encrypted: " + encrypted)
    print("Decrypted: " + playfair(encrypted, key, False))
elif cipher == 'vignere':
    encrypted = vignere(message, key, True)
    print("Encrypted: " + encrypted)
    print("Decrypted: " + vignere(encrypted, key, False))
elif cipher == 'atbash':
    encrypted = atbash(message)
    print("Encrypted: " + encrypted)
    print("Decrypted: " + atbash(message))



