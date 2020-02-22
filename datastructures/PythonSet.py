separator = "============================"
print("Set in python")
print(separator)
print()

print("A set is a data structure which stores unique elements which are mutable and unordered")
print("A Set can be created by either {} or by calling the set constructor set()")

my_sample_set_with_all_unique_elements = {"Java", "Python", "Ruby", "Perl", "PHP"}
my_sample_set_with_all_repeating_elements = {"Java", "Python", "Ruby", "Perl", "PHP", "Java", "Python", "Ruby", "Perl"}

print()
print("Printing my_sample_set_with_all_unique_elements = {}".format(my_sample_set_with_all_unique_elements))
print("Printing my_sample_set_with_all_repeating_elements = {}".format(my_sample_set_with_all_repeating_elements))
print("As you can see in the above example, set would only contain unique elements and discard any repeating elements")

print()
print("To add items to a set, we call the add() method, with a parameter as the item to be added. The location of the "
      "item being inserted is unknown as set is not ordered")
print("Below is the sample call to check add() method")
set_of_fruits = {"Apple", "Orange", "Banana", "Kiwi"}
set_of_fruits.add("Pear")
print("After calling add('Pear') on set_of_fruits")
print(set_of_fruits)

print()
print("To remove an item from the set, we call the pop() method. But, since a set in unordered, there is no gurantee "
      "which item would be removed from the set. \nThe pop() method returns the item which is removed")
print("Below is the sample call to check pop() method")
print("Before calling pop() on set_of_fruits. {}".format(set_of_fruits))
popped_item = set_of_fruits.pop()
print("After calling pop() on set_of_fruits. {}".format(set_of_fruits))
print("Popped item = {}".format(popped_item))