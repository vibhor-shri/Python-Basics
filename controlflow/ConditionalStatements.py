separator = "============================"
print("Conditional Statements in python")
print("A conditional statement allows you to skip part(s) of your code, based on a specific condition")
print(separator)
print()

print("The 'if' statement is a condition statement, which returns a boolean attesting weather a particulat condition"
      " is true or false")
age = 66
if age >= 60:
    print("Senior Citizen")
else:
    print("Adult, non senior citizen")

print()
print("Using comparision operators in conditional statements: == and !=")
print("Example below uses conditional operator == to check if number is even or odd")
number = 9
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


print()
print("Example below uses conditional operator != to check if number is even or odd")
if number % 2 != 0:
    print("Odd number")
else:
    print("Even number")

print()
print("We can use 'if', 'elif', and 'else' to create a chaining of multiple conditions")
print("Example below uses if, elif, else to execute particular block of code based on which condition is true")

age = 23

if age < 3:
    print("Toddler")
elif 3 < age < 60:
    print("Adult")
else:
    print("Senior citizen")











