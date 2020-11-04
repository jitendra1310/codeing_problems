#!/usr/bin/python3.8

class Solution:
    
    """
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
    """
    def  moveElement(self, nums,target=0):
        """
        :type nums: List[int]
        :rtype: modify nums in-place instead.
        """
        count = 0
        for i in range(0,len(nums)):
            if nums[i] != target:                
                nums[count] = nums[i]
                count +=1
                
        for j in range(count,len(nums)):
            nums[j] = 0
        return nums
        
    def myApprochElementMoveToEnd(self,nums,target=0):
        A = []
        B = []
        #print(input)
        for i in range(0,len(nums)):
            if nums[i] != target:
                A.append(nums[i])
            else:
                B.append(nums[i])
        A.extend(B)
        nums.extend(A)
        print(A)
    def gfgApprochElementMoveToEnd(self,nums,target=0):
        A = []
        count = 0
        #print(input)
        for i in range(0,len(nums)):
            if nums[i] != target:
                A.append(nums[i])
                count +=1
        for j in range(count,len(nums)):
            A.append(target)
        return A    
    
objects = Solution()
input  = [0,1,0,0,0,0,0,0,0,0]
print(objects.gfgApprochElementMoveToEnd(input,0))
    
    