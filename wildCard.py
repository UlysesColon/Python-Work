import re

atRegex = re.compile(r'.at')
print(atRegex.findall('The Cat in the Hat sat on the Flat Mat.'))
