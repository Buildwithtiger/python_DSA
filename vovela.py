stri=input("enter the string")
print(stri)
print(str)
vovel=0
sum=0
counti=0
for ch in stri:
  vovel+=len(ch)
if (ch=='a')or(ch=='e')or(ch=='i')or(ch=='o')or(ch=='u'):
    print("vowl is present")
    sum+=len(ch)
else:
   print("not present")
print(sum)
print("upercase")
print(stri.upper)
print("print lowercase")
print(stri.lower)
found=input("which word u have to find")
for chh in stri:
 if chh==found:
  print("word is founded")
  counti+=len(chh)
else:
   print("word is not founded")
print(counti)
compare=input("enter the comare dtring")
if compare==stri:
  print("both string are same")
else:
  print("string is not same")
spaces=input("enter spaces string")
print(spaces.replace(" ",""))
