import sys

def collatz(number):
    
    try:
        #if number is even print number // 2 and return value
        if number % 2 == 0:
            return number // 2 
        else:
            return 3 * number + 1
        #if number is odd the print and return 3 * number + 1
    except TypeError:
        print('please input a number')
        sys.exit()

userInt = int(input("please give me a number: "))

while True:
    
    output = collatz(userInt)
    
    if output == 1:
        print('got to one!')
        break
    else:
        print(str(output) + ' is the current output')
        userInt = output