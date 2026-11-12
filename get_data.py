import pandas as pd
import requests

url = "https://archive-api.open-meteo.com/v1/archive?latitude=36.62&longitude=44.88&start_date=2020-01-01&end_date=2025-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&timezone=auto"

print("سەرقاڵی هێنانی داتای کەشوهەوای چۆمانم...")
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["daily"])
df.to_csv("choman_weather.csv", index=False)
print("سەرکەوتوو بوو! فایلی 'choman_weather.csv' دروستبوو.")