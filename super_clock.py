import time
import json
import requests
import os
from datetime import datetime
from gpiozero import LED, Button
from threading import Thread

# Load configuration
with open('config.json') as config_file, open('alarms.json') as alarms_file:
    config = json.load(config_file)
    alarms = json.load(alarms_file)["alarms"]

# Constants
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
CITY = config['city']
ALARM_PIN = 17  # GPIO pin for the alarm (change as needed)

# Initialize alarm
alarm_led = LED(ALARM_PIN)
alarm_button = Button(2)  # Button to stop the alarm

def get_weather():
    params = {
        'q': CITY,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_API_URL, params=params)
    data = response.json()
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        weather_info = f"Weather: {weather}, Temp: {temperature}°C"
    else:
        weather_info = "Error fetching weather data"
    return weather_info

def display_time():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Time: {current_time}")
        print(get_weather())
        time.sleep(60)  # Update every minute

def check_alarms():
    while True:
        now = datetime.now().strftime("%H:%M")
        if now in alarms:
            alarm_led.on()
            print("Alarm! Press the button to stop.")
            alarm_button.wait_for_press()
            alarm_led.off()
        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    display_thread = Thread(target=display_time)
    alarm_thread = Thread(target=check_alarms)
    display_thread.start()
    alarm_thread.start()
    display_thread.join()
    alarm_thread.join()