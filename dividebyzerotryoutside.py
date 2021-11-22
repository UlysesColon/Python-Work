def spam(dividedby):
    return 42 / dividedby
#function within the try
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid Argument')