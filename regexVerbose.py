import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #Area Code
    (\s|-|\.)?          #Separator
    \d{3}               #First 3 digits
    (\s|-|\.)           #Separator
    \d{4}               #Last four Digits
    (\s*(ext|x|ext.)\s*\d{2,5})? #Extension
)''', re.VERBOSE)

print(phoneRegex.search('Hey my phone is 555-444-3333').group())
print(phoneRegex.search('Hey my phone is 555-444-3333 ext 6666').group())