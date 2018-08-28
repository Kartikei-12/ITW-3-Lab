
# Queue implemented using list

print("Hello World!")

queue = list()

def my_input(msg):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print("Please enter a proper number.")
        else:    
            return result

def pushQ(a):
    queue.append(a)

def pullQ():
    if len(queue) <= 0:
        print("queue underflow, exiting")
        exit()
    a = queue[0]
    del queue[0]
    return a

size = my_input("Enter size of queue:")
for i in range(1, size):
    pushQ(input("Enter element {}: ".format(i)))

while True:
    ch = my_input("\n\n1. To push element."+
                  "\n2. To pull element."+
                  "\n3. To view queue"+
                  "\n0. To exit"+
                  "\nWhat would you like:")
    if ch == 1:
        pushQ(input("Enter element to push: "))
    elif ch == 2:
        print("\n\nPulled element:", pullQ())
    elif ch == 3:
        print(queue)
    elif ch==0:
        exit()
    else:
        print("\nInvalid input exiting")
        exit()