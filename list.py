size=int(input("enter the list size"))
li=[]
for i in range(size):
    values=int(input("enter the elements in list"))
    li.append(values)
print(li)
valuess=int(input("enter the number to add"))
li.append(valuess)
li[2]=22
print(li)
valodd=0
valeven=0
for nu in li:
    if nu %2==0:
        print("even no is present",nu)
    else:
        print("the number is odd",nu) 
print("even number count is",valeven)
print("even number count is",valodd)
