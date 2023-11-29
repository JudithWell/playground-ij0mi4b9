# Bonus 1: Schaltjahrlisten zurückgeben

Als Zusatzaufgabe habt ihr hier die Gelegenheit, das Schaltjahrsbeispiel komplexer zu bauen: Nun soll nämlich eine Liste von Jahreszahlen als Parameter übergeben werden und eine Liste der Schaltjahre aus dieser Liste zurückgegeben werden.

**Achtung: Da es sich um eine Bonusaufgabe handelt, gibt es hier keine automatische Korrektur. Bastle dir selbst Testfälle wie unten z.B. mit `print()`, um deinen Code auf korrekte Funktion zu prüfen.**

```python runnable
def istTeilerVon(teiler, zahl):
    """
    Prüft, ob zahl durch teiler teilbar ist.
    Z.B. liefert istTeilerVon(2, 4) True zurück.
    """
    return ((zahl % teiler) == 0)

'''
Ergänze unten deine Methode JahreszahlPruefen() aus den vorherigen Aufgaben.
Rückgabe: True wenn die übergebene Zahl ein Schaltjahr ist.
'''
def JahreszahlPruefen(jahr):
    
    


    
    return True

''' 
Ergänze hier nun die Methode JahreszahlListePruefen().
Es wird eine Liste der Schaltjahre aus liste zurückgegeben.
'''
def JahreszahlListePruefen(liste):
    
    
    
    
    
    


    return

# Testaufruf:
print(JahreszahlListePruefen([2000, 2004, 2100, 2023]))
# sollte [2000, 2004] zurückgeben.
# TODO: Mindestens 3 Testfälle ergänzen.


```

# Bonus 2: Schaltjahre aus einer bestimmten Zeitspanne

Eine weitere mögliche Anforderung wäre, dass wir alle Schaltjahre nicht aus einer gegebenen Liste, sondern aus einem Intervall $[von, bis]$ bestimmen wollen.
Implementiere die Funktion in der unteren Box entsprechend!


**Achtung: Da es sich um eine Bonusaufgabe handelt, gibt es hier keine automatische Korrektur. Bastle dir selbst Testfälle wie unten z.B. mit `print()`, um deinen Code auf korrekte Funktion zu prüfen.**

::: Hinweise
Du kannst `list(range(von, bis))` nutzen, um eine Liste aller ganzen Zahlen im Intervall $[von,bis)$ zu erhalten, die Zahl `bis` ist also nicht mehr Teil der Rückgabe! (Nutze also `range(von, bis + 1)`.)
:::


```python runnable
def istTeilerVon(teiler, zahl):
    """
    Prüft, ob zahl durch teiler teilbar ist.
    Z.B. liefert istTeilerVon(2, 4) True zurück.
    """
    return ((zahl % teiler) == 0)

'''
Ergänze unten deine Methode JahreszahlPruefen() aus den vorherigen Aufgaben.
Rückgabe: True wenn die übergebene Zahl ein Schaltjahr ist.
'''
def JahreszahlPruefen(jahr):
    
    


    
    return True

''' 
Ergänze hier nun die Methode JahreszahlIntervallPruefen().
Es wird eine Liste der Schaltjahre aus dem Intervall [von, bis] zurückgegeben.
'''
def JahreszahlIntervallPruefen(von, bis):
    
    
    
    
    
    


    return

# Testaufruf:
print(JahreszahlListePruefen(1900,1908))
# sollte [1904, 1908] zurückgeben.
# TODO: Mindestens 3 Testfälle ergänzen.


```
