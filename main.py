#!/usr/bin/env python
import numpy as np
from datetime import datetime
import random
import itertools
import sched, time
import board
import neopixel
import atexit

class WordClock:
    def __init__(self):
        filepath = 'Layout'
        self.__letterMatrix = np.loadtxt(fname=filepath, dtype=str)
        self.__letterString = ("".join(self.__letterMatrix.tolist()))
        self.__hourCat = 0
        self.__minCat = 0

    def returnHourCat(self):
        self.__hour = datetime.now().hour
        self.__min = datetime.now().minute
        if (self.__hour == 12 and self.__min>=25):
            self.__hourCat = 1
        elif (self.__hour > 12 and self.__min >=25):
            self.__hourCat = self.__hour - 11
        elif (self.__hour > 12 and self.__min <25):
            self.__hourCat = self.__hour -12
        else:
            self.__hourCat = self.__hour
        return str(self.__hourCat)

    def returnMinuteCat(self):
        self.__minute = datetime.now().minute
        self.__minuteMatrix = np.array(np.arange(0, 60)).reshape(12, 5)
        self.__minuteCategory = np.where(self.__minuteMatrix == self.__minute)
        self.__minuteCategory = str(self.__minuteCategory[0])
        self.__minuteCategory = self.__minuteCategory.split("[")[1].split("]")[0]
        return self.__minuteCategory

    def searchLedPixel(self, wordList):
        s = self.__letterMatrix
        test = self.defineExceptionStateFiveTen()
        pinVector = []
        for item in wordList:
            row = 0
            for line in s:
                if (item in ''.join(line) and test==False):
                    print(item + " ["+ str(row) + "]["+str(line.find(item)) + ":" + str(line.find(item)+len(item))+ "]")
                    for l in range (0,len(item)):
                        pinLightUp = ((row)*13) + (line.find(item) + l)
                        pinVector.append(pinLightUp)
                    break
                elif (item in ''.join(line) and test==True):
                    print(item + " ["+ str(row) + "]["+str(line.find(item)) + ":" + str(line.find(item)+len(item))+ "]")
                    for l in range (0,len(item)):
                        pinLightUp = ((row)*13) + (line.find(item) + l)
                        pinVector.append(pinLightUp)
                else:
                    row += 1

        return pinVector

    def getLetterString(self):
        return self.__letterString

    def defineExceptionStateFiveTen(self):
        minCat = self.returnMinuteCat()
        hourCat = self.returnHourCat()
        doubleFiveAndTen = False
        if (minCat == 1 and hourCat == 5): #fünf nach fünf
            doubleFiveAndTen = True
        if (minCat == 11 and hourCat == 5): #fünf vor fünf
            doubleFiveAndTen = True
        if (minCat == 5 and hourCat == 5): #fünf vor halb fünf
            doubleFiveAndTen = True
        if (minCat == 7 and hourCat == 5): #fünf nach halb fünf
            doubleFiveAndTen = True
        if (minCat == 2 and hourCat == 10): #zehn nach zehn
            doubleFiveAndTen = True
        if (minCat == 10 and hourCat == 10): #zehn vor zehn
            doubleFiveAndTen = True
        if (minCat == 8 and hourCat == 10): #zehn nach halb zehn
            doubleFiveAndTen = True
        return doubleFiveAndTen



#Setup Dictionaries for different word groups
dicIntro  = {
  "1": "FRAU BABY",
  "2": "FRAU BABY BERND",
  "3": "BABY BERND",
  "4": "MEIN BRAUNLING",
  "5": "HI BRAUNBERT",
  "6": "MEINE KATJA",
  "7": "MEINE SONNE",
  "8": "HI SCHATZ",
}
dicItIs  =  {
  "1": "ES IST",
  "2": "WIR HABEN",
}
dicMinute  =    {
  "0": "UHR",
  "1": "FUENF NACH",
  "2": "ZEHN NACH",
  "3": "VIERTEL NACH",
  "4": "ZWANZIG NACH",
  "5": "FUENF VOR HALB",
  "6": "HALB",
  "7": "FUENF NACH HALB",
  "8": "ZEHN NACH HALB",
  "9": "DREIVIERTEL",
  "10": "ZEHN VOR",
  "11": "FUENF VOR"
}
dicHour  =  {
  "1": "EINS",
  "2": "ZWEI",
  "3": "DREI",
  "4": "VIER",
  "5": "FUENF",
  "6": "SECHS",
  "7": "SIEBEN",
  "8": "ACHT",
  "9": "NEUN",
  "10": "ZEHN",
  "11": "ELF",
  "12": "ZWOELF",
}
dicEnd  =   {
  "1": "KUSS",
  "2": "KISS YOU",
  "3": "MISS YOU",
  "4": "LOVE YOU",
}


def tellTime():
    #Instanciate
    ins = WordClock()

    #get Dictionary Keys
    hourCat = ins.returnHourCat()
    minCat = ins.returnMinuteCat()
    randItIs = str(random.randint(1,2))
    randIntro = str(random.randint(1,8))
    randEnd = str(random.randint(1,4))

    #get Word List to Pass to function for finding postion of LED pixels
    wordListToPass = [dicIntro.get(randIntro).split(), dicItIs.get(randItIs).split(),  dicMinute.get(minCat).split(), dicHour.get(hourCat).split(), dicEnd.get(randEnd).split()]
    wordListToPass = itertools.chain.from_iterable(wordListToPass)


    #pins to light up
    ledList = ins.searchLedPixel(wordListToPass)
    #print(ledList)

    #Test for right Output
    letterList = ins.getLetterString()
    output = []
    for i in range(0, len(ledList)):
         s = ledList[i]
         f = letterList[s]
         output.append(f)
         print(s, f)
    return output, ledList


#setup of raspi and neopixel
pixels = neopixel.NeoPixel(board.D18, 255)

def ledShutOff(): #reset all pixel to 0
    pixels.fill((0,0,0))

def lightUpLeds():
    randRed= random.randint(1,155)
    randGreen= random.randint(1,155)
    randBlue=random.randint(1,155)

    ledShutOff() #calling function to turn LEDs off
    wordOutput, ledList = tellTime() #get values for WordOutput and ledList
    for i in ledList:                   # turn LEDs on
        pixels[i]= ((randRed,randGreen,randBlue)) #setting color of individual LED pixel
    with open('output_test.txt', 'a') as f:
        print(wordOutput, ledList, file= f)

lightUpLeds() #initially calling function

# Running tellTime() every 60 sec
s = sched.scheduler(time.time, time.sleep)
def schedTellTime():
    lightUpLeds()
    s.enter(60, 1, schedTellTime)

s.enter(60, 1, schedTellTime)
s.run()


atexit.register(ledShutOff)


# Bei Abbruch des Programms alle LEDs aus
# Ausführung des Programs bei boot
# Pulsierendes Herz am Ende
# Prüfen: zehn nach halb zehn - fünf nach halb fünf
