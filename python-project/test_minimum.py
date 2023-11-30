import minimum as m

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")
    send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")

def fail():
    print("TECHIO> success false")

def assertMini(liste, expected):
    idx = m.min(liste)
    assert idx == expected, "minimum({}) -> index == {}, erwartet: {}".format(liste, idx, expected)

def test_vertauschen():   
    try:
        assertMini([1,2,3,4], 0)
        assertMini([4,2,3,4], 1)
        assertMini([4,2,3,4,-1], 4)
        
        # success
        success() 
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)

if __name__ == "__main__":
    test_vertauschen()