# fapello
### Beskrivning av Skriptet för Nedladdning av Media från Specifika Webbplatser

Detta Python-skript är designat för att automatisera processen att hämta mediafiler, inklusive bilder och videoklipp, från specifikt angivna webbsidor. Skriptet är utformat för att fungera med webbplatser där mediafiler är ordnade på ett förutsägbart sätt, vilket möjliggör automatiserad skrapning och nedladdning baserat på sidans struktur.

#### Funktioner

- **Automatisk upptäckt och nedladdning av bilder:** Skriptet besöker angivna webbsidor och laddar automatiskt ner alla bilder som hittas på dessa sidor. Det ignorerar explicit tumnagelbilder för att säkerställa att endast fullstorleksbilder laddas ner.
  
- **Upptäckt och nedladdning av videoklipp:** Förutom bilder, identifierar skriptet även sidor som innehåller videoklipp genom att söka efter specifika HTML-element som indikerar närvaron av en video. När en sådan sida hittas, extraherar skriptet videoklippets URL och laddar ner filen.

- **Dynamisk mapphantering:** För varje URL som processas skapar skriptet en dedikerad mapp baserat på sidans namn. Detta organiserar nedladdade mediafiler på ett snyggt sätt och gör det enkelt att hålla reda på innehållet från olika källor.

- **Enkel konfiguration:** Användare kan enkelt ange vilka webbsidor som ska skrapas genom att lägga till URL:erna i en textfil. Skriptet läser sedan denna fil och utför nedladdningsprocessen automatiskt.

#### Användning

1. **Förbered en textfil:** Skapa en textfil (`urls.txt`) och lägg till de fullständiga URL:erna för de sidor du vill skrapa, en URL per rad.
2. **Konfigurera skriptet:** Se till att skriptets konfigurationsdel är korrekt inställd för att matcha den specifika webbplatsens struktur du siktar på.
3. **Kör skriptet:** Starta skriptet från kommandoraden eller terminalen och följ instruktionerna för att ange sökvägen till din textfil när du uppmanas.

#### Krav

- Python 3.x
- Externa bibliotek: `requests` för HTTP-anrop, `beautifulsoup4` för HTML-skrapning. Dessa kan installeras via pip:
  ```
  pip install requests beautifulsoup4
  ```

#### Notering

Detta skript är avsett att användas på ett ansvarsfullt sätt för att respektera webbplatsernas användarvillkor och begränsningar. Användning av skriptet för massnedladdning eller skrapning av innehåll utan tillstånd från webbplatsägaren rekommenderas inte och kan strida mot lagar eller regler. Användare uppmanas att kontrollera webbplatsens policyer innan skriptet används.
