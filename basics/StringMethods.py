separator = "============================"
print ("String Methods")
print(separator)

my_name = "vibhor shrivastava"
print(my_name)
test_string1 = "one test, two test, 3 test, n test, we all have test"
test_string2 = "one jsontester, two tester, 3 tester, n testers, we all hate testers"
test_string3 = " "
test_string_digit = "10"
test_string_digit1 = "10 abcd"

"""This is the title method of String. It will return title case of every word in string as a string"""
my_name_title = my_name.title()
print("after calling title() method ")
print(my_name_title)

"""This is the islower() method of String. It will return true if all the characters in the string are in lower case,
false otherwise"""
is_lower_case = my_name.islower()
print()
print("after calling islower() method ")
print(is_lower_case)

"""This is the isupper() method of String. It will return true if all the characters in the string are in upper case, 
false otherwise """
is_upper_case = my_name.isupper()
print()
print("after calling isupper() method ")
print(is_upper_case)

"""This is the isdigit() method of String. It will return true if all the characters in the string are digits,
and atleast one character is present, false otherwise"""
is_digit_one = my_name.isdigit()
is_digit_two = test_string_digit.isdigit()
is_digit_three = test_string_digit1.isdigit()
print()
print("after calling isdigit() method ")
print(is_digit_one)
print(is_digit_two)
print(is_digit_three)

"""This is the isspace() method of String. It will return true if all the characters in the string are whitespace 
characters, false otherwise """
is_space_one = my_name.isspace()
is_space_two = test_string3.isspace()
print()
print("after calling isspace() method ")
print(is_space_one)
print(is_space_two)

"""This is the count method. It returns the no. of occurrence of a substring, in the given string , as an integer. 
It takes an argument, ie, the item to be found. It also takes 2 optional arguments, start and end, to specify start and 
end index of the given string as the sample space to search"""
test_count = test_string1.count("test")
test_count2 = test_string2.count("test")
print()
print("after calling count() method ")
print(test_count)
print("Notice how count() method only focuses on substring, and not the exact match of words")
print(test_count2)

"""This is the capitalise() method of String. It will capitalise the first characters in string,
and return the result as a string"""
test_capitalise = my_name.capitalize()
print()
print("after calling capitalize() method ")
print(test_capitalise)

"""This is the replace() method of String. It will return a copy of the string,
 which replaces old substring with new substring"""
replace_one = test_string1.replace("test","replacedString")
print()
print("before calling replace() method ")
print(test_string1)
print("after calling replace() method ")
print(replace_one)

"""This is the rfind() method of String. It will return the highest index in the string where the substring
in parameters is found, -1 otherwise"""
rfind_one = test_string1.rfind("test")
rfind_two = test_string1.rfind("english")
print()
print("after calling rfind() method ")
print(rfind_one)
print(rfind_two)

"""This is the rindex() method of String. Similar to the rfind() method, only difference being it will return
ValueError if substring in parameters is not found"""
rindex_one = test_string1.rindex("test")
# rindex_two = test_string1.rindex("english") # Uncomment this line to see the ValueError
print()
print("after calling rindex() method ")
print(rindex_one)

print()
print("Learn more about every String method in python @ " +
      "https://docs.python.org/3.8/library/stdtypes.html#string-methods")
