import RPi.GPIO as GPIO # Import Raspberry Pi GPIO libr
from time import sleep

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

pin1 = 11
pin2 = 13
GPIO.setup(pin1, GPIO.IN)
GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)
while True:
   if GPIO.input(pin1):
      GPIO.output(pin2, True)
   else:
      GPIO.output(pin2, False)
   sleep(0.01)
GPIO.cleanup()
