#!/usr/bin/python3
#Methods and Functions Homework Overview

def vol(r):
    return (4/3)*(3.14)*r**3;

def ran_bool(num,low,high):
    return num in range(low,high+1)

def ran_check(num,low,high):
    if num in range(low,high+1):
        return str(num) + " is in range betwwen "+ str(low) + " and "+ str(high)
    else:
        return str(num) + " is not in range betwwen "+ str(low) + " and "+ str(high)


def up_low(strin1):
    
print(ran_check(3,2,10))
print(vol(2))