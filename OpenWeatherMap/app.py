import streamlit as st
import requests
from discord_webhook import DiscordWebhook
from API_KEY import MY_SECRET_KEY
 
# إعداد عنوان الصفحة
st.set_page_config(page_title="Weather App (OWM)", layout="wide")
st.title("☀️ Weather App (OpenWeatherMap)")
st.write("Search by city name or by latitude/longitude. Shows description in English & German.")
 
# 1. وضع اختيار البحث 
search_mode = st.radio("Search mode", ["City name", "Latitude/Longitude"])
 
# إعداد المتغيرات
city_name = ""
lat, lon = 0.0, 0.0
 
# 2. حقول الإدخال حسب الوضع المختارة 
if search_mode == "City name":
    city_name = st.text_input("City name", "Berlin")
    url_base = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={MY_SECRET_KEY}&units=metric"
else:
    col_lat, col_lon = st.columns(2)
    lat = col_lat.number_input("Latitude", value=52.52)
    lon = col_lon.number_input("Longitude", value=13.40)
    url_base = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={MY_SECRET_KEY}&units=metric"
 
# 3. زر جلب البيانات
if st.button("Get weather"):
    # جلب البيانات بالإنجليزية والألمانية (متطلب
    res_en = requests.get(url_base + "&lang=en").json()
    res_de = requests.get(url_base + "&lang=de").json()
 
    if res_en.get("main"):
        st.divider()
        st.header(f"📍 {res_en['name']}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Temperature", f"{res_en['main']['temp']} °C")
            [cite_start]st.write(f"**Description (EN):** {res_en['weather'][0]['description']}") #[span_12](end_span)
        
        with col2:
            [span_13](start_span)st.write(f"**Beschreibung (DE):** {res_de['weather'][0]['description']}") #[span_13](end_span)
            st.write(f"**Humidity:** {res_en['main']['humidity']}%")
 
        # ميزة إرسال التنبيه 
        WEBHOOK_URL = "https://discordapp.com/api/webhooks/1460250874302566571/zM4x1I-tiZYX12KCiQb3sTNfBioIFcjDEZnWhDZrSaMRE9Edy4vifjcFSvR"
        if st.button("🚀 Send Alert to Discord"):
            msg = f"Wetter Update: {res_en['name']} - {res_en['main']['temp']}°C ({res_de['weather'][0]['description']})"
            DiscordWebhook(url=WEBHOOK_URL, content=msg).execute()
            st.success("Sent to Discord! ✅")
    else:
        st.error("Location not found. Please check your input.")
 