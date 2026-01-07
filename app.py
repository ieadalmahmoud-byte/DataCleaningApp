from src.datacleaner import DataCleaner
 
def main():
    konfig_p = "./config/config.json"
    eingabe_p = "./data/input/my_data.csv"
    ausgabe_p = "./data/output/bereinigte_daten.csv"
 
    cleaner = DataCleaner(konfig_p)
    
    if cleaner.lade_daten(eingabe_p):
        cleaner.bereinigen()
        cleaner.daten_speichern(ausgabe_p)
        print("--- Prozess erfolgreich abgeschlossen ---")
 
if __name__ == "__main__":
    main()
 