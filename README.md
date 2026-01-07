# Data Cleaning App Professional
 
## Beschreibung
Ein modulares Python-Tool zur automatisierten Bereinigung von CSV-Datensätzen. Dieses Projekt folgt dem **App-Template** Konzept, bei dem Logik, Konfiguration und Daten strikt getrennt sind.
 
## Funktionen
- **Dynamische Bereinigung**: Entfernen von Duplikaten und fehlenden Werten (NA) basierend auf der JSON-Konfiguration.
- **Logging**: Vollständige Verfolgung des Prozesses in der Konsole.
- **Pathlib Integration**: Plattformunabhängige Pfadverwaltung.
 
## Projektstruktur
- `src/`: Enthält die `DataCleaner` Klasse.
- `config/`: JSON-Dateien für die Steuerung der Bereinigungslogik.
- `data/`: Input- und Output-Ordner für die Datenverarbeitung.
- `app.py`: Der Haupteinstiegspunkt der Anwendung.
 
## Bedienung
1. Legen Sie Ihre CSV-Datei in `data/input/` ab.
2. Passen Sie die `config/config.json` an.
3. Starten Sie die Anwendung mit:
   ```bash
   python app.py
 
