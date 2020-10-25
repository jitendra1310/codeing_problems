#!/usr/bin/python3.8
import math 
class solution:
    
    def __init__(self):
        self.buffer_egge = 3      
        self.list1 = [79,82,42,44,43,55,62,87,85,88,89,81]
        self.list2 = [81,77,45,41,39,48,71,78,81,84,82,72]
        self.today_order_list = [77,53,33,32,49,53,68,71]        
        self.egg_order()        
    
    def  egg_order(self):        
        for i in range(8,len(self.list1)):
            self.today_order_list.append(math.ceil((self.list1[i]+self.list2[i])/2)+self.buffer_egge)
         
        
object = solution()
print(f"Total Order:{sum(object.today_order_list)}")
print("Order List:",object.today_order_list)
        