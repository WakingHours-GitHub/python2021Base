def ask(name="bobby"):
    print(name)

class Person:
    def __init__(self):
        print("bobby")


# 将函数这个对象赋给变量.
my_func = ask



ask("离谱")

print(type(Person)) # <class 'type'>
print(Person.__bases__) # (<class 'object'>,)


# 同理：
l = ['a']
print(type(l)) # <class 'list'>
print(type(list)) # <class 'type'>
print(type(type)) # <class 'type'>



