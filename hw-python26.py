# Given a list of dictionaries create a list of tuples
# list1 = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
# Create a list of tuples
# tuple[('red', 'high'), ('yellow', 'low')]

list1 = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]

tuple_list = []
for d in list1:
    tuple_list.append((d['color'], d['value']))

print(tuple_list)