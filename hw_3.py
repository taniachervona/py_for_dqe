str_var = """homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


# normalize text
sep_with_colon = str_var.split(sep=':')
sep_with_point = sep_with_colon[1].split(sep='.')
result_str = sep_with_colon[0].capitalize() + ':'
input_var = ''
for i in sep_with_point[:-1]:  # last element of list it is str included only whitespaces
    input_var = input_var + '\n\t' + f'{i}.'.lstrip().capitalize()
result_str = result_str + input_var

# new sentence from last words of exists sentences
new_sentence = ''
for i in sep_with_point[:-1]:  # last element of list it is whitespaces
    split_str = i.lstrip().split()
    new_sentence = new_sentence + split_str[-1] + ' '
new_sentence.capitalize()

# fix iz to is
fix_iz = result_str.replace(" iz", " is")

# calculation of whitespaces
count_var = 0
for j in ['\n', '\t', ' ']:
    var = str_var.count(j)
    count_var = count_var + var
