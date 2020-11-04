#!/usr/bin/python3.8

class Solution:
    """
    """
    def fourSum(self, nums, target):
       nums.sort()
       combinations = []
       for i in range(0,len(nums)-3):
           for j in range(i+1,len(nums)-2):
               l = j+1
               r = len(nums)-1
               while l < r:
                   current_sum = nums[i]+nums[j]+nums[l]+nums[r]
                   if current_sum > target:
                       r -=1
                   elif current_sum < target:
                       l +=1
                   elif nums[i]+nums[j]+nums[l]+nums[r] == target:
                       if([nums[i],nums[j],nums[l],nums[r]] not in combinations):
                           combinations.append([nums[i],nums[j],nums[l],nums[r]])
                       r -=1
                       l +=1
                       break
                    
       return combinations
    
obj = Solution()
arr = [1,0,-1,0,-2,2]
#print(type(arr))
print(obj.fourSum(arr,0))
                                  
                  