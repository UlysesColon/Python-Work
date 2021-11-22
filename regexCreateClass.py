import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))


#in negative using ^

negVowelRegex = re.compile(r'[^aeiouAEIOU]')
print(negVowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))