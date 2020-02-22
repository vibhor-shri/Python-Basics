separator = "============================"
print("Tuple in python")
print(separator)
print()

print()
print("Tuples are immutable data structures, which are used to store closely related information. Items cannot be "
      "removed or added to a tuple after creation, and we cannot sort tuples in place")
print("Example below for coordinates: Which stores latitude and longitude")
coordinates = (28.7041, 77.1025)

print()
print("Coordinate type is = {} ".format(type(coordinates)))

print()
print("The parentheses are optional while creating a tuple")
pi = 3.14
radius = 5
height = 7
volume = pi, radius, height
print("Data structure defined by volume variable = {}".format(type(volume)))

print()
print("We can access items from a tuple similar to a list")
print("volume[0] would print 3.14")
print(volume[0])

