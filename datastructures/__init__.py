ds = "Data Structure"
ordered = "Ordered"
unordered = "Unordered"
mutable = "mutable"
immutable = "immutable"
list_constructor = "[] or list()"
tuple_constructor = "() or tuple()"
set_constructor = "{} or ser()"
dictionary_constructor = "{key, value} or dict()"

data_structures = {}
data_structures["List"] = {ordered, mutable, list_constructor}
data_structures["Tuple"] = {ordered, immutable, tuple_constructor}
data_structures["Set"] = {unordered, mutable, set_constructor}
data_structures["Dictionary"] = {unordered, mutable, dictionary_constructor}
print(data_structures)