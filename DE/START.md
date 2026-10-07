# Bildgeneratoren selbst vergleichen

## 1. Voraussetzung und Lernziel
Nutze eine schon funktionierende Bild-KI. Du lernst einen nachvollziehbaren kleinen Vergleich, keine neue Installation und keinen allgemeinen Sieger. Mehrere vorhandene Modelle sind nützlich; mit nur einem übst du Wiederholbarkeit und Fehlersuche. Für den Datei-Prüfer brauchst du vorhandenes Python3 und Pillow. Das Paket lädt und installiert nichts.

## 2. Download vollständig entpacken
Lies AUFGABEN.json, QUELLEN.md und den Prüfercode. Die vier Aufgaben behandeln Zählen, deutschen Text, räumliche Anordnung und echte Transparenz. Ein Modell ohne RGBA-Unterstützung wird bei Transparenz als nicht unterstützt dokumentiert. Ein aufgemaltes Schachbrett ist kein Alphakanal.

## 3. Erst das Ziel festlegen
Wähle genau eine Aufgabe und kopiere ihren prompt wortgleich in dein vorhandenes Werkzeug. Lege die criteria daneben. Ändere keine Begriffe, während du Kandidaten vergleichst. Mit Objekten beginnst du klein; Gesichtstreue und Schönheit sind andere Kriterien und bleiben getrennte Wertungen.

## 4. Workflow und Modell festhalten
Notiere tatsächlichen Modellnamen, Revision, Quantisierung, Workflow und Eingangsdateien. Eigene geprüfte FLUX-Installation und Workflow: https://github.com/dolmario/flux-comfyui-lokal . Eine zu deinem Modell passende Vorlage benutzen. Keine gleichnamigen Loader oder Textencoder unterschiedlicher Modellfamilien austauschen. Dieses Vergleichspaket enthält keine neue universelle Fünf-Modell-Installation.

## 5. Parameter vergleichen
Gleiche Bildgröße und derselbe Prompt erleichtern den Vergleich. Modellgerechte Schrittzahl, CFG, Sampler und Scheduler notieren. Derselbe Seed erzeugt über verschiedene Modelle hinweg weder dieselbe Startnoise noch gleiche Bilder. Distillierte Modelle brauchen andere Einstellungen als große Grundmodelle. Erzwungene identische Schritte sind nicht automatisch fair.

## 6. Vier Wiederholungen je Kandidat
Nimm zum Beispiel die Seeds11,22,33,44, wenn dein Werkzeug Seeds anbietet. Dienste ohne Seed entsprechend markieren. Erhalte auch Fehler und unpassende Ergebnisse. Nichts heimlich herausfiltern. Ein schöner Treffer aus vier Versuchen ist kein Nachweis, dass jeder Lauf stimmt.

## 7. Dateien und Zeit sichern
Speichere Originaldateien mit eindeutigen Namen. Notiere Gesamtdauer einschließlich Laden und separat einen warmen Folgelauf. Ausgabezeit, Ladezeit und Auflösung nicht vermischen. Die alten eigenen ungefähr8Sekunden oder11Minuten sind Archivbeobachtungen unter damaligen Einstellungen, keine Geschwindigkeitszusage für deinen Rechner.

## 8. Ergebnis groß anschauen
Zähle Tassen, Löffel und Äpfel einzeln. Beim Text jeden Buchstaben, Komma, Umlaut und ß prüfen. In unserem neuen Auftrag stehen wirklich ö und ß; ein alter Auftrag mit Drehzahl1500 enthielt beides gar nicht. Beim Layout die Positionen links/Mitte/rechts getrennt abhaken. Keine subjektive Schönheit als Texttreue verkaufen.

## 9. Eigenschaften messen
Mit deinem tatsächlichen gespeicherten Bild:
```powershell
python ./BILD-DATEI-PRUEFEN.py --image ./mein-bild.png --output ./mein-bild-pruefung.json
```
Der Helfer liest nur Bildgröße, Hash und Alphaeigenschaften. Er verändert kein Bild und bewertet keine Gesichter oder Buchstaben. Vorhandene Berichtdateien bleiben erhalten. Ein vorhandener Alphakanal, der überall255ist, hat keine transparenten Pixel. Nichtdeckende Pixel beweisen wiederum nicht automatisch, dass das Motiv sauber ausgeschnitten ist.

## 10. Protokoll ausfüllen
DEIN-VERGLEICH.csv hat getrennte Felder für Kriterien, Geschmack, Fehler, echte Datei, Zeit und Parameter. Markiere fehlende Unterstützung, abgebrochene Läufe und fehlende Dateien ausdrücklich. Unser tatsächlicher Prüfer-Test verwendet Autor-Testbilder und ist keine neue Modellmessung. Fremde API-ok-Meldungen ersetzen weder Bildprüfung noch echte Datei.

## 11. Lokal und Cloud unterscheiden
Lokale Gewichte können ohne Cloudinferenz laufen, sofern auch Nodes und Encoder lokal bleiben. Ein angeblich lokaler Workflow kann trotzdem einen entfernten Encoder ansprechen. Private Fotos nicht ungeprüft an Dienste geben. Cloudbilder haben dienstabhängige Bedingungen; lokal ist ebenfalls keine pauschale Zusage für Lizenz, Filterfreiheit oder fehlende Wasserzeichen.

## 12. Deine Auswahl begründen
Entscheide für deine konkrete Aufgabe: korrekter Text, Zählen, Geschwindigkeit unter deinen Einstellungen oder Bildwirkung. Mit vier kleinen Aufgaben folgt keine universelle Modellrangliste. Lies aktuelle Quellen für deine genaue Modellversion. Eigene ältere Qwen-, FLUX-, Klein- und Cloud-Bilder bleiben Archivbeispiele; dieses Paket behauptet keine heute neu ausgeführten sechs Modellläufe.
