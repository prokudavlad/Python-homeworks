# Given a dictionary
# {1:'entry 1', 2:'entry 2', 3:'entry 3', 4:'entry 4'}
# Create a tuple of values for the first three elements of a dictionary

d = {1: 'entry 1', 2: 'entry 2', 3: 'entry 3', 4: 'entry 4'}
t = tuple(d.values())[0:3]
print(t)