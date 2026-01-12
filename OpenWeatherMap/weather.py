import requests
# استيراد المفتاح من الملف الذي أنشأناه
from API_KEY import MY_SECRET_KEY
 
# 1. Konfiguration
URL = "https://api.openweathermap.org/data/2.5/weather"
LAT = 52.5200
LON = 13.4050
 
# 2. Parameter mit dem importierten Key
params = {
    "lat": LAT,
    "lon": LON,
    "appid": MY_SECRET_KEY, # هنا استخدمنا المتغير المستورد
    "units": "metric",
    "lang": "de"
}
 
# 3. Daten abrufen und SPEICHERN
try:
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        data = response.json()
        
        # طباعة النتائج للتأكد
        print(f"Erfolg! Stadt: {data['name']}")
        
        # --- إضافة كود الحفظ في ملف CSV ---
        with open("weather_data.csv", "a", encoding="utf-8") as file:
            # حفظ: المدينة، الحرارة، وصف الطقس
            line = f"{data['name']},{data['main']['temp']},{data['weather'][0]['description']}\n"
            file.write(line)
        print("Daten wurden in weather_data.csv gespeichert.")
        
    else:
        print(f"Fehler: {response.status_code}")
except Exception as e:
    print(f"Verbindungsfehler: {e}")
 