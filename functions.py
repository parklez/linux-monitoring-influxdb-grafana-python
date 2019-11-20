
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

def _get_cpu_averageload():
    path = "/proc/loadavg"
    f = open(path, "r")
    averages = f.read().strip().split(" ")
    f.close()
    return averages

def get_system_load_last_min():
    return _get_cpu_averageload()[0]

def get_last_pid():
    return _get_cpu_averageload()[-1]

def get_processes_threads():
    return _get_cpu_averageload()[3].split("/")[1]

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

def _get_current_logged_users():
    # https://linuxhandbook.com/linux-login-history/
    # /var/run/utmp
    result = execute_shell('who')
    # https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
    return str(result, 'utf8')

def get_number_of_logged_users():
    output = _get_current_logged_users()
    return len(output.splitlines())

def get_uptime():
    path="/proc/uptime"
    f = open(path, "r")
    uptime = f.read().split(" ")
    f.close()
    return float(uptime[0])

def get_number_of_processes_since_boot():
    path = "/proc/stat"
    f = open(path, "r")
    for line in f:
        if line.startswith("processes"):
            break
    f.close()
    return int(line.split()[1])

_received = -1
_sent = -1

#Network I/O could've been written using /proc/stat, it might sum up use from all network devices.
def get_received_bytes():
    'returns bytes worth of traffic since last call'
    received_path = '/sys/class/net/wlp2s0/statistics/rx_bytes'

    rf = open(received_path, 'r')

    data = int(rf.read())
    rf.close()
    
    global _received

    if _received == -1:
        _received = data
        return 0
    
    else:
        diff =  data - _received
        _received = data
        return diff

def get_sent_bytes():
    'returns bytes worth of traffic since last call'
    sent_path = '/sys/class/net/wlp2s0/statistics/tx_bytes'

    sf = open(sent_path, 'r')

    data = int(sf.read())
    sf.close()
    
    global _sent

    if _sent == -1:
        _sent = data
        return 0
    
    else:
        diff =  data - _sent
        _sent = data
        return diff

# https://unix.stackexchange.com/questions/55212/how-can-i-monitor-disk-io
# TODO: write I/O stuff
