"""
Here's a bunch of functions to get information from the machine
Daijoubu
"""
import subprocess
    

def execute_shell(arg):
    return subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE).stdout.read()

def get_cpu_temp():
    path="/sys/class/thermal/thermal_zone0/temp"
    f = open(path, "r")
    temp_raw = int(f.read().strip())
    temp_cpu = float(temp_raw / 1000.0)
    f.close()
    return temp_cpu

def get_cpu_averageload():
    path = "/proc/loadavg"
    f = open(path, "r")
    averages = f.read().strip().split(" ")
    f.close()
    return averages

def get_cpu_name():
    path = "/proc/cpuinfo"
    f = open(path, "r")
    for line in f:
        if line.startswith("model name"):
            break
    f.close()
    return line.strip()[13:]

def _get_mem_usage():
    path = "/proc/meminfo"
    result = []
    f = open(path, "r")
    for line in f:
        if line.startswith("MemTotal:") or line.startswith("MemFree:") or line.startswith("MemAvailable:"):
            result.append(line.strip())
    f.close()
    return result

def get_mem_total():
    return _get_mem_usage()[0].split()[1]

def get_mem_free():
    return _get_mem_usage()[1].split()[1]

def get_mem_avail():
    return _get_mem_usage()[2].split()[1]

def get_current_logged_users():
    # https://linuxhandbook.com/linux-login-history/
    # /var/run/utmp
    result = execute_shell('who')
    # https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
    return str(result, 'utf8')


# https://unix.stackexchange.com/questions/55212/how-can-i-monitor-disk-io
# TODO: write I/O stuff and NETWORK stuff
