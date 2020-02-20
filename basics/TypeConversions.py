

separator = "============================"
print("Data Type")
print(separator)

type_int = 7
type_float = 3.2
type_string = "String"
type_string_representing_valid_no = "10"
type_boolean = True

print(type(type_int))
print(type(type_float))
print(type(type_string))
print(type(type_string_representing_valid_no))
print(type(type_boolean))

print()
print("Type Conversion")
print(separator)

int_to_float = float(type_int)
int_to_string = str(type_int)

print(int_to_float)
print(type(int_to_float))

print()
print(int_to_string)
print(type(int_to_string))

print()
float_to_int = int(type_float)
float_to_string = str(type_float)

print(float_to_int)
print(type(float_to_int))

print()
print(float_to_string)
print(type(float_to_string))

print()
string_to_int = int(type_string_representing_valid_no)
string_to_float = float(type_string_representing_valid_no)

# Below calls will result in exception as Invalid Literal
# string_to_int = int(type_string)
# string_to_float = float(type_string)

print(string_to_int)
print(type(string_to_int))

print()
print(string_to_float)
print(type(string_to_float))

print()
# Below call will result in exception: Can only concatenate string
# print(type_string + type_int + type_float + type_boolean)
print("Multiple type conversion with concatenation")
print(type_string + " " + str(type_int) + " " +  str(type_float) + " " +  str(type_boolean))
