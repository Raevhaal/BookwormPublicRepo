from PIL import Image, ImageFilter, ImageOps, ImageEnhance, ImageGrab, ImageDraw
#from pytesseract import image_to_string
import pytesseract
from primedict import primedict
import time
import keyboard
import os

errors = 0

def bookwormcheater():
    #Clears terminal
    os.system('cls')
    try:
        def findwords(characters):
            def calculateprimedict(inputstring):
                tmp = 1
                for i2 in inputstring:
                        tmp = tmp * int(alphabettoprime.get(i2))
                return tmp
            
            charlen = int(("1"*len(characters)), 2)
            words = []
            print("Started finding words..")
            for i in range(charlen, 0, -1):
                if(bin(i).count("1") > 3):  # Change back to 3
                    temp = str(bin(i)[2:])
                    temp = ("0"*(len(characters)-len(temp))) + temp
                    temp2 = ""
                    
                    for i2 in range(len(temp)):
                        if(temp[i2] == "1"):
                            temp2 = temp2 + characters[i2]
                    convertedtoprime = calculateprimedict(temp2)
                    # Could be converted to one action maybe with mydictget faster by a couple ms
                    try:
                        if(convertedtoprime in primedict[len(temp2)]):
                            awordin = primedict[len(temp2)][convertedtoprime]
                            if(awordin not in words):
                                words.append(awordin)
                    except KeyError:
                        pass
                        #print("Keyerror")  
            print("Finished finding words")
            print("Currently Scoring words\n")
            scores = []
            for i in words:
                sum = 0
                for i2 in i:
                    sum += letterweight[i2]
                scores.append(sum)

            words = [words for _, words in sorted(zip(scores, words))]
            socres = scores.sort()
            return words, scores

        def removedumbshit(stringinput):
            stringinput = stringinput.replace("\r", "")
            stringinput = stringinput.replace("\n", "")
            stringinput = stringinput.replace(" ", "")
            stringinput = stringinput.lower()
            return stringinput

        def imageProcessing(imagetest,blackWhite):
            #Import image
            #imagetest = Image.open('temp/mainimage.png')#Import last full image
            #Grayscale and convert to black and white
            imagetest = imagetest.convert('L')  # grayscale
            imagetest = imagetest.point(lambda x: 0 if x < blackWhite else 255, '1')  # Black and white

            #Remove frame / removing noise
            draw = ImageDraw.Draw(imagetest)
            colorfill = 255
            
            #Horizontal lines
            draw.rectangle((0, 150, 430, 180), fill=colorfill)
            draw.rectangle((0, 250, 430, 270), fill=colorfill)
            draw.rectangle((0, 340, 430, 360), fill=colorfill)
            #Vertical lines
            draw.rectangle((162, 100, 190, 430), fill=colorfill)
            draw.rectangle((247, 100, 267, 430), fill=colorfill)
            draw.rectangle((330, 100, 355, 430), fill=colorfill)
            #Outline
            draw.rectangle((0, 0, 530, 100), fill=colorfill)
            draw.rectangle((0, 0, 90, 530), fill=colorfill)#leftline
            draw.rectangle((0, 430, 530, 530), fill=colorfill)
            draw.rectangle((430, 0, 530, 530), fill=colorfill)
            imagetest.save("temp/mainimage.png")
            return imagetest

        def ocrShit(image):
            #Pytesseract ocr code
            pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR/tesseract"
            custom_oem_psm_config = r"--oem 3 --psm 11"
            custom_oem_psm_config3 = r"--oem 3 --psm 3"
            characters = pytesseract.image_to_string(image, lang='Bookworm2', config=custom_oem_psm_config)
            characters = removedumbshit(characters)

            if("x" in characters):
                mode3chars = pytesseract.image_to_string(
                    image, lang='Bookworm2', config=custom_oem_psm_config3)
                removedumbshit(mode3chars)
                for i in [index for index, value in enumerate(characters) if value == "x"]:
                    if(mode3chars[i] == "k"):
                        print("Changed x for k")
                        characters[i] = "k"
            
            return characters
                        


        #Start timer to see how long each check takes
        start_time = time.time()

        #Screenshot code
        imagetest = ImageGrab.grab(bbox=(700, 479, 1230, 1009))
        width, height = imagetest.size
        print("\nTook image (Width = %s, Height = %s)" % (width, height)) 

        #Image code
        image = imageProcessing(imagetest,38)
        characters = ocrShit(image)

        #QU correction
        if(len(characters) > 16):
            pass

        #Prime to alphabet dictionary
        alphabettoprime = {'e': 2, 's': 3, 'i': 5, 'a': 7, 'r': 11, 'n': 13, 't': 17, 'o': 19, 'l': 23, 'c': 29, 'd': 31, 'u': 37,
                        'p': 41, 'm': 43, 'g': 47, 'h': 53, 'b': 59, 'y': 61, 'f': 67, 'v': 71, 'k': 73, 'w': 79, 'z': 83, 'x': 89, 'q': 97, 'j': 101}

        #Weight of each letter
        letterweight = {"a": 1, "b": 1.25, "c": 1.25, "d": 1, "e": 1, "f": 1.25, "g": 1, "h": 1.25, "i": 1, "j": 1.75, "k": 1.75, "l": 1,
                        "m": 1.25, "n": 1, "o": 1, "p": 1.25, "q": 1.75, "r": 1, "s": 1, "t": 1, "u": 1, "v": 1.6, "w": 1.5, "x": 2, "y": 1.5, "z": 2}

        #Test all iterations
        print("Onscreen characters: %s" % (characters.upper()))

        #Print Text grid
        for i in range((len(characters) // 4)):
            print(characters[i*4].upper(), characters[i*4+1].upper(),
                  characters[i*4+2].upper(), characters[i*4+3].upper())
        for i in range((len(characters) % 4), 0, -1):
            print("%s " % (characters[-i].upper()), end='')

        print("\nTotal characters onscreen = %s" % (len(characters)))

        #Starts anagram algorythm
        if(not(len(characters) > 18)):
            words, scores = findwords(characters)

        #Search took print message
        print("The wordfinder took %s seconds to run\n" %(round(time.time() - start_time, 2)))

        #Prints the top 10 words
        output = ""
        if(len(words)> 9):
            for i in range(9, -1, -1):
                print("Word = %-15s Weight = %-15s" % (words[i-10].upper(), scores[i-10]))
                output = output + ("%s,%s\n" % (words[i-10], scores[i-10]))

        #Saves output to file   
        output = output[0:-1]
        f = open("Graph/data.txt", "w")
        f.write(output)
        f.close()
        print("Saved output to file")

    except ValueError:
        print("Cant find onscreencharacters")
        print("eatshit something is wrong")
    
    print("\nReady for input again")

#Sets up hotkeys for everything
startkey = "page up"
print("Waiting for input")
keyboard.add_hotkey(startkey, bookwormcheater)
keyboard.wait("esc")
