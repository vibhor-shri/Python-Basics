separator = "============================"
print("List in python")
print("List in python is a collection of objects of either same or different data types")
print(separator)
print()

print("There are 2 ways to create a list in python:")
print("1. By putting [] brackets in an assignment statement; my_list = []")
print("2. By calling list constructor in an assignment statement; my_list = list()")

test_list = []
test_list_one = list()

print()
print("List of same data type, eg given below")

list_of_int_data_type = [3, 6, 8, 9, 1, 0]  # integer type list
list_of_float_data_type = [3.14, 6.34, 8.67, 9.56, 1.12, 0.34]  # float type list
list_of_string_data_type = ["a", "B", "c", "test", "anything in single or double quotes"]  # string type list
list_of_languages = ["C", "C++", "C#", "Java", "Python", "Perl", "Kotlin"]  # another string type list
list_of_bool_data_type = [True, False, False, True]  # boolean type list

print("This is an int data type list: {}".format(list_of_int_data_type))
# To print int data type list without formatting, un comment below code
# print(list_of_int_data_type)
print("This is an float data type list: {}".format(list_of_float_data_type))
# To print float data type list without formatting, un comment below code
# print(list_of_float_data_type)
print("This is an string data type list: {}".format(list_of_string_data_type))
# To print string data type list without formatting, un comment below code
# print(list_of_string_data_type)
print("This is an bool data type list: {}".format(list_of_bool_data_type))
# To print bool data type list without formatting, un comment below code
# print(list_of_bool_data_type)


print()
print("Lists are indexed from 0 up to n-1, n being the length the list")
print("first item in a list is at index 0, last item in a list is at index length of list -1")

print()
print("To access 1st item in a list, first_item = list_name[0]")
print("This is the first item in the int data type list: {}".format(list_of_int_data_type[0]))
print()
print("To access 2nd item in a list, second_item = list_name[1]")
print("This is the second item in the float data type list: {}".format(list_of_float_data_type[1]))
print()
print("To access nth item in a list, nth_item = list_name[n-1]")
print("This is the 5th item in the string data type list: {}".format
      (list_of_string_data_type[len(list_of_string_data_type) - 1]))
print()
print("To access last item in a list, last_item = list_name[-1]")
print("This is the last item in the bool data type list: {}".format(list_of_bool_data_type[-1]))
print()
print("To access second to last item in a list, second_last_item = list_name[-2]")
print("This is the second last item in the float data type list: {}".format(list_of_float_data_type[-2]))

print()
print("type() method helps us determine which type of object or data is the item of")

print()
list_of_multiple_data_type = ["A String", 12, 3.14, False]
print("This is a list of multiple data types: {}".format(list_of_multiple_data_type))

print()
print("Type of first element in the list = {}".format(type(list_of_multiple_data_type[0])))
print("Type of second element in the list = {}".format(type(list_of_multiple_data_type[1])))
print("Type of third element in the list = {}".format(type(list_of_multiple_data_type[2])))
print("Type of fourth element in the list = {}".format(type(list_of_multiple_data_type[3])))

print()
print("If we call type() on the list itself, we see that the result is different")
print("Type being called on list object =  {}".format(type(list_of_int_data_type)))
print("Type being called on another list object =  {}".format(type(list_of_multiple_data_type)))

print()
print("Partitioning in list")
print("List can be partitioned based on what we want from the list; eg below")
list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print()
print("list of days in a week = {}".format(list_of_days))
weekdays = list_of_days[0:5]
weekends = list_of_days[5:7]
print("Getting weekdays from the days list ----->  list_of_days[0:5] = {}".format(weekdays))
print("Getting weekends from the days list -----> list_of_days[5:7] = {}".format(weekends))
print("In the above example, notice how in [0:5], the start index, ie, 0 is inclusive and end index, ie, 5 is exclusive")

print()
weekends_alternate_way = list_of_days[5:len(list_of_days)]
print("Another way to get weekends from the days list -----> list_of_days[5:len(list_of_days)] = {}".
      format(weekends_alternate_way))

print()
print("Other examples of list partitioning")
list_from_start_index_n_index = list_of_days[3:]
print("This example return items in the list from a specified start index till the end of the list.")
print("The call is made by list_of_days[3:]. This gives a list of items starting from the 3rd index till the end")
print(list_from_start_index_n_index)

print()
list_from_end_index_to_start_index = list_of_days[:5]
print("This example return items in the list from a specified end index -1 till the start of the list.")
print("The call is made by list_of_days[:5]. This gives a list of items starting from the 0th index till the end index")
print(list_from_end_index_to_start_index)
print("Notice, in each of the above samples, the order of the items are maintained.")

print()
print("Changing/Updating/Reassigning values in a list")
print("We can change or update the value at a particular index in a list by simply re assigning a new item at "
      "a particular index. Call can be made like, list_name[index value] = 'new item'")
list_of_days[6] = 'Funday'
print("Updated list of days = {}".format(list_of_days))
print("The statement, list_of_days[6] = 'Funday' updated the value of the last item in the list")

print()
print("We can also append values to the end of the list by using the append method. Example below")
print("In our list_of_days, we can add another item 'made up day', by calling the append method like: "
      "list_of_days.append('made up day')")
list_of_days.append("made up day")
print(list_of_days)

print()
print("if an item is requested from a list, which is beyond the capacity of the list, then an error is returned."
      " Un comment the below code to see the error")
# print(list_of_days[12])

print()
print("Few other methods in list")

print()
print("pop() method: Called on the list object.It removes the given item in the list, and return it. If optional "
      "parameter [index] is not given, it pops the last item in the list")
print("Testing of list.pop(). Called on the list_of_days object")

print()
print("List before pop is called = {}".format(list_of_days))
item = list_of_days.pop()
print("Item that was removed from the list = {}".format(item))
print("List after pop is called = {}".format(list_of_days))

print()
print("List before pop is called = {}".format(list_of_days))
item2 = list_of_days.pop(6)
print("Item that was removed from the list, after calling pop(6) = {}".format(item2))
print("List after pop is called with index value as 6 = {}".format(list_of_days))

print()
print("If pop() is called with an invalid index, an error is returned. Uncomment below code to test: "
      "list_of_days.pop(22)")
# item3 = list_of_days.pop(22)

print()
print("The max() method in a list returns the item with the maximum value in the list, or the last item "
      "if the elements were sorted in ascending order")
print("The max item in the int data type list list_of_int_data_type is = {}".format(max(list_of_int_data_type)))

print()
print("The max value in an float type list is the item with the maximum value in the list, or the last item "
      "if the elements were sorted in ascending order")
print("The max item in the float data type list list_of_float_data_type is = {}".format(max(list_of_float_data_type)))

print()
print("The max value in a string type list is the value which appears in the last, if the list is sorted alphabetically")
print("The max item in the int data type list list_of_languages is = {}".format(max(list_of_languages)))

print()
print("Calling the max method in a list which has multiple data types, will result in error. Uncomment below line "
      "to see the error")
# max_item = max(list_of_multiple_data_type)

print()
print("The min() method in a list returns the item with the smallest value in the list, or the first item "
      "if the elements were sorted in ascending order")
print("The min item in the int data type list list_of_int_data_type is = {}".format(min(list_of_int_data_type)))

print()
print("The min value in an float type list is the item with the smallest value in the list, or the first item "
      "if the elements were sorted in ascending order")
print("The min item in the float data type list list_of_float_data_type is = {}".format(min(list_of_float_data_type)))

print()
print("The min value in a string type list is the value which appears in the first index, if the list is sorted alphabetically")
print("The min item in the string data type list list_of_languages is = {}".format(min(list_of_languages)))

print()
print("Calling the min method in a list which has multiple data types, will result in error. Uncomment below line "
      "to see the error")
# min_item = min(list_of_multiple_data_type)

print()
print("The sorted() is called, taking a parameter as a list object, and it returns a copy of a list in order"
      " from smallest to largest, leaving the original list unchanged.")
print("Original list = {}".format(list_of_int_data_type))
print("After calling sorted() method, list = {}".format(sorted(list_of_int_data_type)))

print()
print("The sorted() method can be called with an optional parameter, reverse=True, to return the same list in "
      "descending order")
print("Original list = {}".format(list_of_int_data_type))
print("After calling sorted() method with reverse=True, list = {}".format(sorted(list_of_int_data_type, reverse=True)))

print()
print("Note: That calling sorted either ways, would not change the original list. It return only a copy of the "
      "original list in sorted order, either ascending or descending")
print("Checking the original list after sorted() calls: {}".format(list_of_int_data_type))

print()
print("Calling sorted on a list which has different data types will result in an error. Uncomment below lines to check")
# print(sorted(list_of_multiple_data_type))

print()
print("len() method: Takes a parameter of list, and returns the size/length of the list")
print("The length of list_of_days = {}".format(len(list_of_days)))


