from __future__ import print_function
from fileManagement import open_file_in_read_mode


sampleFile ="sample.txt"
openSampleFile=open_file_in_read_mode(sampleFile)

if(openSampleFile is not None): 
    Lines = openSampleFile.readlines()
 
    puzzleValue = 0
    leftValue = 0
    rightValue = 0
    fullValue = 0
    
    # Strips the newline character
    for line in Lines:
        leftValue = 0
        rightValue = 0
        lineValue = str(line.strip())
        lineLength = len(lineValue)
        

        for i in range(lineLength):
            #print(ord(lineValue[i]))
            if(ord(lineValue[i])>=48 and ord(lineValue[i])<=57 and rightValue==0):
                rightValue=lineValue[i]

            if(ord(lineValue[lineLength-i-1])>=48 and ord(lineValue[lineLength-i-1])<=57 and leftValue==0):
                leftValue=lineValue[lineLength-i-1]

        tmpValue=str(rightValue)+str(leftValue)
        fullValue=fullValue+int(tmpValue)
        print("rightValue :{},leftValue : {}, lineValue : {}, tmpValue : {}".format(rightValue,leftValue,lineValue,tmpValue))

    print("fullValue : {}".format(fullValue))
        
    # closing the opened file
    openSampleFile.close()
    print("file closed")