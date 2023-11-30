# Mensch oder Computer?

Wann immer wir ein Programm schreiben, ist es wichtig zu berücksichtigen, wer oder was dieses Programm verwenden wird: ein Mensch oder der Computer.

Die Vorlage zum Schaltjahr war auf die Bedienung von Menschen zugeschnitten:
- Die Eingabe der Jahreszahl erfolgte über die Tastatur nach Starten des Programms.
- Zur Kontrolle wurde die Jahreszahl auch wieder ausgegeben.
- Außerdem erfolgt die Rückmeldung des Programms in Textform ("Schaltjahr!" oder "Kein Schaltjahr!").

Das **Ziel** der heutigen Stunde soll sein, ein Programm zu schreiben, das eine Liste von Jahreszahlen erhält und mit einer Liste an Wahrheitswerten (Boolean) antwortet. Ist die i-te Zahl ein Schaltjahr, so soll der i-te Eintrag der Ergebnisliste True sein.

Aber eins nach dem anderen!

# Methoden Informationen mitgeben

Betrachten wir die von Python zur Verfügung gestellte Funktion `print()`. Diese können wir verwenden, um Textausgaben zu machen. Damit der Computer weiß, was ausgegeben werden soll, muss die entsprechende Zeichenkette an die Methode übergeben werden, dafür schreiben wir sie in die Klammern hinter `print`:

```python
print("test")
print("Hallo!")
print("Baum.")
```

Wir erhalten also **unterschiedliche** Ergebnisse beim Aufruf **derselben** Funktion - abhängig davon, was in den Klammern steht. 

Wir nennen "das was in den Klammern steht" **Methodenparameter**, **Funktionsparameter** oder einfach nur **Parameter**.

Mithilfe von Parametern kann einer Funktion eine Information (oder auch mehrere Informationen) mitgegeben werden. Eine Funktion kann beliebig viele, mit Komma getrennte Parameter haben. Eine Funktion zum Bilden der Summe zweier Zahlen könnte so aussehen:

```python runnable
def addiere(x, y):
    summe = x + y
    print(summe)

addiere(1, 3)
addiere(-1, 1)
addiere(7, 5)
addiere("Hallo", " Welt!")
```

?[Welche Aussagen zu Parametern sind wahr?]
- [x] In der Methodendefinition stehen die Namen der Parameter in Klammern hinter dem Methodennamen.
- [x] Parameter kann ich in Methoden genauso verwenden, wie Variablen.
- [x] Funktionenparameter werden verwendet, um mit derselben Funktion unterschiedliche Probleme zu lösen.

## Aufgabe: Subtraktion implementieren

Definiere in der nachfolgenden Code-Box eine Funktion `subtrahiere()`, die zwei Parameter erhält und die Differenz der beiden Parameter mit `print()` ausgibt. Bitte gib **nur das Ergebnis** ohne weiteren Text aus! Aufrufbeispiel:

```python
subtrahiere(1, 2)
# gibt -1 aus
```

@[Subtrahieren]({"stubs": ["subtrahiere.py"], "command": "python3 test_subtrahiere.py", "project": "python"})

## Anwendung aufs Schaltjahr

Nun wollen wir unser Schaltjahrbeispiel so umbauen, dass die Methode `JahreszahlPruefen()` einen Parameter erhält, in dem das zu prüfende Jahr steht. Mögliche Aufrufe sollen so aussehen:

```python
JahreszahlPruefen(1998)
# gibt "Kein Schaltjahr!" aus
JahreszahlPruefen(2000)
# gibt "Schaltjahr!" aus
```

@[Jahreszahl als Parameter mitgeben]({"stubs": ["schaltjahrParam.py"], "command": "python3 test_schaltjahrParam.py", "project": "python"})

## Kontrollfragen zu Parametern

?[Welche der folgenden Funktionen verwenden Parameter (sinnvoll)?]
- [x] funktionA
- [ ] funktionB
- [ ] funktionC
- [x] funktionD
```python
def funktionA(parameter):
    funktion2(parameter)
def funktionB():
    funktion2(parameter)
def funktionC(parameter):
    funktion2(baum)
def funktionD(parameter1, parameter2):
    funktionD(parameter1, parameter1 + parameter2)
```

?[Wir benötigen Parameter ...]
- [x] um mit einzelnen Funktionen viele unterschiedliche ähnliche Dinge zu tun (z.B. print("A") und print("B"))
- [ ] eigentlich gar nicht, sie sind nur dazu da, uns das Leben schwer zu machen.
- [x] um Informationen von außerhalb einer Funktion in der Funktion verwenden zu können.

?[Was stimmt bei Parametern und Funktionen:]
- [ ] Wenn ich eine Funktion `fun()` aufrufe, die einen Parameter mit dem Namen `zahl` hat, dann muss der Aufruf `fun(zahl)` sein.
- [x] Wenn ich eine Funktion `fun()` definieren will, die einen Parameter mit dem Namen `zahl` hat, dann schreibe ich `def fun(zahl):` usw.
- [x] Wenn ich eine Variable `buchstabe = "a"` definiert habe, und sie an eine Funktion `def fun(zahl): ...` als Parameter übergeben will, dann schreibe ich zum Aufrufen der Funktion `fun(buchstabe)`.
- [ ] Wenn ich eine Variable `buchstabe = "a"` als Parameter an eine Funktion `fun(...)` übergeben will, dann muss die Funktion so definiert sein: `def fun(buchstabe): ...`