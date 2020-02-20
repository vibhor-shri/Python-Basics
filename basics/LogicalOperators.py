
separator = "============================"
print("Logical Operators")
print(separator)

print("'and'" + " " + 'Evaluates if all provided statements are True')
print("'or'" + " " +  'Evaluates if at least one of many statements is True')
print("'not'" + " " +  'Flips the Bool Value')
print()

age = 66
is_toddler = age > 1 and age < 4
is_toddler_or_senior_citizen = age < 2 or age >= 60

print()
print("and operator")
print(is_toddler)

print()
print("or operator")
print(is_toddler_or_senior_citizen)

print()
print("not operator")
print(not 5 < 7)
print(not 7 < 5)

print()
print("Comparision Operations")
print(53>=52)
print(53>=53)
print(53>=55)
print(53<=52)
print(53<=53)
print(53<=54)
print(53==54)
print(53!=54)