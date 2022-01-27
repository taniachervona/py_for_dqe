import random


# create list of 100 random numbers from 0 to 1000
list_var = []  # add variable list type
for i in range(100):  # creating cycle for list_var
    list_var.append(random.randrange(1000))  # every iteration add new element to list


# sort list from min to max (without using sort())
list_new = []  # add new list for sorting
for j in range(len(list_var)):  # creating cycle for define min value in list
    list_new.append(min(list_var))  # add min value from old list to new one
    list_var.remove(min(list_var))  # delete first min value from old list


# calculate average for even and odd numbers
# print both average result in console
list_even = []  # add new list for even values from list_new
list_odd = []  # add new list for odd values from list_new
for el in list_new:  # creating cycle for all elements from list_new
    if el % 2 == 0:  # found even elements
        list_even.append(el)  # add even elements to even list
    else:
        list_odd.append(el)  # add others elements (odd) to odd list
even_avg = round(sum(list_even) / len(list_even), 2)  # found average for even numbers
odd_avg = round(sum(list_odd) / len(list_odd), 2)  # fount average for odd numbers
print(f'average for odd numbers from list: {odd_avg}')  # result visualization
print(f'average for even numbers from list: {even_avg}')  # result visualization

