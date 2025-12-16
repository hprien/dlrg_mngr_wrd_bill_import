# dlrg_mngr_wrd_bill_import
A software to import bills into the DLRG-Manager

## install
```sh
python -m venv venv
```

## run
```sh
source venv/bin/activate
python3 main.py
```

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

ISO 8859-1, leere Zeile am Ende

# abluaf
## Mitglieder exportieren
Extras / Auswertungen:
Berechtigung: `2_GR_Auswertungen`
- Alle Mitglieder nach Name
- Auswertung durchführen
- Abfrage starten
- Daten exportieren (XLSX)
- Datei öffnen

## import im DLRG-Manager
Einstellungen / Finanzen / Rechnungsimport:
Berechtigung: `2_GR_Rechnungen`
- Geschäftsbereich:
- Art der Mitgliedsnummer: "Nummernkreis - Nummer"
- Erste Spalte enthält Überschrift: "Ja"
- Trennzeichen: ";"
- Importdatei: Rechnungen Ubstadt-Weiher

## Rechnungen erstellen
Berechtigung: `2_GR_Beitragsverwaltung`
Finanzen > Beiträge / Rechnungen > Abrechnungen
- Sammellauf

## E-Mail Rechnungstemplate anpassen:
Berechtigung: `2_GR_Buchhaltung_Konfig`
Email Template in Einstellungen / Finanzen / Geschäftsbereiche

## Rechnungen per E-Mail versenden
Berechtigung: `2_GR_Beitragsverwaltung`
Finanzen > Beiträge / Rechnungen > Abrechnungen
- E-Mail Versand