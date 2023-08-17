#!/usr/bin/python3
# A Function that converts a Roman numeral to an integer.

def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) != str):
        return 0

    decimal = 0
    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    for i in range(0, len(roman_string)):
        if i == len(roman_string) - 1:
            decimal += roman[roman_string[i]]
        elif roman[roman_string[i]] >= roman[roman_string[i + 1]]:
            decimal += roman[roman_string[i]]
        else:
            decimal -= roman[roman_string[i]]

    return(decimal)
