def check(tuple):
    return all(tuple)
tuple1 = (1, True, "Hello")
tuple2 = (0, False, "World")
print(check(tuple1))
print(check(tuple2))