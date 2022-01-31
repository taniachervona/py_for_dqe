import random
import string


# 1. create a list of random number of dicts (from 2 to 10)
#
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

list_of_dict = []  # variable initialization
for i in range(random.randint(2, 10)):  # create cycle for get qty of elements in list
    dict_var = {}
    for j in range(random.randrange(10)):  # create cycle for get qty of items for element in list
        dict_var[random.choice(string.ascii_lowercase)] = \
            random.randrange(100)  # chose random key from letters in low register and values in diapazone 0-100
    list_of_dict.append(dict_var)  # add element to list



# 2. get previously generated list of dicts and create one common dict:
#
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

return_dict, reject_keys = {}, []  # variable initialization for final dict and repeat keys
for element in list_of_dict:  # create cycle for list of dictionaries
    for key, value in element.items():  # create cycle for items in every dict
        if key not in reject_keys:  # check is key in reject list of keys
            if key not in return_dict.keys():  # condition for detect is key present in final dict
                return_dict[key] = value  # add value to final dict
            else:
                reject_keys.append(key)  # add key, which should not be checked for next dicts from list
                del return_dict[key]  # delete value from final dict in case we have duplicates
                max_dict, count_var = {}, 0  # variable initialization for find max value
                for found_max in list_of_dict:  # create cycle for find max value in list of dict
                    count_var += 1  # increase counter variable
                    for k, v in found_max.items():  # create cycle for items in every dict
                        if k == key:  # check condition when key in dict quel to checked one
                            max_dict[key + f'_{count_var}'] = v  # add value to special dict to find max value
                max_key = [c for c, d in max_dict.items()
                           if d == max(max_dict.values())]  # find key for max value from max dict
                return_dict[max_key[0]] = \
                    max(max_dict.values())  # add max key: value to final dict
