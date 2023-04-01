import csv
import time
import datetime
import os.path

from sense_hat import SenseHat

def getCurrentDateTime():
    # https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python
    return datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()

sense = SenseHat()
sensingPeriod = 10
datafile = "data.csv"

def sample(
        temperatureC = None, temperatureFromHumidity= None, temperatureFromBarometer=None, humidityRelative=None, pressure=None, sampleStart=None, sampleEnd=None):
    return {
        "thermometerTemperature": temperatureC,
        "hygrometerTemperature": temperatureFromHumidity,
        "barometerTemperature": temperatureFromBarometer,
        "hygrometerHumidity": humidityRelative,
        "barometerPressure": pressure,
        "measureStartTime": sampleStart,
        "measureEndTime": sampleEnd
    }

def fieldnames():
    return list(sample().keys())

if not os.path.isfile(datafile):
    print("Creating CSV file")
    with open(datafile, mode="w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames())
        writer.writeheader()

while True:
    pollingStart = getCurrentDateTime()
    temperatureC = sense.temp
    temperatureFromHumidityC = sense.get_temperature_from_humidity()
    temperatureFromBarometerC = temp = sense.get_temperature_from_pressure()
    humidityRelative = sense.humidity
    pressure = sense.pressure
    pollingEnd = getCurrentDateTime()

    row = sample(
        temperatureC=temperatureC,
        temperatureFromHumidity=temperatureFromHumidityC,
        temperatureFromBarometer=temperatureFromBarometerC,
        humidityRelative=humidityRelative,
        pressure=pressure,
        sampleStart=pollingStart,
        sampleEnd=pollingEnd)

    with open(datafile, mode="a", newline='') as csvfile:
        print("")
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames())
        writer.writerow(row)

    time.sleep(sensingPeriod)