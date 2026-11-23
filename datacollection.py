names = ["Arun", "Priya", "Kumar", "Divya", "Ravi"]
print("Student Names:", names)

names.append("Anu")
names.append("Vijay")
print("After adding:", names)

remove_name = input("Enter name to remove: ")

if remove_name in names:
    names.remove(remove_name)
    print("After removing:", names)
else:
    print("Name not found")

check_name = input("Enter name to check: ")

if check_name in names:
    print("Name is available")
else:
    print("Name is not available")

print("Total names:", len(names))

print("-------------------------------")

set1 = {7, 10, 18, 45, 99}
set2 = {10, 18, 25, 45, 50}
print("All unique numbers:", set1.union(set2))

print("Common numbers:", set1.intersection(set2))

print("Only first set:", set1.difference(set2))

set1.add(12)
print("After adding:", set1)

set1.remove(99)
print("After removing:", set1)

print("-------------------------------")
prices = (100, 250, 150, 300, 250)
print("First price:", prices[0])
print("Last price:", prices[-1])

print("Maximum price:", max(prices))
print("Minimum price:", min(prices))

print("Price count:", prices.count(250))

price_list = list(prices)
print("Converted list:", price_list)

price_list.append(500)
print("After adding:", price_list)

print("--------------------------")

employee = {
    "emp_id": 101,
    "name": "Swetha",
    "age": 22,
    "department": "IT"
}

print("Keys:", employee.keys())
print("Values:", employee.values())

employee["email"] = "swetha@gmail.com"
print("After adding email:", employee)

employee["age"] = 23
print("After updating age:", employee)

employee.pop("department")
print("After removing department:", employee)

if "name" in employee:
    print("Name key exists")
else:
    print("Name key does not exist")

print("-----------------------------")
grocery = {
    "Rice": 60,
    "Sugar": 45,
    "Oil": 150,
    "Milk": 30,
    "Bread": 40
}

print("Grocery Inventory:")

for name, price in grocery.items():
    print(name, "=", price)

grocery["Tea"] = 120
print("After adding:", grocery)

grocery["Rice"] = 65
print("After updating:", grocery)
