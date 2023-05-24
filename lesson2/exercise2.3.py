a = [1, 2, 3]
b = str(a)
c = bool(b)
print(id(a), id(b), id(c), sep='\n')
print()
d = bool([1, 2, 3])
e = bool([1, 2, 3])
print(id(d), id(e), sep='\n')