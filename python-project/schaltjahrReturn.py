def istTeilerVon(teiler, zahl):
    """
    Prüft, ob zahl durch teiler teilbar ist.
    Z.B. liefert istTeilerVon(2, 4) True zurück.
    """
    return ((zahl % teiler) == 0)

'''
Ergänze unten die Methode JahreszahlPruefen() mit einem Parameter und einem Rückgabewert!.
'''



# Testaufruf:
print(JahreszahlPruefen(2023))
