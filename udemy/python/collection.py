from collections import Counter,defaultdict
mylist = [1,1,1,1,2,2,2,2,23,3,3,3,3,3,4,4,4,4]

mylist = Counter(mylist)

#print(mylist)

mylist_1 = [1,1,1,1,'a','a','a']

print(Counter(mylist_1))