# Write your code here :-)
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 255)

pixels.fill((5,0,0))