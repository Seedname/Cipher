import random

def playfair(string, key, encrpyted):
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

    shift = int(encrpyted == True) 
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
    key = key.replace(" ", "")
    returned = ""
    for i in range(len(string)):
        try:
            col = alphabet.index(key[i % len(key)].lower())
            row = alphabet.index(string[i].lower())

            if encrypted:
                returned += alphabet[(col + row) % 26]
            else:
                returned += alphabet[row - col]
        except:
            returned += " "

    return returned
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
def seed(string, key, encrypted):
    random.seed(key)

    returned = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    length = len(alphabet)
    for i in range(len(string)):
        try:
            num = int(random.random() *length) 
            if encrypted:
                returned += alphabet[(alphabet.index(string[i].lower()) + key*num) % length]
            else:            
                b = alphabet.index(string[i].lower())
                x = num*key
                m = length
                num = m+b-x
                sc = int(num/length)
                returned += alphabet[m+b-x-length*sc]
        except:
            returned += " "

    return returned
def rot13(string):
    return caesar(string, 13, True)
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

ciphers = [playfair, vignere, caesar, seed, rot13, atbash]
while True:
    try:
        string = "\nWhich cipher would you like to use?\n"
        for i in range(len(ciphers)):
            string += str(i) + ". " + ciphers[i].__name__ + "\n"

        try:
            cipher = ciphers[int(input(string))]
        except:
            print("\nPlease input an integer(0-" + str(len(ciphers)) + ")\n")
            continue


        message = str(input("\nWhat is your message?\n"))
        
        if cipher == rot13 or cipher == atbash:
            print("\nMessage: " + cipher(message) + "\n\n")
        else:
            encrypt = str(input("\nWould you like to encrypt or decrypt? (e/d)\n"))[0] == "e"
            if cipher == playfair or cipher == vignere:
                key = str(input("\nWhat is your key?\n"))
                print("\nMessage: " + cipher(message, key, encrypt) + "\n\n")
            if cipher == caesar or cipher == seed:
                key = int(input("\nWhat is your key?\n"))
                print("\nMessage: " + cipher(message, key, encrypt) + "\n\n")
    

        if str(input("Generate more ciphertext? (y/n)\n"))[0] == 'y': continue
        break
    except:
        print("\nPlease enter valid values.")

