import picamera
import configparser
import RPi.GPIO as GPIO

config = configparser.ConfigParser()
config.sections()
config.read('homeCam.conf')
DetType = config['DEFAULT']['DetectType']
MotionSen = config['DEFAULT']['MotionSensitivty']
RecLen = config['DEFAULT']['RecordLength']
Qual = config['DEFAULT']['Quality']

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.setup(3, GPIO.OUT) # Set pin 3 to be a motion detector

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH and DetType == "button":
                print("Button was pushed!")
    elif  GPIO.output(3,1) and DetType == "motion":
                print("Motion Detected!")
    elif (GPIO.output(3,1) or GPIO.input(10) == GPIO.HIGH) and DetType == "both":
                print("button or motion detected!")


