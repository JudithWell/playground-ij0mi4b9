# Schaltjahre

Als Hausaufgabe habt ihr ein Python-Programm erarbeitet, das eine Jahreszahl einliest und anschließend ausgibt, ob es sich dabei um eine Jahreszahl handelt. Die folgenden Bedingungen bestimmen, ob ein Jahr ein Schaltjahr ist:

- Ist die Jahreszahl durch 4 teilbar, handelt es sich um ein Schaltjahr, außer ...
- ... die Jahreszahl ist auch durch 100 teilbar. Dann handelt es sich um kein Schaltjahr außer ...
- ... die Jahreszahl ist durch 400 teilbar, dann handelt es sich um ein Schaltjahr.

Die folgende Codevorlage war vorgegeben, wobei hier nur die **erste Regel** umgesetzt wird:

```python runnable
def istTeilerVon(teiler, zahl):
    """
    Prüft, ob zahl durch teiler teilbar ist.
    Z.B. liefert teilt(2, 4) True zurück.
    """
    return ((zahl % teiler) == 0)


def JahreszahlEingebenUndPruefen():
    
    aktuelleEingabe = input("Bitte Jahreszahl eingeben.  ")
    jahr = int(aktuelleEingabe)
    
    print("Jahreszahl: " + str(jahr)) 
    
    if istTeilerVon(4, jahr):
        print("Schaltjahr!")
    else:
        print("Kein Schaltjahr!")


JahreszahlEingebenUndPruefen()
```

Ergänzt nun im folgenden Feld eure Umsetzung der Schaltjahr-Aufgabe:





