# raw code
def demo():
    print('This is a demo function')

demo()

d = demo

var = 1

def new_demo(arg):
    print(arg)
    arg()

new_demo(d)

# using decorator
def decor(func):
    def wrapper(*args, **dkwargs):
        print(args, ' ', dkwargs)
        if dkwargs['license'] == 'userlicense':
            return func(*args, **dkwargs)
        else:
            raise ModuleNotFoundError('Module not Found')
    return wrapper

@decor
def user1(*args, **dkwargs):
    print('User function called', args, dkwargs)


def outer_decor(license=None):
    def decor2(func):
        def wrapper2(*args, **dkwargs):
            if license == 'userlicense':
                return func(*args, **dkwargs)
            else:
                raise ModuleNotFoundError('Module not found')
        return wrapper2
    return decor2

# another form to declare the decorator 
@outer_decor(license='userlicense')
def user2(*args, **dkwargs):
    print('User 2 func called', args, dkwargs)

@outer_decor(license='developerlicense')
def user3(*args, **dkwargs):
    print('User 3 func called', args, dkwargs)


# using the decorator with class
# the funcion __call__ will be call when decorator is trigged
class Decor:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if kwargs['license'] == 'userlicense':
            return self.func(*args, **kwargs)
        else:
            raise ModuleNotFoundError('Module not found')

@Decor
def user4(*args, **dkwargs):
    print('User 4 function called', args, dkwargs)

class Decor2:

    def __init__(self, license=None):
        self.license = license

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.license == 'userlicense':
                return func(*args, **kwargs)
            else:
                raise ModuleNotFoundError('Module not found')
        return wrapper

@Decor2(license='userlicense')
def user5(*args, **dkwargs):
    print('User 5 function called', args, dkwargs)

@Decor2(license='developerlicense')
def user6(*args, **dkwargs):
    print('User 6 function called', args, dkwargs)

# main
if __name__ == '__main__':

    user1('test', license='userlicense')

    # raise an error cause the license is different of 'userlicense  promoved by decorator
    # user1(license='developerlicense')


    # Another way to represet decorator

    my_function = decor(user1)
    my_function(license='userlicense')

    # raise an error cause the license is different of 'userlicense  promoved by decorato
    # my_func2 = decor(user1)
    # my_func2 = my_func2(license='developerlicense')

    print('\n\n', my_function)

    print('\n\n')

    user2()

    # raise an error cause the license is different of 'userlicense  promoved by decorato
    # user3()

    print('\n\n')
    user4(license='userlicense')
    
    # raise an error cause the license is different of 'userlicense  promoved by decorato
    # user4(license='developerlicense')

    print('\n\n')
    user5()

    # raise an error cause the license is different of 'userlicense  promoved by decorato
    # user6()
