

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
#import sys, signal
#def signal_handler(signal, frame):
#    print("\nprogram exiting gracefully")
#    sys.exit(0)

#signal.signal(signal.SIGINT, signal_handler) 
 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 24
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False,
                           pixel_order=ORDER)

try:
	while True:
		pixels.fill((255,255,255))
		pixels.show()
		#time.sleep(1)
		#pixels.fill((0,0,0))
		#pixels.show()
		#time.sleep(1)
		
except KeyboardInterrupt:
	pixels.fill((0,0,0))
	pixels.show()
