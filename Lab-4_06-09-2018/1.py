#Author: Kartikei Mittal
#ID: 2017KUCP1032
#Date: 06-09-2018
#

from my_module import *
abc()



def my_input(msg):
    while True:
        try:
            result = int(input(msg))
            raise DummyException
        except ValueError as V:
            print("Please enter a proper number.", V)
        except Exception as e:
            print(e, "\nWell this was not supposed to happen.")
            return 0
        except DummyException:
            print("Dummy Exception")
            return 0
        else:
            return result

print(my_input("Please: "))

