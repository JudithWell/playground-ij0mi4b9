import subtrahiere2

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
    
def test_subtrahiere():
    try:
        zahl = subtrahiere2.subtrahiere(1, 1)
        assert zahl == 0, "subtrahiere(1, 1) Falsches Ergebnis, erwartet: {}".format(0)
        zahl = subtrahiere2.subtrahiere(-1, 5)
        assert zahl == -6, "subtrahiere(-1, 5) Falsches Ergebnis, erwartet: {}".format(-6)
        zahl = subtrahiere2.subtrahiere(5, 1)
        assert zahl == 4, "subtrahiere(5, 1) Falsches Ergebnis, erwartet: {}".format(4)

        if print_used:
            fail()
            send_msg("Achtung!", "Bitte verwende nicht print()!")
            builtins.print = orig_print
            return

        # success
        builtins.print = orig_print
        success() 
    except AssertionError as e:
        builtins.print = orig_print
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)

# }

if __name__ == "__main__":
    test_subtrahiere()