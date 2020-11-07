#!/usr/bin/python3.98
import sys

class Sorting:
    def __init__(self,arr_list,n):
        self.arr_list = arr_list
        self.n = n
        self.selectctionSort()
        
    def selectctionSort(self):
        min_idx = 0
        for i in range(0,len(self.arr_list)):
            min_idx = i
            
            for j in range(i+1,len(self.arr_list)):                
                if self.arr_list[j] < self.arr_list[min_idx]: 
                    min_idx = j
            # Swaping 
            self.arr_list[i],self.arr_list[min_idx] = self.arr_list[min_idx],self.arr_list[i]
        print(list(self.arr_list))
        
A = [64, 25, 12, 22, 11]         
obj = Sorting(A,5)
                   