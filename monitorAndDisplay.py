from sense_hat import sense_hat
import json

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

def get_cpu_main():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=","").replace("'C\n", ""))

def main():
    sense = SenseHat()
    config = json.load(open('/home/pi/PIoT-Assignment-1/config.json'))

