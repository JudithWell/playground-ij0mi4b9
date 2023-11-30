# Bonus: Vorbereitungen für Sortieralgorithmen

Nächste Woche werden wir uns mit Sortieralgorithmen beschäftigen.
Die Aufgabe solcher Sortieralgorithmen ist, Listen o.ä. in eine sortierte Form (z.B. aufsteigend sortierte Zahlen, Alphabetisch sortierte Begriffe) zu bringen. Sortieren ist deshalb wichtig, da es in großen Datenmengen deutlich einfacher ist, bestimmte Einträge zu finden, wenn diese Daten bereits sortiert sind.

Wir werden in diesem Abschnitt ein paar Funktionen vorbereiten, die wir beim Sortieren gebrauchen können.

## Vertauschen zweier Elemente

Sogenannte "in situ"-Sortieralgorithmen bearbeiten die Liste, die ihnen übergeben wurde (im Gegensatz zu Algorithmen, die die ursprüngliche Liste nicht verändern, aber eine neue Liste mit denselben Elementen in sortierter Reihenfolge zurückgeben).
Um eine unsortierte Liste zu sortieren, müssen also Elemente innerhalb der Liste vertauscht werden können.

Ein Beispiel vorneweg:

```python
liste = [1, 3, 2]

# vertausche Element an Index 1 und Index 2
vertausche(liste, 1, 2)
# liste ist jetzt [1, 2, 3]
```

Implementiere nun die entsprechende Funktion `vertausche()`, die drei Parameter erhält: Die Liste und die zwei Indizes (bei 0 beginnend) der Elemente die vertauscht werden sollen.

@[Vertauschen zweier Listeneinträge]({"stubs": ["vertauschen.py"], "command": "python3 test_vertauschen.py", "project": "python"})

## Minimumsuche

Ein Sortieralgorithmus, der sehr einfach zu verstehen ist, basiert darauf das kleinste Element in einer Liste zu finden. In einer Liste `[2, 4, 1]` wird das kleinste Element (hier `1`) lokalisiert und dann an die erste Stelle der Liste gelegt.

Wir wollen zunächst nur eine Funktion `minimum()` programmieren, die als Parameter die Liste erhält und den Index des kleinsten Elements in der Liste zurückgibt. Aufrufe könnten so aussehen:

```python
liste = [2, 4, 1]

minIndex = minimum(liste)
# minIndex == 2 (1 steht an dritter Stelle in der Liste, Indizes beginnen bei 0)
```

Programmiere nun die entsprechende Funktion `minimum()`!

::: Hinweise:
- Durchlaufe die Liste mit einer "index-basierten" Wiederholung
- Merke dir das bisher kleinste Element und dessen Index in je einer Variable
- Vergleiche jedes Element mit dem bisher kleinsten und aktualisiere entsprechend die Variableneinträge
:::

@[Minimum einer Liste finden]({"stubs": ["minimum.py"], "command": "python3 test_minimum.py", "project": "python"})
