[![PyPi version](https://img.shields.io/pypi/v/html2json.svg)](https://pypi.python.org/pypi/html2json/)
[![PyPi pyversions](https://img.shields.io/pypi/pyversions/html2json.svg)](https://pypi.python.org/pypi/html2json/)
[![PyPi license](https://img.shields.io/pypi/l/html2json.svg)](https://pypi.python.org/pypi/html2json/)

# duden_search

_Kleines Kommandozeilenprogramm zum Nachschlagen von Wörtern aus dem Duden-Wörterbuch._

![Alt Text](6eab6b364c.gif)

## Ziele:

* Erkundung des Playwright-Tool mit seiner Python-API für Web-Browsing und Web-Scraping mit dem BeautifulSoup-Tool. 
* Erstellung einen Bot, der auf die Seite www.duden.de zugreift und in der Lage ist, die Informationen zu einem vom Autor angegebenen Wort herunterzuladen und zu suchen und die Informationen als Rich Text im JSON-Format herunterzuladen.
* All dies sollte mit Code, der in Python geschrieben und für die Implementierung oder Erweiterung durch andere Programmierer dokumentiert ist. 

## Environment

Für die Reproduktion der Python-Umgebung, mit der ich dieses Tool ausgeführt habe, habe ich die Datei requirements.txt zur Verfügung gestellt, die von diesem Repository heruntergeladen werden kann. 
Es ist möglich, dass weniger Bibliotheken und "Dependencies" benötigt werden als in der requirements.txt beschrieben. Verwenden Sie pip oder conda, um die Abhängigkeiten zu finden, die Sie für diese Aufgabe benötigen.
Nachfolgend finden Sie eine Liste der Bibliotheken für die Anwendung main.py sowohl von der Standard-Python-Bibliothek als auch von Drittanbieter-Bibliotheken. 

* Playwright https://playwright.dev/
* Beautiful soup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* Pytest https://docs.pytest.org/en/7.1.x/
* Request  https://docs.python-requests.org/en/latest/

## Usage
Die nächste Codezeile dient zum Nachschlagen des Wortes "Wort" im Duden und zum Speichern der Definitionen im CSV-Format und der HTML-Seite im JSON-Format. 
Die Animation zeigt, wie man die Hilfe abfragt, um die vom CLI benötigten Parameter zu sehen, sowie ein Beispiel für die erwartete Ausgabe für das Wort "Bagger". 
```
>python main.py -h -iw Wort -oj Wort.json -oc Wort.csv
```
![Alt Text](usage.gif)

## Test-Politik

Pytest wird als Paket zum Testen verwendet. Einige Eckfälle wurden nicht bewertet, insbesondere bei der Verwendung des Playwright-Selektors für einige Tags im Html-Dokument sowie für den Html-zu-Json-Parser. 
Um die Tests auszuführen, geben Sie einfach in die Befehlskonsole ```pytest``` ein. Fügen Sie das Flag -v hinzu, um mehr Details über fehlgeschlagene Fälle zu erhalten.

## Enwickler

<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
</svg>

![Alt text](https://raw.github.com/potherca-blog/StackOverflow/master/question.13808020.include-an-svg-hosted-on-github-in-markdown/controllers_brief.svg