#!/usr/bin/env python
import sched, time
import board
import neopixel
from classWordClock import WordClock
from setupLEDs import getMyLEDs, lightUpLeds, ledShutOff     

#Instanciate a Wordclock
myWordClock = WordClock()

#setup of raspi and neopixel
pixels = neopixel.NeoPixel(board.D18, 255)

#initially calling function to light up pixels
lightUpLeds(myWordClock, pixels) 

# Running function to light up pixels every 60 sec
s = sched.scheduler(time.time, time.sleep)
def schedTellTime():
    lightUpLeds(myWordClock, pixels)
    s.enter(60, 1, schedTellTime)

s.enter(60, 1, schedTellTime)
s.run()

# Bei Abbruch des Programms alle LEDs aus
# Ausführung des Programs bei boot
# Pulsierendes Herz am Ende
# Prüfen: zehn nach halb zehn - fünf nach halb fünf
