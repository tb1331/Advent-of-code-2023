test_string = "abcone2threexyz"
fina_list = []

num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}










for word in data:
    #add
    add_space = [' '.join(i) for i in word]
    #kepp numb
    keep_num = [(s) for s in add_space if s.isdigit()]
    my_list = keep_num
    miss = my_list[0]
    if len(my_list) == 1:
        my_list.insert(-1,miss)
    #merge
    new_list = "".join(my_list)
    first_digit = (str(new_list)[0])
    last_digit = str(new_list[-1])
    new_digit = first_digit +last_digit
    final_list.append(new_digit)

real_list = [int(x) for x in final_list]
list_sum = sum(real_list)
print(final_list)
print(list_sum)