my_lst = [15,6,6,6,6,7,10,12,20,10,28,10]

dt = dict.fromkeys(my_lst,0)
for key in my_lst:
    if key in dt:
        dt[key] +=1
for key, value in dt.items():
    if value>1:
        print('key-' , key)
        print('value- ',value)
        print('------')