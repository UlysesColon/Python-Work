import re
robocop = re.compile(r'robocop',re.I)
print(robocop.search('Robocop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Why does your coding textbook talk about RobOcOp so much?').group())