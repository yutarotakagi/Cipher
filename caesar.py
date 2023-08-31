# cording: uft-8

import string

def Caesar():
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    original = map(str, input("original text : "))
    num = int(input("index : "))
    output = ''
    for i in original:
        if i in lowercase:
            i = lowercase[(lowercase.index(i) + num) % 26]
        elif i in uppercase:
            i = uppercase[(uppercase.index(i) + num) % 26]
        output += i
    print(output)

if __name__ == "__main__":
    Caesar()