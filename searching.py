size=int(input("enter the array size"))
arr=[]
for i in range(size):
    values=int(input("enter the array element"))
    arr.append(values)
for j in arr:
    if(j==11):
     print("the no is present")
    else:
     print("the no is not present")
