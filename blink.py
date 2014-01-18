# from http://raspberrypi.stackexchange.com/questions/9013/why-cant-i-turn-on-an-led-through-python

#  2  4  6  8 10 12 14 16 18 20 22 24 26
#  1  3  5  7  9 11 13 15 17 19 21 23 25
# Connect the LED to 6 and 12.

from RPi import GPIO
from time import sleep
import atexit

def main():
  #Use the physical pin numbers, not the logical names
  GPIO.setmode(GPIO.BOARD)

  GPIO.setup(12, GPIO.OUT)

  blink_pwm()
  #blink()

def blink():
  while True:
    print "on"
    GPIO.output(12, True)
    sleep(3)
    print "off"
    GPIO.output(12, False)
    sleep(3)

def blink_pwm():
  p = GPIO.PWM(12, 100)
  p.start(10)
  while True:
    for dcs in range(0,90,2), range(90,0,-2):
      for dc in dcs:
	p.ChangeDutyCycle(dc)
	sleep(0.05)
    p.ChangeDutyCycle(0)
    sleep(1)
  p.stop()

atexit.register(GPIO.cleanup)

main()
