from array import *

val=array('i',[])
n=int(input("Enter length of array"))

for i in range(n):
    x=int(input("Enter next value "))
    val.append(x)

for e in val:
    print(e)

sr=int(input("Enter search key: "))
k=0
for i in val:
    if i==sr:
        print(k)
        break
    k+=1
else:
    print("Not found")

print(val.index(sr))