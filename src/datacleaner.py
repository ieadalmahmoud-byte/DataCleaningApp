import pandas as pd
import json
import logging
from pathlib import Path
 
class DataCleaner:
    def __init__(self, config_path):
        self.config_path = Path(config_path)
        self.config = self.load_config()
        self.df = None
        
        # إعداد نظام التسجيل (Logging)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
 
    def load_config(self):
        """تحميل إعدادات JSON"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Fehler beim Laden der Konfiguration: {e}")
            return {}
 
    def load_data(self, data_path):
        """تحميل ملف البيانات CSV"""
        try:
            self.df = pd.read_csv(Path(data_path))
            logging.info(f"Daten geladen. Zeilen: {self.df.shape[0]}")
        except Exception as e:
            logging.error(f"Fehler beim Laden der Daten: {e}")
 
    def clean(self):
        """تنفيذ عمليات التنظيف بناءً على الإعدادات"""
        if self.df is None: return
 
        cleaner_cfg = self.config.get("cleaner", {})
 
        # حذف القيم المفقودة
        if cleaner_cfg.get("drop_na"):
            self.df.dropna(inplace=True)
            logging.info("Fehlwerte entfernt.")
 
        # حذف التكرارات
        if cleaner_cfg.get("drop_duplicates"):
            self.df.drop_duplicates(inplace=True)
            logging.info("Duplikate entfernt.")
 
        # حذف الأعمدة غير المطلوبة
        cols_to_remove = cleaner_cfg.get("columns_to_remove", [])
        self.df.drop(columns=[c for c in cols_to_remove if c in self.df.columns], inplace=True)
        
        logging.info(f"Bereinigung abgeschlossen. Verbleibende Zeilen: {self.df.shape[0]}")
 
    def save_data(self, output_path):
        """حفظ البيانات المنظفة"""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(output_path, index=False)
        logging.info(f"Bereinigte Daten gespeichert unter: {output_path}")

 