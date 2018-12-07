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





