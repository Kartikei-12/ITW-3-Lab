
# Fibonacci series
print("Hello World!")

def my_input(msg):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print("Please enter a proper number.")
        else:    
            return result

n = my_input("Enter number of rows:")
num1 = 1
num2 = 1
for i in range(n):
    for _ in range(n-i-1):
        print(" ", end=' ')
    for _ in range(i+1):
        if num2 < 10:
            print(" ", end='')
        print(num2, " ", end='')
    num1, num2 = num2, num1+num2
    print("")
