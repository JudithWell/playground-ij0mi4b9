from schaltjahrParam import JahreszahlPruefen
import builtins

last_print_out = ""

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
        JahreszahlPruefen(jahr)
        assert last_print_out == "Schaltjahr!", 'Jahreszahl {} "Schaltjahr!" erwartet, letzte Ausgabe war {}'.format(jahr, last_print_out)
        
        # Test 2:
        jahr = 1998
        JahreszahlPruefen(jahr)
        assert last_print_out == "Kein Schaltjahr!", 'Jahreszahl {} "Kein Schaltjahr!" erwartet, letzte Ausgabe war {}'.format(jahr, last_print_out)

        # Test 3:
        jahr = 2000
        JahreszahlPruefen(jahr)
        assert last_print_out == "Schaltjahr!", 'Jahreszahl {} "Schaltjahr!" erwartet, letzte Ausgabe war {}'.format(jahr, last_print_out)
        
        # Test 4:
        jahr = 1900
        JahreszahlPruefen(jahr)
        assert last_print_out == "Kein Schaltjahr!", 'Jahreszahl {} "Kein Schaltjahr!" erwartet, letzte Ausgabe war {}'.format(jahr, last_print_out)
        
        builtins.print = orig_print
        success()
    except AssertionError as e:
        builtins.print = orig_print
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)


if __name__ == "__main__":
    test_schaltjahr()

