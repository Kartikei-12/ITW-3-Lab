
# Stack implemented using list
import copy

print("Hello World!")

stack = list()

def my_input(msg):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print("Please enter a proper number.")
        else:    
            return result

def pushS(a, size):
    global stack
    if len(stack) >= size:
        print("Stack overflow")
        return
    stack.append(a)

def popS():
    if len(stack) <= 0:
        print("Stack underflow, exiting")
        return
    a = copy.deepcopy(stack[-1])
    del stack[-1]
    return a

size = my_input("Enter size of stack:")
for i in range(size):
    pushS(input("Enter element {}: ".format(i+1)), size)

while True:
    ch = my_input("\n\n1. To push element."+
                  "\n2. To pop element."+
                  "\n0. To exit"
                  "\nWhat would you like():")
    if ch == 1:
        pushS(input("Enter element to push: "), size)
    elif ch == 2:
        print("\n\nPopped element:", popS())
    elif ch==0:
        exit()
    else:
        print("\nInvalid input exiting")
        