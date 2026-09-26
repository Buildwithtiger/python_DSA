size=int(input("enter the array size"))
arr=[]
for i in range(size):
    value=int(input("enter the array values"))
    arr.append(value)
print(arr)
arr[3]=22
print(arr)