import numpy as np
from datetime import datetime
import random

class WordClock:
    def __init__(self):
        filepath = '/home/treffer/playground/WordClock/Layout'
        self.__letterMatrix = np.loadtxt(fname=filepath, dtype=str)

    def returnHourCat(self):
        self.__hour = datetime.now().hour
        self.__min = datetime.now().minute
        if self.__hour >=12:
            self.__hourCat = self.__hour - 12
        if self.__min >= 25:
            self.__hourCat = self.__hourCat + 1
        return str(self.__hourCat)

    def returnMinuteCat(self):
        self.__minute = datetime.now().minute
        self.__minuteMatrix = np.array(np.arange(0, 60)).reshape(12, 5)
        self.__minuteCategory = np.where(self.__minuteMatrix == self.__minute)
        self.__minuteCategory = str(self.__minuteCategory[0])
        self.__minuteCategory = self.__minuteCategory.split("[")[1].split("]")[0]
        return self.__minuteCategory

    def searchWords(self, wordList = []):
        s = self.__letterMatrix
        for item in wordList:
            row = 0
            for line in s:
                if item in ''.join(line):
                    print(item + " ["+ str(row) + "]["+str(line.find(item)) + ":" + str(line.find(item)+len(item))+ "]")
                    break
                else:
                    row += 1


#Setup Dictionaries for different word groups
dicIntro  =	{
  "1": "Frau Baby",
  "2": "Frau Baby Bernd",
  "3": "Baby Bernd",
  "4": "Mein Braunling",
  "5": "Hi Braunbert",
  "6": "Meine Katja",
  "7": "Meine Sonne",
  "8": "Meine Sterne",
  "9": "Hi Schatz",
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
  "1": "ein",
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
randIntro = str(random.randint(1,9))
randEnd = str(random.randint(1,4))

#Get locations of used words
ins.searchWords(dicIntro.get(randIntro).split())
ins.searchWords(dicItIs.get(randItIs).split())
ins.searchWords(dicMinute.get(minCat).split())
ins.searchWords(dicHour.get(hourCat).split())
ins.searchWords(dicEnd.get(randEnd).split())



