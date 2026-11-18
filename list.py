marks = []

for i in range(5):
    mark = int(input("Enter student mark: "))
    marks.append(mark)
   
print("All Student Marks:", marks)

mark = int(input("Enter student mark to add: "))
marks.append(mark)
print(marks) 


mark = int(input("Enter student mark to insert: "))
marks.insert(2,mark)
print(marks) 

remove_mark = int(input("Enter mark to remove: "))

if remove_mark in marks:
    marks.remove(remove_mark)
    print("After remove:", marks)
else:
    print("Mark not found")

print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

total = sum(marks) 
print("Total:",total)
avg = total/ len(marks)
print("Average:",avg)

print("Assending Order:", )

marks.sort()
print("Assending Order",marks)

count = 0
for mark in marks:
    if mark > 75:
        count += 1
print("Students scored above 75:", count)

print("Marks greater than or equal to 50:")
for mark in marks:
    if mark >= 50:
        print(mark)

   
