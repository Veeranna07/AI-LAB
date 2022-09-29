# Create a list
L=[]
for i in range(1,6):
    el=int(input("enter elements :"))
    L.append(el)
print(L)

# Insert
p1=int(input("Enter position : "))
val1=int(input("Enter value at index : "))
L.insert(p1,val1)
print(L)

#Update
p2=int(input("Enter position : "))
val2=int(input("Enter value to be updated : "))
L[p2]=val2
print("After updating the list = ",L)

# Extend
L1=[100,200,300]
L.extend(L1)
print(L)

#Maximum Value
max(L)

#Minimum value
min(L)

#length of the list
len(L)

#slicing
l=int(input("Enter left side index : "))
r=int(input("Enter right side index : "))
print(L[l:r])

#Removing elements
List=[11,22,3,4,5,4,3,22,11,7]
print("After removing duplicate elements : ",list(set(List)))
