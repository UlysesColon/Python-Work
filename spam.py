while True:
    spam = int(input('Tell me how much spam'))

    if spam == 1:
        print('hello')
    elif spam == 2:
        print('howdy')
    else:
        print('greetings!')
        break

# spam == 1: hello
# spam == 2: howdy
# spam else: Greetings! and break