catNames=[]
while True:
    print('Enter a name of a cat ' + str(len(catNames) + 1) + '(or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('the cats names are:')
for name in catNames:
    print(' ' + name)