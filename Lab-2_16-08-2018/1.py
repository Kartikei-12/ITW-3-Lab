
# Temperatur conversion program
print("Hello World!")


def my_input(msg):
    while True:
        try:
            result = float(input(msg))
        except ValueError:
            print("Please enter a proper number.")
        else:    
            return result

print("Temperature in Fahrenheit is:", 
      (9/5)*my_input("Enter temperature in celcius:") + 32)
