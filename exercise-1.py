def last_to_first(items):
    return items[-1:] + items[:-1]



if __name__ == '__main__':
    print("Example:")
    print(last_to_first([2, 3, 4, 1]))
    print(last_to_first([1, 2, 3, 4]))
    print(last_to_first([1, 2]))
    print(last_to_first([]))
