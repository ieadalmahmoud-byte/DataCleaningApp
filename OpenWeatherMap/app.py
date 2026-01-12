import streamlit as st
import requests
from discord_webhook import DiscordWebhook
from API_KEY import MY_SECRET_KEY
 
# 1. Page Configuration
st.set_page_config(page_title="Wetter Alert", layout="centered")
st.title("☀️ Berlin Wetter & Discord")
 
# 2. API Data Fetch
def get_weather():
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat=52.52&lon=13.40&appid={MY_SECRET_KEY}&units=metric&lang=de"
        return requests.get(url).json()
    except:
        return None
 
data = get_weather()
 
# 3. Display Data
if data:
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    st.info(f"Aktuelles Wetter: {temp}°C, {desc}")
 
    # Discord Webhook URL
    WEBHOOK_URL = "https://discordapp.com/api/webhooks/1460250874302566571/zM4x1I-tiZYX12KCiQb3sTNfBioIFcjDEZnWhDZrSaMRE9Edy4vifjcFSvR"
 
    st.markdown("---")
    # 4. Der Button
    if st.button('🚀 Alarm an Discord senden'):
        msg = f"📢 Wetter-Update Berlin: {temp}°C, Status: {desc}"
        webhook = DiscordWebhook(url=WEBHOOK_URL, content=msg)
        webhook.execute()
        st.success("✅ Nachricht an Discord gesendet!")
else:
    st.error("API-Verbindungsfehler!")
 