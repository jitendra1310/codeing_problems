#!/usr/bin/python3.8

"""
Title: Two Number Sum
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

#https://www.youtube.com/watch?v=gCin6Qz-eJQ
class TwoNumberSum:
    """
    Approch: Bruteforce
    
    Algo:
    
    A = []
    target
    for i=0 : i<(len(A)-1)
      for j = i+1 : j<(len(A))
        if target == Sum(A[i]+A[j])
            return True
    
    return False    
    """  
    
    #Time complexity: O(n^2)
    #Space complexity: O(1)
    def approchBruteForce(self,inputArray,target):        
        for i in range(len(inputArray)-1):
            for j in range(i+1,len(inputArray)):
                if inputArray[i]+inputArray[j] == target:
                    print(inputArray[i]+inputArray[j])
                    return True
        return False
    
    """
    Hash Table
    """
    #Time complexity: O(n)
    #Space complexity: O(n)
    def approchHashTable(self,inputArray,target):
        ht = dict()
        for i in range(len(inputArray)):
            if inputArray[i] in ht:
                print(ht[inputArray[i]],inputArray[i])
                return True
            else:
                ht[target-inputArray[i]] = inputArray[i]
        return False
    """
    Approch 3:
    https://www.youtube.com/watch?v=s1xA_K1JReo
    Array Must be sorted Array
    """
    #Time complexity: O(n)
    #Space complexity: O(1)
    
    def approchTwoSum(self, inputArray, target):
        l = 0 #left index
        r = len(inputArray) -1 #Right index
        
        while l<=r:
            if inputArray[l]+inputArray[r] == target:
                print(inputArray[l],inputArray[r])
                return True
            elif inputArray[l]+inputArray[r] < target:
                l += 1
            elif inputArray[l]+inputArray[r] > target:
                r -=1 
        return False    
   


#calling
obj = TwoNumberSum()
print(obj.approchHashTable([2,7,11,15],9))
