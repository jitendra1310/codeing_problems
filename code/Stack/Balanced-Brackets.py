"""
Check The Balanced Brackets
Youetube: https://www.youtube.com/watch?v=QZOLb0xHB_Q
"""
class balancedBrackets:
    
    def __init__(self):
        self.stack = []
    
    def checkExp(self,expression):
        expression = list(expression)
        res  = True
        for i in range(0,len(expression)):
            value = expression[i]
            if value in ['[','(','{']:
                self.stack.append(value)
            elif value in [')','}',']']:
                if value == ')' and self.stack[-1] == '(':
                    self.stack.pop()
                elif value == '}' and self.stack[-1] == '{':
                    self.stack.pop()
                elif value == ']' and self.stack[-1] == '[':
                    self.stack.pop() 
                else:
                    return False
        
        if(len(self.stack) >0):
            return False
        else:
            return True
       
obj = balancedBrackets()            
print(obj.checkExp('[()()]{'))