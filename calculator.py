import keyboard
import sys
import threading 

def esc_listener():
    keyboard.wait("esc")
    print("\nbye (ESC)")
    sys.exit()

threading.Thread(target=esc_listener, daemon=True).start()    

print("welcome in the calculator")

number1 = int(input("pass the first number: "))
number2 = int(input("pass the second number: "))

operation = input("press one of the letter to choose the operation\na for addition\nb for substraction\nc for multiplication\nd for division: ")

while operation not in ["a", "b", "c", "d"]:
    operation = input("unknown operation, press one of the letter to choose the operation\na for addition\nb for substraction\nc for multiplication\nd for division: ")
    if operation == "a":
        print(number1 + number2)
    elif operation == "b":
        print(number1 - number2)
    elif operation == "c":
        print(number1 * number2)
    elif operation == "d":
        print(number1 / number2)
    else:
        print("unknown operation, try again")