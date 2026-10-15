name=input("enrter the STring")
revser=""
for ch in name:
    revser=ch+revser

print(revser)
if name==revser:
   print("the string is palindrome")
else:
    print("string is not palindrome")