import logging
from src.datacleaner import DataCleaner
 
def main():
    # 1. تحديد المسارات (Paths)
    config_file = "./config/config.json"
    input_data = "./data/input/my_data.csv"
    output_data = "./data/output/cleaned_data.csv"
 
    # 2. إنشاء كائن المنظف
    cleaner = DataCleaner(config_file)
 
    # 3. تشغيل العمليات
    cleaner.load_data(input_data)
    cleaner.clean()
    cleaner.save_data(output_data)
 
    print("--- Prozess erfolgreich beendet ---")
 
if __name__ == "__main__":
    main()
 