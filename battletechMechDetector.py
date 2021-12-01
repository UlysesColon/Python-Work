import pyperclip, re

#Currently only designed for inner Sphere mechs designation


battlemechRegex = re.compile(r'''(
    (\w+\s\w+|\w+)          #Mech Name that can include spaces                           
    (\s\w{1,3})             #ShortName
    -                       #Dash
    [a-zA-Z0-9]{1,3}        #ModelNumber
    
    )''',re.VERBOSE)


#Regex for clan mechs
#Catching name, but missing 'Locust C' 'and Pirahna (Standard)'
clanmechRegex = re.compile(r'''
    (\w+)                   #Name
    (\s)                      #Space
    (\(\w+\)|\(\w+\s\w+\))  #Alternate name
    (\s)                      #Space
    (\w+)                  #Model Number
''',re.VERBOSE)


#regex to capture nonstandard mech names 'Locust C' 'and Pirahna (Standard)' for example

nonstandardRegex = re.compile(r'''
    (\w+)           #Name
    (\s)            #Space
    (\(\w+\)|[a-zA-Z]{1})    #C or Standard

''', re.VERBOSE)



text = str(pyperclip.paste())

matches = []
clanMatches = []
nonStandMatches = []

#Printing Inner Sphere mechs
for groups in battlemechRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print('No Mechs found.')

#Printing Clanmechs
for groups in clanmechRegex.findall(text):
    clanMech = ''.join([groups[0],groups[1],groups[2],groups[3],groups[4]])
    clanMatches.append(clanMech)

if len(matches) > 0:
    pyperclip.copy('\n'.join(clanMatches))
    print('\n'.join(clanMatches))
else:
    print('No Clan Mechs found.')

'''
#Printing Non Standards NEEDS MORE WORK
for groups in nonstandardRegex.findall(text):
    nonStandardMech = ''.join([groups[0],groups[1],groups[2]])
    nonStandMatches.append(nonStandardMech)

if len(matches) > 0:
    pyperclip.copy('\n'.join(nonStandMatches))
    print('\n'.join(nonStandMatches))
else:
    print('No Non Standard Mechs found.')
'''

