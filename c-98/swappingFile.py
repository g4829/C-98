def swappingTheFiles():
    fileName=input("Enter the File Name")
    numberOfWords=0
    file=open(fileName,'w')
    for line in file:
        words=line.split()
        numberOfWords+=len(words)
    print("Number Of Words")
    print(numberOfWords)

swappingTheFiles()