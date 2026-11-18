num1 = set()

for i in range(10):
    num = int(input("Enter a number: "))
    num1.add(num)
print("Unique Numbers:", num1)

num1.add(29)
print("After Adding:", num1)

num1.discard(13)
print("After Removing:", num1)

num1.remove(23)
print("After Removing:", num1)

print("Is 20 available?", 20 in num1)

num2 = {50, 20, 30, 70, 60}
print("Second Set:", num2)

print("Union:", num1.union(num2))

print("Intersection:", num1.intersection(num2))

print("Difference:", num1.difference(num2))

print("Total Unique Elements:", len(num2))
---------------------------------------------------------------------------------------------


student = {
    "student_id": 101,
    "name": "Swetha",
    "age": 21,
    "course": "Computer Science",
    "college": "Seethalakshmi Ramaswami College",
    "marks": 85
}


print("Student Details:", student)

print("Student Name:", student["name"])
print("Student Marks:", student["marks"])


student["skills"] = "Python, HTML, CSS, JavaScript"

print("After Adding Skills:", student)


student["marks"] = 90
print("Updated Marks:", student["marks"])


student.pop("age")
print("After Removing Age:", student)

print("Student Keys:", student.keys())

print("Student Values:", student.values())

print("Student Details:")
for key, value in student.items():
    print(key, ":", value)

if "course" in student:
    print("Course key exists")
else:
    print("Course key does not exist")
