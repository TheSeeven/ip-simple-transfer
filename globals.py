from operations import *
from gui import *
from multiprocessing import *

MY_IP_ADRESS = getIpAdress()
GUI = Interface(MY_IP_ADRESS)
samplethread = Process(target=samplethreadfunction)