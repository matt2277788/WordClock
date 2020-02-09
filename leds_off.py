# Write your code here :-)
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 255)

a = [0,1,2,3]

for i in a:
    pixels[i]= ((55,55,55 ))

pixels.fill((0,0,0))