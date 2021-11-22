birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a Name: (blank to quit)')
    name = input()
    if name == '':
        for k,v in birthdays.items():
            print('Name: ' + k + ' Birthday: ' + v)    
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday Updated.')

    
