newlist = [1,2,3,4,5,6,7,8,9]

def chunks(l, n):
        for nums in range(0, len(l), n):
                yield l[nums:nums + n]

# n = eval(input("Enter your desired chunk: "))
n = 3
x = list(chunks(newlist, n))

print(x)