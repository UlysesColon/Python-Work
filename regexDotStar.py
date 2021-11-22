import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
moG = greedyRegex.search('<To serve man> for dinner.>')
print(moG.group())