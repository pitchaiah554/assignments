def remove_duplicates(st):
    result = ''.join([value for index, value in enumerate(st) if value not in st[0:index]])
    print(result)

remove_duplicates('abababadsaakk')