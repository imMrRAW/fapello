# Fapello Downloader

## Beskrivning
Det här Python-skriptet är utformat för att ladda ner bilder och videor från användares sidor på fapello.com. Skriptet läser in en lista med URL:er från en fil `urls.txt` och laddar ner alla tillgängliga bilder och upp till 50 videor från varje användares sida.

## Användning
1. Lägg till önskade URL:er till användarsidor på fapello.com i filen `urls.txt`, en URL per rad.
2. Kör `Fapello.py`.
3. Skriptet skapar en mapp för varje användare och laddar ner bilderna och upp till 50 videor till respektive mapp.

## Förutsättningar
- Python 3.x
- Bibliotek: requests, tqdm

## Installation av beroenden
```
pip install -r requirements.txt
```

## Konfiguration
Ingen konfiguration krävs. Se till att ha en fil `urls.txt` med önskade URL:er till användarsidor på fapello.com.

## Struktur
```
.
├── main.py
├── README.md
├── requirements.txt
├── urls.txt
└── Downloads/
```

- `Fapello.py`: Huvudskriptet för nedladdning av bilder och videor.
- `README.md`: Den här filen, innehåller beskrivning och instruktioner för projektet.
- `requirements.txt`: Lista över Python-bibliotek som krävs.
- `urls.txt`: Filen med URL:er till användarsidor på fapello.com.
- `Downloads/`: Mappen där nedladdade bilder och videor sparas.

## Bidrag
Bidrag är välkomna! Öppna gärna en issue för att diskutera större ändringar eller skapa en pull request direkt om du har mindre ändringar att föreslå.

## Licens
Det här projektet är licensierat under [MIT licensen](LICENSE).
