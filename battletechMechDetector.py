import pyperclip, re

#Currently only designed for inner Sphere mechs designation


battlemechRegex = re.compile(r'''(
    (\w+\s\w+|\w+)          #Mech Name that can include spaces                           
    (\s\w{1,3})             #ShortName
    -                       #Dash
    [a-zA-Z0-9]{1,3}        #ModelNumber
    
    )''',re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in battlemechRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print('No Mechs found.')
    

