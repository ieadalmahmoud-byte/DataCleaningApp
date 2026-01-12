import pandas as pd
import matplotlib.pyplot as plt
 
# 1. قراءة البيانات من الملف الذي أنشأته سابقاً
try:
    # نقوم بتحديد أسماء الأعمدة لأن  الحالي قد لا يحتوي على العناوين
    df = pd.read_csv('weather_data.csv', names=['Stadt', 'Temperatur', 'Wetter'])
    
    # 2. إعداد الرسم البياني
    plt.figure(figsize=(10, 6))
    
    # رسم خط يمثل درجات الحرارة
    plt.plot(df['Temperatur'], marker='o', linestyle='-', color='b', label='Temperatur (°C)')
    
    # 3. تزيين الرسم البياني (التنسيق)
    plt.title('Temperaturverlauf in Berlin (Mitte)', fontsize=14)
    plt.xlabel('Messungen (Anzahl)', fontsize=12)
    plt.ylabel('Temperatur in °C', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # إضافة نص يوضح حالة الطقس لكل نقطة
    for i, txt in enumerate(df['Wetter']):
        plt.annotate(txt, (i, df['Temperatur'][i]), textcoords="offset points", xytext=(0,10), ha='center')
 
    # 4. عرض الرسم
    print("Generiere Graph...")
    plt.show()
 
except FileNotFoundError:
    print("Fehler: Die Datei weather_data.csv wurde nicht gefunden. Bitte lasse das Hauptskript zuerst laufen.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
plt.show
 