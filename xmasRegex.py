import re

xmasRegex = re.compile(r'\d+\s\w+')

print(xmasRegex.findall('12 Drummers, 11 Pipers, 10 Lords, 9 Ladies, 8 Maids, 7 Swans, 6 Geese, 5 Rings, 4 Birds, 3 Hens, 2 Doves, 1 Partrige'))

