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


def create_final_dict_with_initial_order():
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


def create_final_dict_without_ordering():
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


def normalize_sentence_including_first_separator(sentence: str):
    if sentence.startswith("\t") is True \
            or sentence.startswith("\n") is True:
        item = '\n\t' + f'{sentence}.'.lstrip().capitalize()
    else:
        item = ' ' + f'{sentence}.'.lstrip().capitalize()
    return item


def split_string_with_colon(string_var: str):
    return string_var.split(sep=':')


def normalize_text(full_text: str):
    input_var = split_string_with_colon(
        full_text)[0].capitalize() + ':'
    sep_with_point = split_string_with_colon(
        full_text)[1].split(sep='.')
    for i in sep_with_point[:-1]:
        input_var = input_var + \
                    normalize_sentence_including_first_separator(i)
    return input_var


print("\nnormalize_text() function result:")
print(normalize_text(str_var))


def choose_last_word_in_str(str_line: str):
    split_str = str_line.lstrip().split()
    return split_str[-1]


def create_new_sentence(var: str):
    new_sentence = ''
    for i in split_string_with_colon(var)[1].split(sep='.')[:-1]:
        new_sentence = new_sentence + \
                       choose_last_word_in_str(i) + ' '
    return '\t' + new_sentence[:-1].capitalize() + '.'


print("\ncreate_new_sentence() function result:")
print(create_new_sentence(str_var))


def fix_iz_to_is(text_var: str):
    """
    final function for text preparation
    :return:
    """
    result_str = normalize_text(text_var) + "\n" + \
        create_new_sentence(text_var)
    return result_str.replace(" iz", " is")


print("\nFINAL RESULT: ")
print(fix_iz_to_is(str_var))


def count_for_whitespaces(text_all: str):
    count_var = 0
    for j in ['\n', '\t', ' ']:
        var = text_all.count(j)
        count_var = count_var + var
    return count_var


print("\ncount_for_whitespaces() function result:")
print(count_for_whitespaces(str_var))
