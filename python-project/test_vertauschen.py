import vertauschen as v

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")
    send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")

def fail():
    print("TECHIO> success false")

def assertSwap(liste, indices, expected):
    call = str(liste) + ", " + str(indices[0]) + ", " + str(indices[1])
    v.vertauschen(liste, indices[0], indices[1])
    assert liste == expected, "vertausche({}) -> liste == {}, erwartet: {}".format(call, liste, expected)

def test_vertauschen():   
    try:
        assertSwap([1,2,3,4], (1,2), [1,3,2,4])
        assertSwap([1,2,3,4], (1,1), [1,2,3,4])
        assertSwap(["A", "B", "C"], (0,2), ["C", "B", "A"])

        # success
        success() 
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)

if __name__ == "__main__":
    test_vertauschen()