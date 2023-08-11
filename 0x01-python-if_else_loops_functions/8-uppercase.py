#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        let = ord(letter)
        if let >= 97 and let < 124:
            let = let - 32
        print("{}".format(chr(let)), end='')
    print()
