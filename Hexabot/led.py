
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D10, 24)

pixel_pin = board.D10

num_pixels = 24

def LED():
    while True:
        
        count = 0
        p_on = 0

        while count < 72:
            pixels[p_on] = (0, 0, 255)
            if p_on < 21:
                pixels[p_on+1] = (0, 0, 255)
                pixels[p_on+2] = (0, 0, 255)
            time.sleep(0.01)
            pixels[p_on] = (0, 0, 0)
            if p_on < 21:
                pixels[p_on+1] = (0, 0, 0)
                pixels[p_on+2] = (0, 0, 0)
            p_on = p_on + 1
            count = count + 1
            if p_on == 23:
                p_on = 0
        p_on = 0

        while count < 79:
            pixels.fill((0, 0, 255))
            time.sleep(0.1)
            pixels.fill((0, 0, 0))
            time.sleep(0.1)
            count = count + 1
