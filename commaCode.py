spam = ['Apples', 'bananas', 'tofu', 'cats']

stringOutput = ''

def commacode(someList):
    global stringOutput
    for i in range(len(someList)):
        stringOutput += someList[i] + ', '

    print(stringOutput)

commacode(spam)