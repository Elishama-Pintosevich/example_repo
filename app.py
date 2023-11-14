# print("hello world")
# int float String char
x = "dani"
# x = 1.7
# print(x)

my_list = [1,"chaim", 7.8]

my_dict = {"name":"dudi", "age":20}

dict_val = list(my_dict.values())
dict_key = list(my_dict.keys())

my_dict.pop('age')

my_dict['address'] = 'rishon'

# print(my_dict)
# print(my_dict['name'])
# x = 5.6
# y = int(x)
# print(y)

# print(my_dict)
# print(dict_val)
# print(dict_key)
# my_list.append(x)
# print(my_list)
# print(len(my_list))
# print(len(x))
# my_list.pop(0)
# print(my_list)
# my_list1 = [1,2,3]
# my_list2 = ['dudi','chaim','dani']

# text = 'my name "eli" '

# my_list3 = my_list1 + my_list2

# print(my_list3)
my_dict1 = {"name":"yosi", "age":20}
my_dict2 = {"adress": "petach tikva", "status":"single"}
my_dict3 = {**my_dict1, **my_dict2}
# my_dict4 = my_dict1 + my_dict2
# print(my_dict3)
# my_dict3 |= {"status":"married", "adress":"JLM"}
# print(my_dict3)

def add(x,y,z=0):
    return x+2, y+2, z+2 

def my_string(name):
    text = f"hello dear {name}, have a nice day!"
    return text, 5      

# print(my_string('dani'))
a = add(10,12)
# print(a)
# print(a.index(14))
# print(a)
name = 'elishama'
test = 'sha' in name
# print(test)
# print(f'a={a}, b={b}, c={c}')




# def dudi(some_func):
#     def dani():
#         print('top')
#         some_func()
#         print('bottom')
#     return dani()    
def dudi(some_func):
    print('top')
    return some_func()    

@dudi
def eli():
    print("hello world!")












