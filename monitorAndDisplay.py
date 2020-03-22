from sense_hat import SenseHat
from time import sleep
import json
import os


hot = (255, 0, 0)
good = (0, 255, 0)
cold = (0, 0, 255)
white = (150, 150, 150)

class Temp():
    def __init__(self, temperature, colour):
        self.temperature = temperature
        self.colour = colour
        self.nums = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1,
                     0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
                     1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 
                     1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
                     1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1,
                     1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1,
                     1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,   
                     1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
                     1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
                     1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1]

    def checkTemp(self, config):
        if(self.temperature <= config['cold_max']):
            self.colour = cold
        elif(self.temperature >= config['hot_min']):
            self.colour = hot
        else:
            self.colour = good

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
        self.temperature = round(temp_corr)

    def display_num(self, sense, val, x, y, r, g, b):
        offset = val * 15
        for pix in range(offset, offset + 15):
            xt = pix % 3
            yt = (pix - offset) // 3
            sense.set_pixel(xt + x, yt + y, r * self.nums[pix], g * self.nums[pix], b * self.nums[pix])

    def display_temp(self, sense):
        abs_temp = abs(self.temperature)
        tens = abs_temp // 10
        ones = abs_temp  % 10
        r = self.colour[0]
        g = self.colour[1]
        b = self.colour[2]

        if (abs_temp > 9):
            self.display_num(sense, tens, 1, 2, r, g, b)
        else:
            self.display_num(sense, 0, 1, 2, r, g, b)
        
        self.display_num(sense, ones, 5, 2, r, g, b)
            

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
    temp = Temp(0, white)

    while True:
        temp.setTemperature()
        temp.checkTemp(config)
        temp.display_temp(sense)
        sleep(10)

if __name__ == '__main__':
    main()