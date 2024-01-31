from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import sys
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(11, GPIO.IN)

BLINK_RATE = 1
PROGRAM_LENGTH = 10
if (len(sys.argv) > 2):
   BLINK_RATE = int(sys.argv[1])
   PROGRAM_LENGTH = int(sys.argv[2])
ITER_COUNT = int(PROGRAM_LENGTH / (BLINK_RATE))
DEBUG = False
if '-debug' in sys.argv:
  DEBUG = True
LED_PIN = 13
PIN_NUMBER = 11
LED_IS_ON = False
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
with open('data.txt', 'w') as data:
  for i in range(0, ITER_COUNT): # loop through ITER_COUNT times
    if not(GPIO.input(PIN_NUMBER)):
      LED_IS_ON = False
    GPIO.output(LED_PIN, LED_IS_ON)
    # Just show time in seconds not fraction of seconds
    data.write(f'{time.time():1.0f} {LED_IS_ON}\n')
    if DEBUG:
      t = time.time()
      date_t = datetime.fromtimestamp(t)
      print(f'switch is on: {GPIO.input(PIN_NUMBER)} \t LED is on: {GPIO.input(LED_PIN)} \t current time: {date_t} \t number of iteration: {i}')
    LED_IS_ON = not(LED_IS_ON)
    time.sleep(BLINK_RATE)
GPIO.cleanup()
