#!/usr/bin/python3
def best_score(a_dictionary):
    if not (a_dictionary):
        return None
    key_list = list(a_dictionary)
    value_list = list(a_dictionary.values())
    max = value_list[0]
    max_index = 0
    i = 0
    for each in value_list:
        if each > max:
            max = each
            max_index = i
        i += 1
    return key_list[max_index]
