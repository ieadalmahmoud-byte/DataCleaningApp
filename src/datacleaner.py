import pandas as pd
import json
import logging
from pathlib import Path
 
class DataCleaner:
    def __init__(self, konfig_pfad):
        self.konfig_pfad = Path(konfig_pfad)
        self.konfig = self.lade_konfiguration()
        self.df = None
        
        # Professionelles Logging-Setup
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
 
    def lade_konfiguration(self):
        """Lädt die Einstellungen mit Fehlerbehandlung"""
        try:
            with open(self.konfig_pfad, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"Konfigurationsdatei nicht gefunden: {self.konfig_pfad}")
            return {}
 
    def lade_daten(self, daten_pfad):
        """Lädt die Daten und prüft, ob die Datei existiert"""
        p = Path(daten_pfad)
        if not p.exists():
            logging.error(f"Quelldatei nicht gefunden: {daten_pfad}")
            return False
        
        try:
            self.df = pd.read_csv(p)
            logging.info(f"Daten erfolgreich geladen. Zeilen: {len(self.df)}")
            return True
        except Exception as e:
            logging.error(f"Fehler beim Laden der CSV: {e}")
            return False
 
    def bereinigen(self):
        """Dynamische Bereinigung basierend auf der JSON-Konfiguration"""
        if self.df is None:
            logging.warning("Keine Daten zum Bereinigen vorhanden.")
            return
 
        # Einstellungen aus dem Bereich 'cleaner' der JSON-Datei abrufen
        cleaner_cfg = self.konfig.get("cleaner", {})
 
        if cleaner_cfg.get("drop_na", True):
            self.df.dropna(inplace=True)
            logging.info("Fehlwerte (NA) wurden erfolgreich entfernt.")
 
        if cleaner_cfg.get("drop_duplicates", True):
            self.df.drop_duplicates(inplace=True)
            logging.info("Duplikate wurden erfolgreich entfernt.")
 
    def daten_speichern(self, ausgabe_pfad):
        """Speichert die Ergebnisse und erstellt bei Bedarf den Ordner"""
        if self.df is None:
            return
 
        p = Path(ausgabe_pfad)
        p.parent.mkdir(parents=True, exist_ok=True)
        
        self.df.to_csv(p, index=False)
        logging.info(f"Bereinigte Daten wurden gespeichert unter: {p}")

 