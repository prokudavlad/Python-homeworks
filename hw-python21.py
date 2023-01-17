from collections import defaultdict
a = [10, 10, 23, 10, 123, 66, 78, 123]
counter = []
counter = defaultdict(int)
for elem in a:
    counter[elem] += 1
    doubles = {element: count for element, count in counter.items() if count > 1}
print(doubles)