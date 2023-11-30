# Rückblick: Listen iterieren

In der letzten Lerneinheit haben wir **Listen** kennengelernt. Außerdem haben wir zwei Möglichkeiten behandelt, Listen zu durchlaufen, das heißt eine bestimmte Folge von Anweisungen für jedes Listenelement auszuführen.

**Möglichkeit 1: Iteration über den Index der Elemente**

Hierbei nutzen wir die Funktion `len()` (von englisch "length") um die Länge der Liste zu ermitteln und entsprechend oft die Wiederholung ausführen zu lassen:

```python runnable
liste = [1, 2, 3, 4, 7, 9, 12]

for index in range(len(liste)):
    # Referenzieren eines Elements über seinen index:
    # Das Element an der Stelle index wird an print() übergeben
    print(liste[index])
```

**Möglichkeit 1: Iteration über die Elemente ohne Index**

Man liest: "Für jeden `eintrag` in `liste`: gib den Eintrag aus."

```python runnable
liste = [1, 2, 3, 4, 7, 9, 12]

for eintrag in liste:
    # Referenzieren des Elements durch die Laufvariable der Wiederholung.
    print(eintrag)
```

# Funktionen auf Listenelemente anwenden

In dieser Weise können wir z.B. die Elemente beliebiger Listen mit unserer Funktion `addiere()` addieren:

```python runnable
def addiere(x, y):
    summe = x + y
    return summe

liste = [1, 2, 4, 7]
summe = 0

for eintrag in liste:
    summe = addiere(eintrag, summe)

print(summe)
# gibt 14 aus.
```

Als kleine Übung wollen wir die Summenbildung wie oben (Zeile 6 bis 9) in einer eigenen Funktion `addiereListe()` unterbringen. 
Die Funktion soll die Liste mit Werten im Parameter `liste` erhalten und gibt die Summe wieder zurückgeben:

**Hinweis**: Hier ist die Rückgabe mit `return` und nicht die Ausgabe mit `print()` gemeint.

@[Listen addieren]({"stubs": ["addiereListe.py"], "command": "python3 test_addiereListe.py", "project": "python"})

# Listen zurückgeben

In manchen Situationen sollen Funktionen nicht einzelne Werte, sondern Listen zurückliefern. Betrachten wir zum Beispiel die Funktion `positiveZahlen()` wie unten:

```python
liste = [1, 2, 3, -1, -2, -3, 5]
positiv = positiveZahlen(liste)
# positiv == [1, 2, 3, 5]
positiv = positiveZahlen([5, -5, 7, 0])
# positiv == [5, 7]
```

**Anmerkung zum zweiten Beispiel**: Um eine Liste an eine Funktion zu übergeben, muss sie nicht in eine Variable gespeichert werden, sondern kann auch direkt "am Platz des Parameters" mit den eckigen Klammern initialisiert werden.

?[Die Funktion `positiveZahlen()` ...]
- [ ] ... wandelt alle Einträge der übergebenen Liste in positive Zahlen um.
- [x] ... erhält eine Liste als Parameter.
- [x] ... liefert eine Liste als Rückgabewert.
- [ ] ... kann auch eine Liste zurückliefern, die 0 enthält.
- [x] ... liefert nur die Zahlen aus der Liste zurück, die positiv sind.

Implementiere im folgenden Block die oben beschriebene Funktion `positiveZahlen()`!

::: Hinweise, falls du nicht weiter weißt
- Durchlaufe die Liste mit `for element in liste:` oder ähnlichem.
- Überprüfe ob das Element größer ist als 0 (`element > 0`).
- Wenn das der Fall ist (`if`), füge das Element der `positivListe` hinzu
- Anhängen an die Liste mit `positivListe.append(element)`
:::

@[Implementiere die Funktion positiveZahlen()!]({"stubs": ["positiveZahlen.py"], "command": "python3 test_positiveZahlen.py", "project": "python"})

# Schaltjahreslisten prüfen

Zu allerletzt wollen wir in diesem Abschnitt unser Schaltjahresbeispiel vollenden.
Wir erinnern uns an das zuvor gesteckte Ziel:

> Das **Ziel** der heutigen Stunde soll sein, ein Programm zu schreiben, das eine Liste von Jahreszahlen erhält und mit einer Liste an Wahrheitswerten (Boolean) antwortet. Ist die i-te Zahl ein Schaltjahr, so soll der i-te Eintrag der Ergebnisliste True sein.

Wir haben nun alle dafür notwendigen Grundlagen erlernt und können jetzt dieses Programm implementieren.
Das erwartete Verhalten ist wie folgt:

```python
ergebnis = JahreszahlListePruefen([1998, 2000, 2100])
# ergebnis == [False, True, False]
```

**Tipp**: Füge zunächst deine Funktion `JahreszahlPruefen()` von vorher ein, die eine einzelne Jahreszahl prüft. Rufe dann in `JahreszahlListePruefen()` für jedes Listenelement `JahreszahlPruefen()` auf und sammele die Ergebnisse (`True` oder `False`) in einer Ergebnisliste, die du dann ausgibst.

@[Überprüfe eine Liste von Jahreszahlen!]({"stubs": ["schaltjahrListe.py"], "command": "python3 test_schaltjahrListe.py", "project": "python"})


