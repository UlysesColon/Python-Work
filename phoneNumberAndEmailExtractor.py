 #! python3
 # phoneNumberAndEmailExtractor.py - finds phone and email on the clipboard


import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?           #Area Code
    (\s|-|\.)?                   #Separator
    (\d{3})                      #First 3 digits
    (\s|-|\.)                    #Separator
    (\d{4})                      #Last four Digits
    (\s*(ext|x|ext.)\s*\d{2,5})? #Extension
)''', re.VERBOSE)

# DONE: Create Email Regex 

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # username
    @                  # separator
    [a-zA-Z0-9.-]+     # domain name
    (\.[a-zA-Z]{2,4})  # dot-something  
)''', re.VERBOSE)

# DONE: Find Matches in the clipboard text

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    
    if groups[7] != '':
        phoneNum += ' x' + groups[7]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])



# TODO: Copy Results to the Clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clip board:')
    print('\n'.join(matches))
else:
    print('No phone numbers of emails found.')