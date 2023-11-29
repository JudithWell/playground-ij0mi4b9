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

Mithilfe von Parametern kann einer Funktion eine Information mitgegeben werden. Probiere es anhand des nächsten Beispiels aus!

```python runnable
def addiere(x, y):
    summe = x + y
    print(summe)

addiere(1, 3)
addiere(-1, 1)
addiere(7, 5)
addiere("Hallo", " Welt!")
```