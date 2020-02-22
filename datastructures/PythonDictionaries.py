separator = "============================"
print("Dictionaries in python")
print(separator)
print()

print("Dictionaries are data sets which can contain 2 items, ie, key and value. \nThe key is unique in a dictionary "
      "and can be of any immutable data type. \nEach key in a dictionary would correspond to a value, the value again "
      "can be of any data type, or be another data structure altogether")

print()
print("The dictionary can be declared in a similar way as sets, the difference being if you are not creating a "
      "dictionary via a constructor, the you have to put item in pairs inside the {} braces")
print("The 2 ways in which a dictionary can be created are: dict_name = {'key':'value'} or by calling the dict() method ")

print()
dict_of_alphabets = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
print(dict_of_alphabets)
print("dict_of_alphabets is which type of dataset?  = {}".format(type(dict_of_alphabets)))

print()
print("To add items to a dictionary, we can use dict_name[key] = value")
print("Adding E to the dict_of_alphabets dictionary")
print("Dictionary before adding E = {}".format(dict_of_alphabets))
dict_of_alphabets["E"] = 5
print("Dictionary after adding E = {}".format(dict_of_alphabets))

print()
print("To get an items from a dictionary, we can use dict_name[key] to get the value of the item corresponding "
      "to the given key")
print("Getting item with key 'B' from the dictionary = {}".format(dict_of_alphabets["B"]))

print()
print("Trying to get a key which is not present in the dictionary, would result in an exception: KeyError")
print("Uncomment below line to see the error")
#print("Getting item with key 'Z' from the dictionary = {}".format(dict_of_alphabets["Z"]))

print()
print("To prevent the above error, we can check if a key is present in the dictionary or not, using the 'in' operator")
print("Checking if Z exists as a key in dict_of_alphabets: {}".format('Z' in dict_of_alphabets))
print("Checking if C exists as a key in dict_of_alphabets: {}".format('C' in dict_of_alphabets))

print()
print("Alternately we can check if a key, does not exist in dictionary by using 'not in' operator")
print("Checking if Z does not exist as a key in dict_of_alphabets: {}".format('Z' not in dict_of_alphabets))
print("Checking if C does not exist as a key in dict_of_alphabets: {}".format('C' not in dict_of_alphabets))

print()
print("A better way to lookup for keys and their corresponding values is by the get() method. This method takes in "
      "a parameter, ie, key, and returns the value if key is present in the dictionary, 'None' otherwise")
print("Using the get() method to get values from a dictionary")
print("get('D') called on dict_of_alphabets returns {}".format(dict_of_alphabets.get("D")))
print("get('Z') called on dict_of_alphabets returns {}".format(dict_of_alphabets.get("Z")))

print()
print("Identity operators in Dictionaries")
print("We can check if key returned 'None' using the 'is' operator. Alternately, we can also check if key is not "
      "'None' using the 'is not' operator")
item = dict_of_alphabets.get("Z")
print("Checking if item is None or not: {}".format(item is None))
print("Checking if item is not None: {}".format(item is not None))

print()
print("We can also use the get() method of the dictionary, with an optional parameter, which would be returned in case "
      "a lookup failed, or no key exists in the dictionary")
print("Calling get('Z', 'No value exists with key 'Z' in dict_of_alphabets)")
print(dict_of_alphabets.get("Z", "No value exists with key 'Z' in dict_of_alphabets"))

print()
print("How identity operators differ from equality operators is shown below")
print(" == or != Vs 'is' and 'is not'")
list_a = [1,2,3]
b = list_a
c = [1,2,3]

print(list_a == b)
print(list_a is b)
print(list_a == c)
print(list_a is c)


print()
print("Compound dictionary")
print("A compound dictionary, is a dictionary of dictionary. It is the same as described above, just that in a "
      "coumpound dictionary, the value of a particular key will again be a dictionary")

alphabets = {"A" : {"A": 1, "a": 1}, "B" : {"B" : 2, "b": 2}, "C" : {"C" : 3, "c": 3}}
print(alphabets["A"])
print(type(alphabets["A"]))