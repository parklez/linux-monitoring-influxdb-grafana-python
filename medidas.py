import time
from influxdb import InfluxDBClient
from functions import *


client = InfluxDBClient('localhost', 8086, 'root', 'root', 'medidas')

cpu_name = get_cpu_name()

def get_data():
    iso = time.ctime()
    cpu_temp = get_cpu_temp()
    free_mem = get_mem_free()

    print('cpu_temp', cpu_temp)
    print('free_mem', free_mem)

    json_body = [
            {
                "measurement": "ambient_celcius",
                "tags": {"host": 'My Laptop'},
                "time": iso,
                "fields": {
                    "value": cpu_temp,
                    },
                "measurement": "free_mem",
                "tags": {"host": 'My laptop'},
                "time": iso,
                "fields": {
                    "value": free_mem,
                    },
            }
            ]

    return json_body

# If database hasn't been created yet
client.create_database('medidas')

sleep_duration = 1
while True:
    json_body = get_data()
    client.write_points(json_body)
    print (".")
    time.sleep(sleep_duration)
