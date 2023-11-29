from addiereListe import *

addiere_used = 0

def new_addiere(x):
    global addiere_used
    addiere_used += 1
    return orig_addiere(x)

orig_addiere = addiere
addiere = new_addiere

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")
    send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")


def fail():
    print("TECHIO> success false")
    
def test_addiereListe():
    try:
        zahl = addiereListe([1, -1])
        assert zahl == 0, "addiereListe([1, -1]) Falsches Ergebnis, erwartet: {}".format(0)
        zahl = addiereListe([1, 2, 3, -6, -6])
        assert zahl == -6, "addiereListe([1, 2, 3, -6, -6]) Falsches Ergebnis, erwartet: {}".format(-6)
        zahl = addiereListe([1,1,1,1, 5, -5])
        assert zahl == 4, "addiereListe([1,1,1,1, 5, -5]) Falsches Ergebnis, erwartet: {}".format(4)

        if addiere_used != 13:
            fail()
            send_msg("Achtung!", "Bitte verwende die vorgegebene Funktion addiere()!")
            return

        # success
        success() 
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)

if __name__ == "__main__":
    test_addiereListe()