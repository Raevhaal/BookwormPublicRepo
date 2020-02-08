def addtodict(binaryinput,value):
    dictionary[len(binaryinput)].append(value)



inputstring = "uianrruoafsttfie"
#Takes the inputstring and makes a binarynumber with the same length
newname = int(("1"*len(inputstring)),2)
dictionary = {
    16:[],
    15:[],
    14:[],
    13:[],
    12:[],
    11:[],
    10:[],
    9:[],
    8:[],
    7:[],
    6:[], 
    5:[],
    4:[]
}
binarylist = []
    
for i in range(newname):
    if(bin(i).count("1") > 3):
        temp = bin(i)[2:]
        temp2 = ""
        for i in range(len(temp)):
            if(temp[i] == "1"):
                temp2 = temp2 + str(i)
        addtodict(temp,temp2)
        binarylist.append(temp)
    
    
print(newname)
print(bin(newname)[2:])

def checkthing(number):
    print("binary = %s\t mylist = %s;" % (binarylist[number],arraything[number]))

#save to file
f = open("dict.txt","w")
f.write( str(dictionary) )
f.close()

"""
for i in range(len(arraything)):
    print(bin(arraything[i])[2:])
"""
