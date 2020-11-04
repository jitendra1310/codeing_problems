#!/usr/bin/python3.8


'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
class sorting:
    def __init__(self,n,arr_list):
        self.n = n
        self.arr_list = arr_list
        self.swap = 0

    def bubble_sort(self):
        for k in range(0,n-1):
            for i in range(0,n-k-1):
                if int(self.arr_list[i]) > int(self.arr_list[i+1]):
                    temp = self.arr_list[i]
                    self.arr_list[i] = self.arr_list[i+1]
                    self.arr_list[i+1] = temp
                    self.swap +=1
        

#n = int(input("Please Enter the list of the:"))
#arr = input("Please enter the list:")

n = 100
arr = "91 76 23 7 61 68 20 21 72 87 18 52 13 89 48 93 97 50 71 3 32 73 70 24 27 11 96 85 33 20 83 29 29 64 57 90 43 90 8 92 86 61 55 73 16 87 30 7 94 19 18 68 80 98 95 6 64 81 81 98 91 79 2 94 25 82 88 71 95 75 17  20 64 34 94 49 22 44 18 97 84 54 31 72 61 83 63 39 70 7 71 27 71 77 17 77 8 79 30 11"
arr = arr.split()  
obj = sorting(n,arr)
obj.bubble_sort()
print(obj.arr_list)
print(obj.swap)