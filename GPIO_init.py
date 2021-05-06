import RPi.GPIO as GPIO

resetPin = 27
u4_resetPin = 4
u3_resetPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(resetPin, GPIO.OUT)
GPIO.output(resetPin, GPIO.LOW)

GPIO.output(resetPin, GPIO.HIGH)