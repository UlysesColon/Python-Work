myPets = ['Huey', 'Louis', 'Dewey']

print('Enter a pet Name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet')

