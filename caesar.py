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

string = "ynkooejcpdanqxeykjrbdofgkq"

for i in range(1, 25):
    print(caesar(string, i, False))