#!/usr/bin/python3.8
"""


############## isSubsequence ###########
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
"""
class StingSubsequence:
    """
    https://www.youtube.com/watch?v=gZaIJtqk4HM
    get all the subsequence of the string 
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        if(s==""): return True        
        index = 0
        for i in range(len(t)-1):
            if s[index]==t[i]:
                index +=1
            if index == len(s)-1:
                return True
        return False
    
    """
    https://www.youtube.com/watch?v=gZaIJtqk4HM
    get all the subsequence of the string 
    """
    def getAllSubsequences(self,str1):
        
        #Basecase
        if (len(str1)==0): return [""]
        small = self.getAllSubsequences(str1[1:len(str1)])        
        result = [""]*(2*len(small))
        k = 0
        
        for i in range(len(small)):
            result[k] = small[i]
            k = k+1
        for i in range(len(small)):
            result[k] = str1[0]+small[i]
            k = k+1
        return result
    
        
#obj = StingSubsequence()
#print(obj.isSubsequence('acb','ahbgdc'))
#print(obj.getAllSubsequences('abcd'))        