
# Operation on List, Tuple, Dictioanary
print("Hello World!")

list1 = [1, 2, 'b', 3, 4, 'a', 1, 100, 87]
print("Original list:", list1)
print("list1[2]:", list1[2])
print("list1[2:]:", list1[2:])
print("list1[:2]:", list1[:2])
print("list1[2:6]", list1[2:6])
print("list1[-2]:", list1[-2])

tup1 = (100, 3, 4, 'a', 1, 87, 1, 2, 'b')
print("Original tuple:", list1)
print("tup1[2]:", tup1[2])
print("tup1[2:]:", tup1[2:])
print("tup1[:2]:", tup1[:2])
print("tup1[2:6]", tup1[2:6])
print("tup1[-2]:", tup1[-2])

print("\n\nDictioanary:")

dict1 = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
}

for i in dict1.keys():
    print("Key:", i, "Value:", dict1[i])