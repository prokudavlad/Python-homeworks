# Create a dictionary with at least 5 natural elements.
new_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
# Swap the first and last element of the object.
first_key = list(new_dict.keys())[0]
last_key = list(new_dict.keys())[-1]
first_value = new_dict[first_key]
last_value = new_dict[last_key]
new_dict[first_key] = last_value
new_dict[last_key] = first_value

del new_dict[list(new_dict.keys())[1]]  # Remove the second element.
new_dict["new_key"] = "new_value"   # Add the key 'new_key' to the end with the value 'new_value'
print(new_dict)