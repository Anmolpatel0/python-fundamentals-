
import streamlit as st

st.set_page_config(
    page_title="Python Fundamentals Lab",
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 Python Fundamentals Lab")
st.write("Learn Python from basics with examples and practice.")
st.caption("Beginner-friendly • Interactive • Portfolio Project")

lessons = {
    "1. Variables and Data Types": '''
# Variables
name = "Anmol"
age = 20
height = 1.72
is_student = True

print(name)
print(age)
print(height)
print(is_student)

# Data types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
''',
    "2. Operators": '''
a = 12
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

print(a > b)
print(a == b)
print(a > 10 and b < 10)
''',
    "3. Input and Output": '''
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello,", name)
print("Next year your age will be", age + 1)
''',
    "4. Conditional Statements": '''
marks = int(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Needs improvement")
''',
    "5. Loops": '''
# For loop
for number in range(1, 6):
    print(number)

# While loop
count = 3

while count > 0:
    print("Countdown:", count)
    count -= 1

# Loop through a list
fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)
''',
    "6. Lists and Tuples": '''
# List: changeable
skills = ["HTML", "CSS", "Python"]
skills.append("Git")
skills[0] = "JavaScript"
print(skills)

# Tuple: not changeable
coordinates = (23.18, 79.98)
print(coordinates)
print(coordinates[0])
''',
    "7. Sets": '''
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)

numbers.add(5)
numbers.discard(2)

print(numbers)
''',
    "8. Dictionaries": '''
student = {
    "name": "Anmol",
    "course": "BCA",
    "year": 2027
}

print(student["name"])

student["city"] = "Jabalpur"

for key, value in student.items():
    print(key, ":", value)
''',
    "9. Functions": '''
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print("Sum:", add(10, 5))
print("Product:", multiply(10, 5))
''',
    "10. Error Handling": '''
try:
    number = int(input("Enter an integer: "))
    print("Your number:", number)

except ValueError:
    print("Please enter a valid integer.")
''',
    "11. Practice Problems": '''
# Even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Sum from 1 to n
n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Total:", total)

# Largest number
numbers = [12, 5, 28, 9]
print("Largest:", max(numbers))

# Count vowels
word = input("Enter a word: ").lower()
vowels = "aeiou"
count = sum(1 for letter in word if letter in vowels)

print("Vowels:", count)
'''
}

with st.sidebar:
    st.title("📚 Python Course")
    selected_lesson = st.radio(
        "Select a lesson",
        list(lessons.keys())
    )
    st.divider()
    st.write("**Course roadmap**")
    st.write("1. Learn")
    st.write("2. Understand code")
    st.write("3. Practise")
    st.write("4. Build projects")

st.subheader(selected_lesson)
st.code(lessons[selected_lesson], language="python")

st.divider()
st.header("🧮 Interactive Calculator")

col1, col2 = st.columns(2)

with col1:
    a = st.number_input("First number", value=10.0)

with col2:
    b = st.number_input("Second number", value=5.0)

operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if operation == "Addition":
    result = a + b
elif operation == "Subtraction":
    result = a - b
elif operation == "Multiplication":
    result = a * b
else:
    result = None if b == 0 else a / b

if result is None:
    st.error("Cannot divide by zero.")
else:
    st.metric("Result", result)

st.divider()
st.header("🎯 Practice: Even or Odd")

number = st.number_input(
    "Enter an integer",
    value=7,
    step=1,
    key="practice_number"
)

if st.button("Check Number"):
    if int(number) % 2 == 0:
        st.success(f"{int(number)} is even.")
    else:
        st.success(f"{int(number)} is odd.")

st.divider()
st.header("🖥️ Python Development Setup")

st.markdown("""
### VS Code
1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install [VS Code](https://code.visualstudio.com/).
3. Install the Python extension.
4. Create a file named `main.py`.

### Google Colab
1. Open [Google Colab](https://colab.research.google.com/).
2. Create a notebook.
3. Paste a Python example into a cell.
4. Press **Shift + Enter** to run it.

### Jupyter Notebook
Install and run:

```bash
pip install notebook
jupyter notebook
```

### PyCharm
You can also use [PyCharm](https://www.jetbrains.com/pycharm/).
""")

st.divider()
st.subheader("🚀 Publish your project")

st.markdown("""
1. Upload `app.py`, `requirements.txt`, and `README.md` to GitHub.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in using GitHub.
4. Select **Create app**.
5. Select your repository and set the main file to `app.py`.
6. Click **Deploy** to get your live app URL.
""")

st.caption("Python Fundamentals Lab | Built for learning and practice")
