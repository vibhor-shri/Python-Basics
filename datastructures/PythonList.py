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
list_of_string_data_type = ["a", "B", "c", "test", "anything in single or double quotes"]  # String type list
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
print("first item in float data type list = {}".format(list_of_float_data_type[0]))
length = len(list_of_float_data_type)
print("Length of the float data dype list = {}".format(length))
print("last item in float data type list = {}".format(list_of_float_data_type[length-1]))
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
weekdays = list_of_days[0:5]
weekends = list_of_days[5:7]
print()
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
print("if an item is requested from a list, which is beyond the capacity of the list, then an error is returned."
      " Un comment the below code to see the error")
# print(list_of_days[12])


