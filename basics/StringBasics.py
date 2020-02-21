
separator = "============================"
print ("String Basics")
print(separator)
print()
my_string = 'Test'
my_string1 = "Test"
my_string2 = "Vibhor\'s String test"

print (my_string)
print (my_string1)
print (my_string2)

hello = "Hello"
world = "World!"

print()
print (hello*5)
print (world*5)

print()
print((hello+world + " ")*5)

print()
print(len(hello))
print(len(world))
print()

first_element = hello[0]
print(first_element)
print(type(first_element))

print()
print("Partitioning in Strings")
print("We can pick out a substring, or partition a string in the following way")
my_new_string = "I love python. My love for java is decreasing"
print("By calling my_new_string[0:12], we get the first 12 characters of my_new_string")
print(my_new_string[0:13])

print()
print("Other examples of list partitioning")
print("Get the elements in string starting from the 15th element, till the end of the string")
print(my_new_string[15:])

print()
print("Get the elements in string starting from the 0th element, till the specified end index of the string")
print(my_new_string[:15])