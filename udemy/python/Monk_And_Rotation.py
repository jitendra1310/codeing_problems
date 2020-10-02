'''
Monk and Rotation

Take Rotation Step

'''
n =  int(input("Please Enter The Length Of Array:"))
print("Rotion move Must Be less than array Lenghth!!")
k =  0

while k <= 0 :
 k =  int(input("Please take the rotion move:"))
 if k>n:
     k = 0
z = list(range(1,n+1))
r = z[n-k:n+1:]+z[0:n-k:]

listtostr =",".join(map(str, r))
#print(z[::])
#print(z[0:n-k:])
#print(z[n-k:n+1:])
print(listtostr)



