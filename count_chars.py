def count_chars(st):
    dt = dict.fromkeys(st, 0)
    for char in st:
        if char in st:
            dt[char] += 1
    for key, value in dt.items():
        print('{} repeated {} times'.format(key, value))

count_chars('ababacdd')