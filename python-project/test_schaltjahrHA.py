jahr = 0

from schaltjahrHA import JahreszahlEingebenUndPruefen
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


def fail():
    print("TECHIO> success false")
    
def test_schaltjahr():
    global jahr
    
    # Test 1:
    jahr = 1996
    JahreszahlEingebenUndPruefen()
    assert last_print_out == "Schaltjahr!", 'Jahreszahl {} "Schaltjahr!" erwartet, letzte Ausgabe war {}'.format(jahr, last_print_out)
    
    # Test 2:
    jahr = 1998
    JahreszahlEingebenUndPruefen()
    assert last_print_out == "Kein Schaltjahr!", 'Jahreszahl {} "Kein Schaltjahr!" erwartet, letzte Ausgabe war {}'.format(jahr, last_print_out)

    # Test 3:
    jahr = 2000
    JahreszahlEingebenUndPruefen()
    assert last_print_out == "Schaltjahr!", 'Jahreszahl {} "Schaltjahr!" erwartet, letzte Ausgabe war {}'.format(jahr, last_print_out)
    
    # Test 4:
    jahr = 1900
    JahreszahlEingebenUndPruefen()
    assert last_print_out == "Kein Schaltjahr!", 'Jahreszahl {} "Kein Schaltjahr!" erwartet, letzte Ausgabe war {}'.format(jahr, last_print_out)


if __name__ == "__main__":
    test_schaltjahr()

