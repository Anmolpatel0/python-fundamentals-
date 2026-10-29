
# Python Fundamentals Practice

print("Welcome to Python!")

# 1. Variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1}.")

# 2. Conditional statements
if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

# 3. Loops
for number in range(1, 6):
    print(number)

# 4. List
skills = ["HTML", "CSS", "Python"]
skills.append("Git")
print(skills)

# 5. Dictionary
student = {
    "name": name,
    "age": age,
    "skills": skills
}

print(student)
