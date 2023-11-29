from schaltjahrReturn import JahreszahlPruefen
import builtins

print_used = False

def new_print(x):
    global print_used
    print_used = True
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
    try:
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
        
        if print_used:
            fail()
            send_msg("Achtung!", "Bitte verwende nicht print()!")
            builtins.print = orig_print
            return
        builtins.print = orig_print
        success()
    
    except AssertionError as e:
        builtins.print = orig_print
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)


if __name__ == "__main__":
    test_schaltjahr()

