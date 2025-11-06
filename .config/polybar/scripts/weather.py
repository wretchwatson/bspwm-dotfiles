#!/usr/bin/env python3
import requests
import sys

def get_weather():
    try:
        api_key = "0ac4f6b0fd31e778aad919cac94a5c7e"
        city = "Ödemiş,TR"
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            temp = round(data['main']['temp'])
            feels_like = round(data['main']['feels_like'])
            humidity = data['main']['humidity']
            description = data['weather'][0]['description'].title()
            icon_code = data['weather'][0]['icon']
            wind_speed = data['wind']['speed']
            
            weather_icons = {
                '01d': '☀️', '01n': '🌙',
                '02d': '⛅', '02n': '☁️',
                '03d': '☁️', '03n': '☁️',
                '04d': '☁️', '04n': '☁️',
                '09d': '🌧️', '09n': '🌧️',
                '10d': '🌦️', '10n': '🌧️',
                '11d': '⛈️', '11n': '⛈️',
                '13d': '❄️', '13n': '❄️',
                '50d': '🌫️', '50n': '🌫️'
            }
            
            icon = weather_icons.get(icon_code, '🌤️')
            
            if len(sys.argv) > 1 and sys.argv[1] == "--tooltip":
                print(f"{description} | Hissedilen: {feels_like}°C | Nem: {humidity}% | Rüzgar: {wind_speed} m/s")
            else:
                print(f"{icon} {temp}°C")
        else:
            print("🌤️ N/A")
    except:
        print("🌤️ --")

if __name__ == "__main__":
    get_weather()
