#!/usr/bin/python3.8

""""
Get minmum and maximum using stack
With O(1) time complexcity  

Link : https://www.youtube.com/watch?v=ufwPuyxkNVE
"""
 
class MinAndMaxStack:
    
    def __init__(self):
        self.main_stack = []
        self.max_stack = []
        self.min_stack = []
    
    def push(self,x):        
        self.main_stack.append(x)
        
        #Min value append to append to min_stack
        if not self.min_stack or x < self.min_stack[-1]:
            self.min_stack.append(x)
            
        #Max value append to append to max_stack    
        if not self.max_stack or x > self.max_stack[-1]:
            self.max_stack.append(x)
    
    def pop(self):
        if len(self.main_stack)>0 or self.main_stack:
            pop_element = self.main_stack.pop()
            
            if not self.min_stack or self.min_stack[-1] == pop_element:
               self.min_stack.pop()
            
            if not self.max_stack  or self.max_stack[-1] == pop_element:
               self.max_stack.pop() 
    
    def top(self):
        if not self.main_stack:
            return -1
        else:
            return self.main_stack[-1]
    """
    Get Minmum
    """  
    def getMin(self):
        if not self.min_stack:
            return -1
        else:
            return self.min_stack[-1]
    """
    Get Maximum
    """    
    def getMax(self):
        if not self.max_stack:
            return -1
        else:
            return self.max_stack[-1]   
       
    def __init__(self):
        self.main_stack = []
        self.max_stack = []
        self.min_stack = []
    
    def push(self,x):        
        self.main_stack.append(x)
        
        #Min value append to append to min_stack
        if not self.min_stack or x < self.min_stack[-1]:
            self.min_stack.append(x)
            
        #Max value append to append to max_stack    
        if not self.max_stack or x > self.max_stack[-1]:
            self.max_stack.append(x)
    
    def pop(self):
        if len(self.main_stack)>0 or self.main_stack:
            pop_element = self.main_stack.pop()
            
            if not self.min_stack or self.min_stack[-1] == pop_element:
               self.min_stack.pop()
            
            if not self.max_stack  or self.max_stack[-1] == pop_element:
               self.max_stack.pop() 
            return pop_element
        else:
            return -1;   
    
    def top(self):
        if not self.main_stack:
            return -1
        else:
            return self.main_stack[-1]
    """
    Get Minmum
    """  
    def getMin(self):
        if not self.min_stack:
            return -1
        else:
            return self.min_stack[-1]
    """
    Get Maximum
    """    
    def getMax(self):
        if not self.max_stack:
            return -1
        else:
            return self.max_stack[-1]   
    
objects = MinAndMaxStack()
objects.push(10)
objects.push(20)
objects.push(30)

print(objects.getMax())
objects.push(5)
#print(objects.getMin())
print(objects.top()) 
print(objects.pop())
print(objects.getMin())
