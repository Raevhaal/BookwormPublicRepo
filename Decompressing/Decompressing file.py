#Adds the missing numbers at the start of each line in compressed txt
def missingnumbers(inputlist):
    lastnumber = 0
    for i in range(len(inputlist)-1):
        if(i > 0):
            if(inputlist[i][0].isdigit()):
                if(inputlist[i][1].isdigit()):
                    lastnumber = str(inputlist[i][0]) + str(inputlist[i][1])
                else:
                    lastnumber = inputlist[i][0]
            else:
                inputlist[i] = lastnumber + inputlist[i]
    return inputlist

def decompressor(inputlist):
    inputlist = missingnumbers(inputlist) #Ads missing numbers
    #Decompressing
    newlist = [inputlist[0]]
    for i in range(len(inputlist)-1):
        if(i > 0):
            if(inputlist[i][1].isdigit()):
                number = int(inputlist[i][0]+inputlist[i][1])
                newlist.append(newlist[i-1][0:number] + inputlist[i][2:])
            else:
                number = int(inputlist[i][0])
                newlist.append(newlist[i-1][0:number] + inputlist[i][1:])
    return newlist

def converttoprimesum(alphabetprime,inputlist):
    outputdict = {
        16: {},
        15: {},
        14: {},
        13: {},
        12: {},
        11: {},
        10: {},
        9: {},
        8: {},
        7: {},
        6: {},
        5: {},
        4: {},
        3: {},
    }
    for i in range(len(inputlist)):
        tmp = 1
        for i2 in inputlist[i]:
            tmp = tmp * int(alphabetprime.get(i2))
        outputdict[len(inputlist[i])][tmp] = inputlist[i]
    return outputdict

#End of functions

#Load the compressed text file
filename = "compressed.txt"
compressed = (open(str(filename),"r")).read()
compressed.replace("\t","")
compressed = compressed.split("\n")

#Decompresses the text file
decompressed = decompressor(compressed)

#Dictionary to convert letters to prime numbers
alphabettoprime = {'e': 2, 's': 3, 'i': 5, 'a': 7, 'r': 11, 'n': 13, 't': 17, 'o': 19, 'l': 23, 'c': 29, 'd': 31, 'u': 37, 'p': 41, 'm': 43, 'g': 47, 'h': 53, 'b': 59, 'y': 61, 'f': 67, 'v': 71, 'k': 73, 'w': 79, 'z': 83, 'x': 89, 'q': 97, 'j': 101}

primedict = converttoprimesum(alphabettoprime,decompressed)

"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    temp = 0
    for i2 in decompressed:
        temp = temp + i2.count(i)
    print(temp)
"""


f = open("primedict.py","w")
f.write("primedict = " + str(primedict))
f.close()





