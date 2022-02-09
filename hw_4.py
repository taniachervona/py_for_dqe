import random
import string


def create_random_list_of_dict():
    list_of_dict = []
    for i in range(random.randint(2, 10)):
        dict_var = {}
        for j in range(random.randrange(10)):
            dict_var[random.choice(string.ascii_lowercase)] = \
                random.randrange(100)
        list_of_dict.append(dict_var)
    return list_of_dict


def found_max_value(list_of_dict: list[dict], key: str):
    max_dict, count_var = {}, 0
    for found_max in list_of_dict:
        count_var += 1
        for k, v in found_max.items():
            if k == key:
                max_dict[key + f'_{count_var}'] = v
    return {k: v for k, v in max_dict.items()
            if v == max(max_dict.values())}


def create_dict_with_unique_keys(list_of_dict: list[dict]):
    return_dict = {}
    for element in list_of_dict:
        for key, value in element.items():
            if key not in return_dict.keys():
                return_dict[key] = value
            else:
                del return_dict[key]
    return return_dict


def create_common_dict():
    """
    final function with the initial order of the elements in the list
    :return:
    """
    list_of_dict = create_random_list_of_dict()
    return_dict, reject_keys = {}, []
    for element in list_of_dict:
        for key, value in element.items():
            if key not in reject_keys:
                if key not in return_dict.keys():
                    return_dict[key] = value
                else:
                    reject_keys.append(key)
                    del return_dict[key]
                    max_item = found_max_value(
                        list_of_dict=list_of_dict, key=key)
                    return_dict.update(max_item)
    return return_dict


def create_common_dict_v2():
    """
    final function with the next order of the elements in the list:
    first unic keys, next - with max value
    :return:
    """
    list_of_dict = create_random_list_of_dict()
    return_dict = create_dict_with_unique_keys(
        list_of_dict=list_of_dict)
    for element in list_of_dict:
        for key, value in element.items():
            if key not in return_dict:
                max_item = found_max_value(
                        list_of_dict=list_of_dict, key=key)
                return_dict.update(max_item)
    return return_dict


#######################################################################################################################
str_var = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

sep_with_colon = str_var.split(sep=':')
sep_with_point = sep_with_colon[1].split(sep='.')


def check_and_leave_paragraphs():
    input_var = ''
    for i in sep_with_point[:-1]:
        if i.startswith("\t") is True \
                or i.startswith("\n") is True:
            item = '\n\t' + f'{i}.'.lstrip().capitalize()
            print(item)
        else:
            item = ' ' + f'{i}.'.lstrip().capitalize()
        input_var = input_var + item
    return input_var


def normalize_text_in_var():
    result_str = sep_with_colon[0].capitalize() + ':'
    return result_str + check_and_leave_paragraphs()


def create_new_sentence():
    new_sentence = ''
    for i in sep_with_point[:-1]:
        split_str = i.lstrip().split()
        new_sentence = new_sentence + split_str[-1] + ' '
    return '\n\t' + new_sentence[:-1].capitalize() + '.'


def fix_iz_to_is():
    """
    final function for text preparation
    :return:
    """
    result_str = normalize_text_in_var() + \
        create_new_sentence()
    return result_str.replace(" iz", " is")


def count_for_whitespaces():
    count_var = 0
    for j in ['\n', '\t', ' ']:
        var = str_var.count(j)
        count_var = count_var + var
    return count_var
