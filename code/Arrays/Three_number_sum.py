#!/usr/bin/python3.8


class ThreeNumberSum:
    
    def Bruteforce(self,inputArray,target)-> bool:
        
        for i in range(len(inputArray)-2):
                        
            for j in range(i+1,len(inputArray)-1):
                                
                for k in range(j+1,len(inputArray)):
                    
                    if inputArray[i]+inputArray[j]+inputArray[k] == target:
                        return True
        return False
                
    def HashingBasedSum(self,inputArray,target) ->bool:
        for i in range(len(inputArray)-1):
            s = set()
            curr_sum = target - inputArray[i]
            
            for j in range(i+1,len(inputArray)):
                if(curr_sum-inputArray[j]) in s:
                    return True
                else:
                    s.add(inputArray[j])
                
        return False
                    
    def MyApprochSum(self,inputArray,target)-> bool:
        for i in range(len(inputArray)-2):
            if(target - (inputArray[i]+inputArray[i+1])) in inputArray[i+1+1:]:
                return True
        return False
    
obj = ThreeNumberSum()
print(obj.Bruteforce([12, 3, 4, 1, 6, 9],24))