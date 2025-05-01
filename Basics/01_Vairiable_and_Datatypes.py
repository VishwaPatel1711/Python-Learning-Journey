#Q1
name="Patel vishwa"
age=int(19)
marks_in_last_exam=float(7.82)
love_Python=bool(True)
print("Name:",name)
print("Age:",age)
print("Marks in last exam:",marks_in_last_exam)
print("Love Python?",love_Python)

#Q2 Swap the values of two variables a and b without using a third variable.
a=10
b=20
print("Before swapping: a =", a, ", b =", b)
a, b = b, a  # Swapping using tuple unpacking
print("After swapping: a =", a, ", b =", b)

#Q3 Take a string variable city="Mumbai" Now print the first and last character of the string.
city="Mumbai"
print("First character:", city[0])
print("Last character:", city[-1])

#Q4 name= "Vishwa" age = 19 print this in one line 
name="Vishwa"
age=19
print(" I am ",name,"and I am ",age," years old.")

#Q5 Take a string variable name="Vishwa" Now print the string in reverse order.
name="Vishwa"
print("Reversed string:", name[::-1])

#Q6 Datatypes in Python
name="Vishwa"
age=19
height=5.4
is_student=True
print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
print(type(height))  # <class 'float'>
print(type(is_student))  # <class 'bool'>