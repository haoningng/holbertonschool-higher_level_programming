#!/usr/bin/python3
def roman_to_int(roman_string):
    units = ['I', 'II', 'III', 'IV', 'V', 'VI', "VII", 'VIII', 'IX']
    tens = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = ['M', 'MM', 'MMM']
    total = 0
    if not (isinstance(roman_string, str)):
        return total
    nested_list = {tuple(thousands): 1000, tuple(hundreds): 100,
                   tuple(tens): 10, tuple(units): 1}
    for key, value in nested_list.items():
        for each in list(reversed(key)):
            if each in roman_string:
                if (roman_string.index(each) == 0):
                    total += (key.index(each) + 1) * value
                    roman_string = roman_string.replace(each, '')
                    break
    return total
