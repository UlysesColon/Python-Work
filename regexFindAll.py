import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())


phoneNumRegexF = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # Has no Groups!!!
print(phoneNumRegexF.findall('Cell: 415-555-9999 Work: 212-555-0000'))

phoneNumRegexG = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #Has Groups!!!
print(phoneNumRegexG.findall('Cell: 415-555-9999 Work: 212-555-0000'))