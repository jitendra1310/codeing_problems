import math
class Prime:
    
    def __init__(self):
        num = input("Enter a number: ")
        self.num = int(num)
    
    """ 
    Description: 
    Complexcity: O(N/2)
    """
            
    def method1(self):  
        print(math.floor(math.sqrt(self.num)))      
        for i in range(2,math.floor(math.sqrt(self.num))):
            if self.num % i ==0:
                return False
        
        return True
    
    """ 
    Description: 
    Complexcity: O(N)
    """
    def method2(self):
        i=2
        while (i <= self.num):
            if self.num % i ==0:
                return False 
        return True
        
        
obj =  Prime();
print(obj.method2())