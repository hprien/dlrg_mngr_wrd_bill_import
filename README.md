# dlrg_mngr_wrd_bill_import
A software to import bills into the DLRG-Manager

## install
```sh
python -m venv venv
source venv/bin/activate
```

# usage
## Bekleidung.csv
This file has the following structure:
```csv
Vorname;Name;Artikelnummer;Artikel;Normalpreis;Zuschuss;Preis (tatsächlich);Anzahl;Größe;Link (nicht notwendig für Bestellung);;Summe
```
## Mailadressen.csv
This file contains the E-Mail addresses for each person:
```csv
Vorname,Name,E- Mail
```
## mitglieder.csv
This file contains all members of the DLRG-Ubstadt-Weiher:
```csv
Nr. (Nummernkreismgr.),Firma,Anrede - Privatperson,Titel,Nachname - Privatperson,Vorname - Privatperson,Straße,PLZ,Ort,Telefon,Telefon 2,Mobil,Telefax,E-Mail (primär),Geburtsdatum,Eintritt,Austritt,Kündigung,Status,Hauptkategorie,Indiv. Nr.,Individuelle Briefanrede,Zahlungsmodus,Rechnungsausgabe,Bemerkung,Familien-Nr
```
## DLRG-Manager Mitglieder export
Extras / Auswertungen (Berechtigung: `2_GR_Auswertungen`):
- Alle Mitglieder nach Name
- Auswertung durchführen
- Abfrage starten
- Daten exportieren (XLSX)
- Datei öffnen
## run script
In the first lines of main.py some configurations need to be done
```sh
python3 main.py
```
## import im DLRG-Manager
Einstellungen / Finanzen / Rechnungsimport (Berechtigung: `2_GR_Rechnungen`):
- Geschäftsbereich:
- Art der Mitgliedsnummer: "Nummernkreis - Nummer"
- Erste Spalte enthält Überschrift: "Ja"
- Trennzeichen: ";"
- Importdatei: Rechnungen Ubstadt-Weiher

## Rechnungen erstellen
Finanzen > Beiträge / Rechnungen > Abrechnungen (Berechtigung: `2_GR_Beitragsverwaltung`):
- Sammellauf

## E-Mail Rechnungstemplate anpassen:
Email Template in Einstellungen / Finanzen / Geschäftsbereiche (Berechtigung: `2_GR_Buchhaltung_Konfig`)

## Rechnungen per E-Mail versenden
Finanzen > Beiträge / Rechnungen > Abrechnungen (Berechtigung: `2_GR_Beitragsverwaltung`):
- E-Mail Versand

# Buchhaltungsdaten
## Standard Kontorahmen 42 (Vereine, Stiftungen, gGmbH) Sphären:
- 01 (Jugend)
- 31 (Ausbildung, Einsatz)
## Buchhaltungskonten:
### Stammverbank
- 40900 - Umsatzerlöse (z.B. Wachdienstbekleidung)
- 42030 - Erlöse aus Teilnehmer-/Nutzungsgebühren
### Jugend
- 40905 - Umsatzerlöse (z.B. Wachdienstbekleidung)
- 42035 - Erlöse aus Teilnehmer-/Nutzungsgebühren