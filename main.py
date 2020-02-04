import numpy as np
from datetime import datetime
import random
import itertools
#import board
#import neopixel

class WordClock:
    def __init__(self):
        filepath = '/home/treffer/playground/WordClock/Layout'
        self.__letterMatrix = np.loadtxt(fname=filepath, dtype=str)
        self.__letterString = ("".join(self.__letterMatrix.tolist()))
        print(self.__letterMatrix.shape)
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
        print(test)
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
        if (minCat == 1 and hourCat == 5):
            doubleFiveAndTen = True;
        if (minCat == 11 and hourCat == 5):
            doubleFiveAndTen = True;
        if (minCat == 2 and hourCat == 10):
            doubleFiveAndTen = True;
        if (minCat == 10 and hourCat == 10):
            doubleFiveAndTen = True;
        return doubleFiveAndTen



#Setup Dictionaries for different word groups
dicIntro  =	{
  "1": "Frau Baby",
  "2": "Frau Baby Bernd",
  "3": "Baby Bernd",
  "4": "Mein Braunling",
  "5": "Hi Braunbert",
  "6": "Meine Katja",
  "7": "Meine Sonne",
  "8": "Hi Schatz",
}
dicItIs  =	{
  "1": "Es ist",
  "2": "Wir haben",
}
dicMinute  =	{
  "0": "Uhr",
  "1": "fünf nach",
  "2": "zehn nach",
  "3": "viertel nach",
  "4": "zwanzig nach",
  "5": "fünf vor halb",
  "6": "halb",
  "7": "fünf nach halb",
  "8": "zehn nach halb",
  "9": "dreiviertel",
  "10": "zehn vor",
  "11": "fünf vor"
}
dicHour  =	{
  "1": "eins",
  "2": "zwei",
  "3": "drei",
  "4": "vier",
  "5": "fünf",
  "6": "sechs",
  "7": "sieben",
  "8": "acht",
  "9": "neun",
  "10": "zehn",
  "11": "elf",
  "12": "zwölf",
}
dicEnd  =	{
  "1": "Kuss",
  "2": "Kiss You",
  "3": "Miss You",
  "4": "Love You",
}

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
#print(wordListToPass)
wordListToPass = itertools.chain.from_iterable(wordListToPass)


#pins to light up
ledList = ins.searchLedPixel(wordListToPass)
print(ledList)


#Test for right Output
#letterList = ins.getLetterString()
#output = []
# for i in range(0, len(ledList)):
#     s = ledList[i]
#     f = letterList[s]
#     output.append(f)
#     print(s , f)
# print(output)


#pixels = neopixel.NeoPixel(board.D18, 30)



