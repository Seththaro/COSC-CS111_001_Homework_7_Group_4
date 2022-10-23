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

    

if __name__ == '__main__':
    print(remove_all_after([1, 2, 3, 4, 5], 3))
    print(remove_all_after([1, 1, 2, 2, 3, 3], 2))
