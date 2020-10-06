#!/usr/bin/python3
#Validating User Input

from IPython.display import clear_output
clear_output()
def user_choice():
    choice = input("please enter a number between (1-10): ")
    return choice.isdigit()
    
print(ran_check(3,2,10))
print(vol(2))