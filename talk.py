# from http://raspberrypi.stackexchange.com/questions/9013/why-cant-i-turn-on-an-led-through-python

from RPi import GPIO
from time import sleep
import atexit
import sys
import os

def main():
  print "  2  4  6  8 10 12 14 16 18 20 22 24 26"
  print "  1  3  5  7  9 11 13 15 17 19 21 23 25"

  print " 1 = 3.3V"
  print " 3 = input from switch (pull up)"
  print " 6 = ground"
  print "12 = output to LED"

  #Use the physical pin numbers, not the logical names
  GPIO.setmode(GPIO.BOARD)

  GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(12, GPIO.OUT)

  GPIO.add_event_detect(3, GPIO.RISING, callback=clicked, bouncetime=200)

  while True:
    sleep(60)

def clicked(channel):
  os.system("curl -X POST http://{}:4576/talk".format(sys.argv[1]))

atexit.register(GPIO.cleanup)

main()
