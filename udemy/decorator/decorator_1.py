'''
Function return function 
'''

def hello(name='jose'):
    print('This is Hello() function')

    def greet():
        return "\t this the greet() function"
    
    def welcome():
        return "\t this is the welcome function"
    
    if(name=='jose'):
        return greet
    else:
        return welcome

'''
Use of the  function
'''

#my_func = hello('dfghj')
#print(my_func())

#########################################

def cool():

    def super_cool():
        return "I am super_cool"
    return super_cool

some_func = cool()

print(some_func())