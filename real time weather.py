import requests
import matplotlib.pyplot as plt
from time import sleep

api_key = 'YOUR_API_KEY'
city = 'Bengaluru'
temps = []

plt.ion()  # Interactive mode on
fig, ax = plt.subplots()

for _ in range(10):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
    data = res.json()
    temps.append(data['main']['temp'])
    ax.clear()
    ax.plot(temps, marker='o')
    ax.set_title(f"Temperature in {city} (°C)")
    plt.pause(1)
    sleep(1)
