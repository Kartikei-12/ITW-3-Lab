
# Dictionary using two lists
print("Hello World!")

keys = list(range(1, 6))
values = ['a', 'b', 'c', 'd', 'e']

mydict = dict(zip(keys, values))

for i in mydict.keys():
    print("Key:", i, "Value:", mydict[i])
