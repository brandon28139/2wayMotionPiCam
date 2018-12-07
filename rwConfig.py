import configparser
config = configparser.ConfigParser()
config.sections()

DetType = None
MotionSen = None
RecLen = None
Qual = None

def readConfig():
    config.read('homeCam.conf')
    DetType = config['DEFAULT']['DetectType']
    MotionSen = config['DEFAULT']['MotionSensitivty']
    RecLen = config['DEFAULT']['RecordLength']
    Qual = config['DEFAULT']['Quality']
