from math_lib.math_ import lowest_common_multiple as lcm
import pyperclip

while True:
    try:
        in1 = int(input("What is the first number you would like to find the LCM of?"))
        in2 = int(input("What is the second number you would like to find the LCM of?"))
        break
    except ValueError:
        print("Not a number! Try again")
result = lcm(in1,in2)
print(result)
pyperclip.copy(result)




