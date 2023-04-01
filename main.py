from sense_hat import SenseHat
import csv
import time

sense = SenseHat()
sensingPeriod = 1
while True:
    temperatureC = sense.temp
    temperatureFromHumidityC = sense.get_temperature_from_humidity()
    temperatureFromBarometerC = temp = sense.get_temperature_from_pressure()
    humidityRelative = sense.humidity
    pressure = sense.pressure
    print(f"T1 = {temperatureC:.2f}, T2 = {temperatureFromHumidityC:.2f}, T3 = {temperatureFromBarometerC:.2f}")
    print(f"humidity = {humidityRelative}, pressure = {pressure}")
    time.sleep(sensingPeriod)