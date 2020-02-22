separator = "============================"
print("Membership operators in python")
print(separator)
print()

print()
print("A membership operator in python, are boolean return operators stating weather something belongs to a "
      "particular data set or not")
print("List, Set, Tuple & Dictionary all support membership operators")

print()
print("Sample below for membership operator called on list_of_numbers.")
list_of_numbers = [7,3,9,2,1]
print(list_of_numbers, "Type of object = {}".format(type(list_of_numbers)))
print("is 3 present in {} : {}".format(list_of_numbers, 3 in list_of_numbers))
print("is 3 not present in {} : {}".format(list_of_numbers, 3 not in list_of_numbers))
print("is 5 present in {} : {}".format(list_of_numbers, 5 in list_of_numbers))
print("is 5 not present in {} : {}".format(list_of_numbers, 5 not in list_of_numbers))

print()
print("Sample below for membership operator called on dimensions.")
dimensions = 12,34,56,44
print(dimensions, "Type of object = {}".format(type(dimensions)))
print("is 12 present in {} : {}".format(dimensions, 12 in dimensions))
print("is 12 not present in {} : {}".format(dimensions, 12 not in dimensions))
print("is 7 present in {} : {}".format(dimensions, 7 in dimensions))
print("is 7 not present in {} : {}".format(dimensions, 7 not in dimensions))

print()
print("Sample below for membership operator called on number_set.")
number_set = set(list_of_numbers)
print(number_set, "Type of object = {}".format(type(number_set)))
print("is 3 present in {} : {}".format(number_set, 3 in number_set))
print("is 3 not present in {} : {}".format(number_set, 3 not in number_set))
print("is 5 present in {} : {}".format(number_set, 5 in number_set))
print("is 5 not present in {} : {}".format(number_set, 5 not in number_set))
