def istTeilerVon(teiler, zahl):
    """
    Prüft, ob zahl durch teiler teilbar ist.
    Z.B. liefert istTeilerVon(2, 4) True zurück.
    """
    return ((zahl % teiler) == 0)

def JahreszahlEingebenUndPruefen():
    '''
    Um das Programm online testen zu können, musste das Einlesen
    mit input() entfernt werden!
    '''
    # aktuelleEingabe = input("Bitte Jahreszahl eingeben.  ")
    # jahr = int(aktuelleEingabe)
    global jahr
    
    print("Jahreszahl: " + str(jahr)) 
    
    ''' 
    Ergänze hier deine Prüfung der Jahreszahl!
    '''
    if istTeilerVon(4, jahr):
        print("Schaltjahr!")
    else:
        print("Kein Schaltjahr!")
    ''' ----- '''



# { autofold
""" 
Geheimer Code zu Testzwecken
"""
    
import builtins

last_print_out = ""
jahr = 0

def new_print(x):
    global last_print_out
    last_print_out = x
    return orig_print(x)


orig_print = builtins.print
builtins.print = new_print


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")
    send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")


def fail():
    print("TECHIO> success false")
    
def test_schaltjahr():
    global jahr
    
    try:
        # Test 1:
        jahr = 1996
        JahreszahlEingebenUndPruefen()
        assert last_print_out == "Schaltjahr!", 'Jahreszahl {} "Schaltjahr!" erwartet, letzte Ausgabe war "{}"'.format(jahr, last_print_out)
        
        # Test 2:
        jahr = 1998
        JahreszahlEingebenUndPruefen()
        assert last_print_out == "Kein Schaltjahr!", 'Jahreszahl {} "Kein Schaltjahr!" erwartet, letzte Ausgabe war "{}"'.format(jahr, last_print_out)

        # Test 3:
        jahr = 2000
        JahreszahlEingebenUndPruefen()
        assert last_print_out == "Schaltjahr!", 'Jahreszahl {} "Schaltjahr!" erwartet, letzte Ausgabe war "{}"'.format(jahr, last_print_out)
        
        # Test 4:
        jahr = 1900
        JahreszahlEingebenUndPruefen()
        assert last_print_out == "Kein Schaltjahr!", 'Jahreszahl {} "Kein Schaltjahr!" erwartet, letzte Ausgabe war "{}"'.format(jahr, last_print_out)
        
        # success
        builtins.print = orig_print
        success() 
    except AssertionError as e:
        builtins.print = orig_print
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)

# }

''' Die folgende Zeile nicht ändern! '''
test_schaltjahr()