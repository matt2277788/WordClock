import numpy as np
from datetime import datetime
import random
import itertools
import sched, time
import board
import neopixel
import atexit
import re
import wordClockDictionaries

def getMyLEDs(myWordClock):
    #get Dictionary Keys
    hourCat = myWordClock.returnHourCat()
    minCat = myWordClock.returnMinuteCat()
    randItIs = str(random.randint(1,2))
    randIntro = str(random.randint(1,8))
    randEnd = str(random.randint(1,4))

    #get Word List to Pass to function for finding postion of LED pixels
    # get dictionaries from wordClockDictionaries File
    dicIntro = wordClockDictionaries.dicIntro
    dicItIs = wordClockDictionaries.dicItIs
    dicMinute = wordClockDictionaries.dicMinute
    dicHour = wordClockDictionaries.dicHour
    dicEnd = wordClockDictionaries.dicEnd
    wordListToPass = [dicIntro.get(randIntro).split(), dicItIs.get(randItIs).split(),  dicMinute.get(minCat).split(), dicHour.get(hourCat).split(), dicEnd.get(randEnd).split()]
    wordListToPass = itertools.chain.from_iterable(wordListToPass)


    #pins to light up
    ledList = myWordClock.getLedList(wordListToPass)
    flippedLedList = myWordClock.getFlippedLedList(ledList)
    
    #Test for right Output in Terminal
    letterList = myWordClock.getLetterString()
    flippedLetterList = myWordClock.getFlippedLetterString()
    for i in range(0, len(ledList)):
         s = flippedLedList[i]
         f = flippedLetterList[s]
         y = ledList[i]
         z = letterList[y]
         print(s, f, y, z)

    return ledList, flippedLedList


def ledShutOff(pixels): #reset all pixel to 0
    pixels.fill((0,0,0))

def lightUpLeds(myWordClock, pixels):
    randRed= random.randint(1,20)
    randGreen= random.randint(1,20)
    randBlue=random.randint(1,20)

    ledShutOff(pixels) #calling function to turn LEDs off
    ledList, flippedLedList = getMyLEDs(myWordClock) #get values for WordOutput and ledList
    flippedSetup = True
    if (flippedSetup == True):
        for i in flippedLedList:                   # turn LEDs on
            pixels[i]= ((randRed,randGreen,randBlue)) #setting color of individual LED pixel
    else:
        for i in ledList:                   # turn LEDs on
            pixels[i]= ((randRed,randGreen,randBlue)) #setting color of individual LED pixel