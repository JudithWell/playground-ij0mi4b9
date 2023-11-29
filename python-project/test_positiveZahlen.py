from positiveZahlen import *

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")
    send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")


def fail():
    print("TECHIO> success false")
    
def test_positiveZahlen():
    try:
        liste = [1, 2, 3, -1, -2, -3, 5]
        pos = positiveZahlen(liste)
        assert pos == [1,2,3,5], "{}: Falsches Ergebnis: {} erwartet {}".format(liste, pos, [1,2,3,5])
        liste = [0]
        pos = positiveZahlen(liste)
        assert pos == [], "{}: Falsches Ergebnis: {} erwartet {}".format(liste, pos, [])
        liste = []
        pos = positiveZahlen(liste)
        assert pos == [], "{}: Falsches Ergebnis: {} erwartet {}".format(liste, pos, [])
        liste = [5, -5, 7, 0]
        pos = positiveZahlen(liste)
        assert pos == [5, 7], "{}: Falsches Ergebnis: {} erwartet {}".format(liste, pos, [5,7])
        
        # success
        success() 
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)

if __name__ == "__main__":
    test_positiveZahlen()