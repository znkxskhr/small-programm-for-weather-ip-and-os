import httpx
import socket
import psutil
import platform
from datetime import datetime


print("1. your current weather\n"
"2. your current ip\n"
"3. your computer components\n")

try:
    user_input = int(input("enter 1-3: "))
except ValueError:
    user_input = 0


if user_input == 1:
    r = httpx.get('https://wttr.in/?format=j1')
    weather = ['FeelsLikeC', 'cloudcover', 'humidity', 'TempC', 'Temp_C']
    data = r.json()
    current_weather = data['current_condition'][0]
    print("current weather: ")
    for key in weather:
        value = current_weather.get(key, 'not found')
        print(f"{key}: {value}")
        #print(data)

    
elif user_input == 2:
    print("your current ip: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
    s.close()


elif user_input == 3:
    print("your current components")
    uname = platform.uname()
    ram = psutil.virtual_memory()

    print(f"ОС: {uname.system} {uname.release}")
    print(f"Pc Name: {uname.node}")
    print(f"Machine: {uname.machine}")
    print(f"Proccessor: {uname.processor}")
    print("\n" \
    "Do you need more information?")
    uip = int(input("1.Yes / 2. No: "))
    if uip == 1:

        print(f"physicall cores: {psutil.cpu_count(logical=False)}")
        print(f"Logical cores: {psutil.cpu_count(logical=True)}")
        cpufreq = psutil.cpu_freq
        if cpufreq:
            print(f"current cpu freq {cpufreq.current:.2f} MHz")
        else:
            print(f"current cpu freq: DO NOT SUPPORT YOUR OS")
        print(f"Full ram space: {ram.total / (1024**3):.2f} GB")
        print(f"Free free ram space: {ram.available / (1024**3):.2f} GB")
        print(f"Current % ram usage: {ram.percent}%")
else:
    print("wrong input. ")