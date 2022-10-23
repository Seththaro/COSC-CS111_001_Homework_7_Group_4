def replace_first(items):
    return items[-1:] + items[:-1]



if __name__ == '__main__':
    print("Example:")
    print(replace_first([2, 3, 4, 1]))
    print(replace_first([1, 2, 3, 4]))
    print(replace_first([1, 2]))
    print(replace_first([]))
