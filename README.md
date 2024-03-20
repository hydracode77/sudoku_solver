# Sudoku Solver
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/1024px-Sudoku-by-L2G-20050714.svg.png" alt="Sudoku_Bild" width="200" height="200">

## Was ist "Sodoku"?
[Wikipedia - Sudoku](https://de.wikipedia.org/wiki/Sudoku)

## Was hab ich programmiert?
Ein Projekt zum Lösen von einfachen Sudoku-Problemen.
Die Zahlen werden manuell eingetragen, Null steht hierbei für ein Leeres Feld. Anschließend wird das Programm gestartet und der Algorythmus findet passende Zahlen, füllt damit die Lücken und stellt das Sudoku bestmöglich fertig.

## So funtioniert der Algorythmus:
- Das Sudoku wird in 3 verschiedenen Listen gespeichert, die Reihen, Spalten und Boxen als Unterlisten haben
- Jedes dieser Listen wird fehlende Stellen überprüft. Gibt es eine Unterliste die nur eine fehlende Stelle hat, wird diese berechnet.
- Alle 3 Listen werden mit den neu gewonnen Ergebnissen in ein einheitliches Format gebracht und verglichen. Daraus entsteht dann eine neue Liste, die alle neu berechneten Stellen enthält.
Dieser Prozess wird so oft wiederholt, bis es nicht mehr möglich ist, neue Stellen zu berechnen.

## Ausstehende Verbesserungsmöglichkeiten:
- Automatisches Hinzufügen eines Sudoku Feldes
- Komplexere Sudokus bearbeitbar machen
