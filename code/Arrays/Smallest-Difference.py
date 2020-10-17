#/usr/bin/python3.8
"""
Smallest Difference pair of values between two unsorted Arrays
Last Updated: 21-05-2018
Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.

Examples :

Input : A[] = {1, 3, 15, 11, 2}
        B[] = {23, 127, 235, 19, 8} 
Output : 3  
That is, the pair (11, 8) 

Input : A[] = {l0, 5, 40}
        B[] = {50, 90, 80} 
Output : 10
That is, the pair (40, 50)

"""

import sys
class Solution:
    #Time complexity: O(m log m + n log n)
    def smallest(self,A,B):
       A.sort()
       B.sort()
       a = 0
       b = 0
       result = sys.maxsize
       while a < len(A) and b < len(B):           
           if(abs(A[a] - B[b]) < result):
               result = abs(A[a] - B[b])
           
           if(A[a] < B[b]):
               a +=1
           else:
               b +=1 
       return result 
      
object = Solution()
A = [1, 2, 11, 7]
B = [4, 13, 19, 23, 127, 235]
print(object.smallest(A,B))