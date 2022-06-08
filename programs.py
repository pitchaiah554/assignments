def factorial(num):
    fact = 1
    if num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            fact  = fact*i
        print("The factorial of", num,"is",fact)
# factorial(5)

def remove_duplicates(st):
    # result = '#'.join(['a','b','a'])
    result = ''.join([value for index, value in enumerate(st) if value not in st[0:index]])
    # print(st[0:5])
    print(result)

# remove_duplicates('abababadsaakk')


def count_chars(st):
    dt = dict.fromkeys(st, 0)
    for char in st:
        if char in st:
            dt[char] += 1
    # print(dt)
    for key, value in dt.items():
        print('{} repeated {} times'.format(key, value))

count_chars('ababacdd')


