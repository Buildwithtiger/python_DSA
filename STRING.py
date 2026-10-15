str=input("enter the string")
print(str)
print("the length of string is=",len(str))
print("reverse string")
revstr=""
for ch in str:
    revstr=ch+revstr
print(revstr)