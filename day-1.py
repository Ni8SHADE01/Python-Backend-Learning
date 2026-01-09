name = "Minhaaj"
age = 20
price = 99.99
is_active = True

for i in range(10):
    print(i + 1)


def multiply(a, b):
    return a * b


result = multiply(10, 5)
print(result)


students = [
    {"name": "A", "age": 21},
    {"name": "B", "age": 22},
    {"name": "C", "age": 20}
]

for student in students:
    print(student["name"])
