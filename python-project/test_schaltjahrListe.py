from schaltjahrListe import *

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")
    send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")


def fail():
    print("TECHIO> success false")
    
def test_schaltjahre():
    try:
        # Prüfe einzel Elemente:
        # Test 1:
        jahr = 1996
        ret = JahreszahlPruefen(jahr)
        assert ret, 'Jahreszahl {} True erwartet, gab aber False zurück'.format(jahr)
        
        # Test 2:
        jahr = 1998
        ret = JahreszahlPruefen(jahr)
        assert (not ret), 'Jahreszahl {} False erwartet, gab aber True zurück'.format(jahr)

        # Test 3:
        jahr = 2000
        ret = JahreszahlPruefen(jahr)
        assert ret, 'Jahreszahl {} True erwartet, gab aber False zurück'.format(jahr)
        
        # Test 4:
        jahr = 1900
        ret = JahreszahlPruefen(jahr)
        assert (not ret), 'Jahreszahl {} False erwartet, gab aber True zurück'.format(jahr)
        
        # Teste Listen
        liste = [2000, 2003, 2100]
        ret = JahreszahlListePruefen(liste)
        assert ret == [True, False, False], "{}: Falsches Ergebnis: {} erwartet {}".format(liste, ret, [True, False, False])
        liste = []
        ret = JahreszahlListePruefen(liste)
        assert ret == [], "{}: Falsches Ergebnis: {} erwartet {}".format(liste, ret, [])
        liste = [4, 100, 400, 1000]
        ret = JahreszahlListePruefen(liste)
        assert ret == [True, False, True, False], "{}: Falsches Ergebnis: {} erwartet {}".format(liste, ret, [True, False, True, False])
        
        # success
        success() 
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)

if __name__ == "__main__":
    test_schaltjahre()