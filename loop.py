print("Print Even Numbers")
for i in range(1,51):
  if i%2==0:
    print("Even Numbers:",i)

print("Skip Multiples of 3")
for i in range(1,31):
 if i % 3 !=0:
  print ("expect div by 3 :",i)

print("Stop at a Specific Number: ")
num = int(input("Enter a number: "))
i = 1
while i <= num:
    if i == 15:
        break
    print(i)
    i += 1

print("Positive and Negative Numbers:")
for i in range(10):
    n1 = int(input("Enter a number: "))
    if n1 == 0:
        print("Zero entered. Loop stopped!")
        break
    elif n1 > 0:
        print(n1, "is a Positive number")
    else:
        print(n1, "is a Negative number")
