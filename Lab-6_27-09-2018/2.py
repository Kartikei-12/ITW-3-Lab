#Author: Kartikei Mittal
#ID: 2017KUCP1032
#Date: 27-Sept-2018
#Assignment

def even(a, b):
    if not a&2:
        a += 1
    return range(a, b, 2) 

def fibonnaci(till):
    a = 1
    b = 1
    ans = list()
    while b<till:
        ans.append(b)
        a,b = b,a+b
    return ans


X = set(even(1, 30))
Y = set(fibonnaci(30))

print("Set X:", X)
print("Set Y:", Y)
X.add(31)
print("X.add(31):", X)
X.update(set([33]))
print("X.remove(33):", X)
X.discard(31)
print("X.discard(31):", X)
print("len(X):", len(X))
print("X.union(Y):", X.union(Y))
print("X|Y:       ", X|Y)
print("X.intersection(Y):", X.intersection(Y))
print("X.difference(Y):", X.difference(Y))
print("X-Y:            ", X-Y)
print("X.symmetric_difference(Y):", X.symmetric_difference(Y))
Z = X.copy()
print("Z = X.copy():", Z)
print("max(X):", max(X))
print("min(X):", min(X))
print("sum(X):", sum(X))
print("all(X):", all(X))
print("any(X):", any(X))
X.pop()
print("X.pop():", X)
print("X.isdisjoint(Y)", X.isdisjoint(Y))
print("X.issubset(Y)", X.issubset(Y))
print("X.issuperset(Y)", X.issuperset(Y))
print("Y.isdisjoint(X)", Y.isdisjoint(X))
print("Y.issubset(X)", Y.issubset(X))
print("Y.issuperset(X)", Y.issuperset(X))

print()
