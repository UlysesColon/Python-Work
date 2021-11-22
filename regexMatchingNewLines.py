import re

noNewLineRegex = re.compile('.*')
print(noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the Law.').group())

newLineRegex = re.compile('.*', re.DOTALL)
print(newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the Law.').group())