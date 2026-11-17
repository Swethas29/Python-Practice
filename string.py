fname=input("Enter your first name: ")
lname=input("Enter your last name: ")
fullname=fname + lname
print("Fullname: ",fullname)
print("UpperCase: ",fullname.upper())
print("LowerCase: ",fullname.lower())
print("Length of the string: " ,(len(fullname)))

for i in fullname:
  print(i)

print("Characters without spaces:")
for i in fullname:
    if i == " ":
        continue
    print(i)


if fullname[0].lower() == "s":
    print("Name starts with S",fullname)
else:
    print("Name does not start with S")

print("First 3 characters:", fullname[:3])
print("Last 3 characters:", fullname[-3:])
