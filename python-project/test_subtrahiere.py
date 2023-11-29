import subtrahiere

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
    
def test_subtrahiere():
    try:
        subtrahiere.subtrahiere(1, 1)
        assert last_print_out == "0", "subtrahiere(1, 1) Falsches Ergebnis, erwartet: {}".format(0)
        subtrahiere.subtrahiere(-1, 5)
        assert last_print_out == "-6", "subtrahiere(-1, 5) Falsches Ergebnis, erwartet: {}".format(-6)
        subtrahiere.subtrahiere(5, 1)
        assert last_print_out == "4", "subtrahiere(5, 1) Falsches Ergebnis, erwartet: {}".format(4)

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