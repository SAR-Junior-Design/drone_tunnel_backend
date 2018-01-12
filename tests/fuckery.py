def decor(func):
     def wrapper(*args, **kwargs):
             print('args - ',args)
             print('kwargs - ',kwargs)

             return func(*args, **kwargs)
     return wrapper

def is_admin(func):
    def wrapper(username):
        if username == "admin":
            return func(username)
        else:
            return login_denied(username)
    return wrapper


@decor
def a(*a, **b):
     print("In a")
     print(a)
     print(b)

@is_admin
def login(username):
    print("login granted " + username)

def login_denied(username):
    print("denied")

#a(10,99, b=5)
#
# login("kaan")
# login("admin")

from functools import wraps




class person(object):

    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def is_alpha(func):
        def wrapper(self, *arg, **kw):
            #print('-- entering', func.__name__)
            #print('-- ', self.__dict__)
            if self.age > 10:
                func(self, *arg, **kw)
                #print('-- exiting', func.__name__)
                #print('-- ', self.__dict__)
                #return res
            else:
                self.too_shy(*arg, **kw)

        return wrapper



    @is_alpha
    def talk(self, words):
        print("Hi y'all, I'm " + self.name)

    def too_shy(self, words ):
        print("did not speak... ")



p1 = person("kaan", 50, "alpha")
p1.talk("yolo")

p2 = person("bob", 9, "beta")
p2.talk("yolo")