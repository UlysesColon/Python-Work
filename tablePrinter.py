tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

tableToPrint = []

colWidths = [0] * len(tableData)



def printTable(table):
    widthToJustify = 0
    lineToPrint = ''
    
    for k in range(len(table)):
        longest = 0
        
        
        joined = ' '.join(table[k])
        joined = joined.split()
        tableToPrint.insert(k, joined)

        for v in tableToPrint[k]:
            if longest < len(v):
                longest = len(v) 
            colWidths[k] = longest
            # print(str(colWidths[k]) + " is col length")   
        if colWidths[k] > widthToJustify:
            widthToJustify = colWidths[k]
            print(widthToJustify)

    
    
    for n in range(len(tableToPrint) + 1):
        for i in tableToPrint:      
            toAddSpaces = 0
            buffer = 2
            
            if len(i[n]) < widthToJustify:
                toAddSpaces = abs(widthToJustify - len(i[n]))
            if len(i[n]) >= widthToJustify:
                toAddSpaces = 0 
                buffer = 1  

            lineToPrint += buffer * " " + i[n] + " " * toAddSpaces    

        print(lineToPrint.center(8).strip())
        lineToPrint = ''
        

            




printTable(tableData)

    
