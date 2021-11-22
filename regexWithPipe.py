import re

heroRegex = re.compile(r'Batman|Tina Fey')

mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost its wheel')
print(mo.group())
print(mo.group(1))

batWoRegex = re.compile(r'Bat(wo)?man')
mo3 = batWoRegex.search('The Adventures of Batman')
print(mo3.group())

mo4 = batWoRegex.search('The Adventures of Batwoman')
print(mo4.group())