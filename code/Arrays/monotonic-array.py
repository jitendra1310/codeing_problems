#!/usr/bin/python3.8
class Solution(object):
    def isMonotonic_MyApproch(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        order = ""
        for i in range(0,len(A)-1):
            
            if(order==""):
                if(A[i] > A[i+1]):
                    order = 'desc'
                elif (A[i] < A[i+1]):
                    order = 'asc'
            elif(order == 'asc'  and A[i] > A[i+1]):
                return False
            elif(order == 'desc' and A[i] < A[i+1]):
                return False
        return True
    
    def isMonotonic_leetcode(self, A):
        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in range(len(A) - 1)))