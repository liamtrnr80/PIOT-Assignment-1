from sense_hat import SenseHat
from time import sleep
import json
import os


r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

class Temp():
    def __init__(self, temperature):
        self.temperature = temperature

    def checkTemp(self, config):
        if(self.temperature <= config['cold_max']):
            print("Sup") # Place holder

    def setTemperature(self, sense):
        temp1 = sense.get_temperature_from_humidity()
        # Done because of a bug with humidity which returns a 0
        if(temp1 == 0):
            temp1 = sense.get_temperature_from_humidity()
        
        temp2 = sense.get_temperature_from_pressure()
        # Done because of a bug with pressure which returns a 0
        if(temp2 == 0):
            temp2 = sense.get_temperature_from_pressure()
        
        temp_cpu = get_cpu_temp()
        temp = (temp1 + temp2) /2
        temp_corr = temp - ((temp_cpu - temp) / 1.5)
        temp_corr = get_smooth(temp_corr)


def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=","").replace("'C\n", ""))

def get_smooth(x):
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x, x, x]
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x
    return (get_smooth.t[0] + get_smooth.t[1] + get_smooth.t[2]) / 3

def main():
    sense = SenseHat()
    config = json.load(open('/home/pi/PIoT-Assignment-1/config.json'))
    temp = Temp(0)

    while True:
        temp.checkTemp(config)
        sleep(10)

if __name__ == '__main__':
    main()