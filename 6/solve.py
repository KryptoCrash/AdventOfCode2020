from functools import reduce

with open("input") as f:
    data = f.read()

print(reduce(lambda a, b: a + b, [len(reduce(lambda a, b: a & b, [set(y) for y in x.split('\n')])) for x in data.split("\n\n")]))