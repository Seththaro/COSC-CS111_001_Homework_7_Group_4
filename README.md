# Homework_7_Group_4


#exercise 3
def remove_all_after(num_list, num_input):

    try:
        num_input = int(num_input)
    except ValueError:
        return "invalid input"

    if num_input not in num_list or num_input <= 0:
        return num_list

    else:
        num_input_indix = num_list.index(num_input)
        del num_list[num_input_indix+1:]
        return num_list
