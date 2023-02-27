# Given a list
# ["bar", "baz", "qux", "etc"]
# Create a tuple
# ("foo", "bar", "baz", "qux", "etc")

lt = ["bar", "baz", "qux", "etc"]
t = ("foo",) + tuple(lt)
print(t)
