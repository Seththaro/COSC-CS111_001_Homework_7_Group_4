def chunks(l, n):
    for nums in range(0, len(l), n):
        yield l[nums:nums + n]



if __name__ == '__main__':
    print(list(chunks([5, 4, 7, 3, 4, 5, 4], 3)))
    print(list(chunks([3, 4, 5], 1)))
