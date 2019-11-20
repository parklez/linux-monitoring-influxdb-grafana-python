import time
from influxdb import InfluxDBClient
from functions import *

debug = True

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'medidas')

cpu_name = get_cpu_name()

def get_data():

    # Make threads for all these:
    iso = time.ctime()
    cpu_temp = get_cpu_temp()
    free_mem = int(get_mem_free())
    used_mem = (int(get_mem_total()) - int(get_mem_free()))
    logged_users = get_number_of_logged_users()
    last_pid = int(get_last_pid())
    avg_load = float(get_system_load_last_min())
    cpu_pt = get_processes_threads()
    #
    if debug:
        print('cpu_temp', cpu_temp)
        print('free_mem', free_mem)
        print('used_mem', used_mem)
        print('logged_users', logged_users)


    json_body = [
                {
                "measurement": "temperatura_cpu",
                "tags": {"host": 'My Laptop'},
                "time": iso,
                "fields": {
                    "value": cpu_temp,
                    }
                },
                {
                "measurement": "memoria_ocupada",
                "tags": {"host": 'My Laptop'},
                "time": iso,
                "fields": {
                    "value": used_mem,
                    }
                },
                {
                "measurement": "usuarios_logados",
                "tags": {"host": 'My Laptop'},
                "time": iso,
                "fields": {
                    "value": logged_users,
                    }
                },
                {
                "measurement": "ultimo_pid",
                "tags": {"host": 'My Laptop'},
                "time": iso,
                "fields": {
                    "value": last_pid,
                    }
                },
                {
                "measurement": "system_load",
                "tags": {"host": 'My Laptop'},
                "time": iso,
                "fields": {
                    "value": avg_load,
                    }
                },
                {
                "measurement": "processes_threads",
                "tags": {"host": 'My Laptop'},
                "time": iso,
                "fields": {
                    "value": cpu_pt,
                    }
                },
                {
                "measurement": "memoria_livre",
                "tags": {"host": 'My laptop'},
                "time": iso,
                "fields": {
                    "value": free_mem,
                    }
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
