# Informationen an ein Programm zurückliefern

Im letzten Abschnitt haben wir Parameter eingeführt. Mit Parametern konnten wir Funktionen Informationen mitgeben, mit denen sie dann arbeiten konnten. Unsere Programme haben ihre Ergebnisse aber immernoch in Textform ausgegeben.

Ziehen wir eine Bilanz zum Schaltjahrprogramm:
- ~~Die Eingabe der Jahreszahl erfolgte über die Tastatur nach Starten des Programms.~~
- [x] Die Jahreszahl wird als Parameter übergeben.
- Zur Kontrolle wurde die Jahreszahl auch wieder ausgegeben.
- Außerdem erfolgt die Rückmeldung des Programms in Textform ("Schaltjahr!" oder "Kein Schaltjahr!").

Der Zweite Punkt, die Ausgabe zur Kontrolle, kann ohne weiteres weggelassen werden, aber wir benötigen noch eine Möglichkeit, eine Rückmeldung an das Programm zurückzuliefern!

# Rückgabewerte für Methoden

Betrachten wir wieder unser einfaches Summen-Beispiel:

```python
def addiere(x, y):
    summe = x + y
    print(summe)
```

Hier könnten wir uns wünschen, das Ergebnis der Summe weiter zu verwenden, zum Beispiel um eine weitere Zahl zu addieren. Wir können das mit dem Schlüsselwort `return` möglich machen:

```python
def addiere(x, y):
    summe = x + y
    return summe
```

Der englische Begriff "return" kann hier auf zwei Arten ins Deutsche übersetzt werden:

- "zurückkehren": Führt der Computer gerade eine Funktion aus und erreicht eine Zeile, in der return steht, kehrt der Computer zurück an die Stelle, an der die Funktion aufgerufen wurde. Das bedeutet, dass **Code in Zeilen nach return nicht mehr ausgeführt wird**!
- "zurückgeben": Der Ausdruck, der nach `return` in derselben Zeile steht, wird zum Rückgabe wert der Funktion.

Letzteres ist genau die Funktionalität, die wir uns gewünscht haben! Mach dich in der nächsten Codebox mit der Verwendung von Rückgabewerten vertraut:

```python runnable
def addiere(x, y):
    summe = x + y
    return summe
# schreibt den Rückgabewert in die Variable zahl
zahl = addiere(1,2)
print(zahl)
# Verwendet die Variable zahl als Parameter
zahl2 = addiere(zahl, zahl)
print(zahl2)
# Verwendet "direkt" den Rückgabewert als Parameter für print()
print(addiere(5,7))
# Verschachteln von Funktionen:
print(addiere(1, addiere(2, 3)))
```

?[Welche Aussagen zu Rückgabewerten sind wahr?]
- [x] Der Rückgabewert einer Methode steht nach dem Schlüsselwort "return"
- [ ] Ich muss Rückgabewerte in Variablen speichern, um sie weiterverwenden zu können.
- [x] Funktionen können ineinander geschachtelt werden, sodass der Rückgabewert der einen Funktion als Parameter der nächsten Funktion zum Einsatz kommt.

## Aufgabe: Subtraktion implementieren 2.0

Definiere in der nachfolgenden Code-Box eine Funktion `subtrahiere()`, die zwei Parameter erhält und die Differenz der beiden Parameter als Rückgabewert zurückliefert. Aufrufbeispiel:

```python
subtrahiere(1, 2)
# gibt nichts aus!
differenz = subtrahiere(1,2)
# differenz == 1-2 == -1
print(differenz)
# gibt -1 aus
```

@[Subtrahieren mit Rückgabewert]({"stubs": ["subtrahiere2.py"], "command": "python3 test_subtrahiere2.py", "project": "python"})

## Anwendung auf die Schaltjahre

Nun wollen wir unser Schaltjahrbeispiel so umbauen, dass die Methode `JahreszahlPruefen()` nicht nur einen Parameter erhält, in dem das zu prüfende Jahr steht, sondern auch noch einen Wahrheitswert zurückgibt. Handelt es sich um ein Schaltjahr, soll `True` zurückgegeben werden, andernfalls `False`. Mögliche Aufrufe sollen so aussehen:

```python
schaltjahr = JahreszahlPruefen(1998)
# schreibt False in schaltjahr
schaltjahr = JahreszahlPruefen(2000)
# schreibt True in schaltjahr
```

**Hinweis**: Rückgabewerte abhängig von Bedingungen können mit `if` zum Beispiel so umgesetzt werden:

```python
if bedingung:
    return False
else:
    return True
```

@[Schaltjahr? Rückgabewert als Boolean erhalten]({"stubs": ["schaltjahrReturn.py"], "command": "python3 test_schaltjahrReturn.py", "project": "python"})

## Kontrollfragen zu Rückgabewerten:

?[Rückgabewerte ...]
- [x] dienen dazu Programmen zu ermöglichen, mit einander zu interagieren und Ergebnisse von Funktionen weiter zu verwenden.
- [ ] sind ein Ersatz für Rücklaufzettel an Elternbriefen.
- [x] können entweder direkt verwendet werden, oder in einer Variable zwischengespeichert werden.

?[Welcher der folgenden Codeabschnitte nutzt den Rückgabewert von addiere() korrekt?]
- [ ] A
- [ ] B
- [x] C
- [ ] D
- [x] E


```python
# Abschnitt A:
addiere(2, 5)
print(summe)

# Abschnitt B:
addiere(2, 5)
print(addiere)

# Abschnitt C:
summe = addiere(2,5)
print(summe)

# Abschnitt D:
print(addiere)(2, 5)

# Abschnitt E:
print(addiere(2,5))
```

