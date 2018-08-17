
# Symmetric matrix

def my_input(msg):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print("Please enter a proper number.")
        else:    
            return result

print("Hello World!")
x = my_input("Enter multiple:")
si = my_input("Enter size of matrix:")

for i in range(1, si+1):
    for j in range(i*x, (si+i)*x, x):
        if j<10:
            print("  ", end='')
        elif j<100:
            print(" ", end='')
        print(j, " ", end='')
    print("")