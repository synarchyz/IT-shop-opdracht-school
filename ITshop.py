# Simpel programma voor opdracht week 5-7

# minimale voorraad
min_switches = 20
min_routers = 10
min_kabels = 100  # zelf gekozen

# startvoorraad
switches = 32
routers = 16
kabels = 180

print("Welkom bij de IT-shop")

doorgaan = "ja"

while doorgaan == "ja":
    print("\n--- Nieuwe bestelling ---")

    s = int(input("Aantal switches: "))
    r = int(input("Aantal routers: "))
    k = int(input("Aantal losse ethernetkabels: "))

    gratis_kabels = s * 2 + r
    totaal_kabels = k + gratis_kabels

    if s > switches or r > routers or totaal_kabels > kabels:
        print("\n[BERICHT VOOR KLANT]")
        print("Sorry, er is niet genoeg voorraad voor deze bestelling.")
    else:
        switches = switches - s
        routers = routers - r
        kabels = kabels - totaal_kabels

        print("\n[BERICHT VOOR KLANT]")
        print("Bedankt voor uw bestelling.")
        print("U krijgt:")
        print("-", s, "switches")
        print("-", r, "routers")
        print("-", k, "betaalde kabels")
        print("-", gratis_kabels, "gratis kabels")
        print("Totaal kabels:", totaal_kabels)

    print("\n[BERICHT VOOR VOORRAADBEHEERDER]")

    # Controleer of we onder de minimale voorraad switches zitten
    if switches < min_switches:
        # Bereken hoeveel switches we tekort hebben
        tekort_switches = min_switches - switches
        bestel_switches = tekort_switches
        # % 4 betekent: wat blijft over als je deelt door 4
        rest = bestel_switches % 4
        # != betekent: 'niet gelijk aan'
        # Als rest niet 0 is, dan is het aantal nog geen veelvoud van 4
        if rest != 0:
            # Rond naar boven af naar een veelvoud van 4
            bestel_switches = bestel_switches + (4 - rest)
        print("Bestel", bestel_switches, "switches")
    else:
        # Anders is de voorraad genoeg
        print("Switches: geen bestelling nodig")

    # Controleer of we onder de minimale voorraad routers zitten
    if routers < min_routers:
        # Bereken hoeveel routers we tekort hebben
        tekort_routers = min_routers - routers
        bestel_routers = tekort_routers
        # Routers moeten per 2 besteld worden
        rest = bestel_routers % 2
        # != betekent: niet gelijk aan
        if rest != 0:
            # Rond naar boven af naar een veelvoud van 2
            bestel_routers = bestel_routers + (2 - rest)
        print("Bestel", bestel_routers, "routers")
    else:
        # Anders is de voorraad genoeg
        print("Routers: geen bestelling nodig")

    # Controleer of we onder de minimale voorraad kabels zitten
    if kabels < min_kabels:
        # Bereken hoeveel kabels we tekort hebben
        tekort_kabels = min_kabels - kabels
        bestel_kabels = tekort_kabels
        # Kabels moeten per 10 besteld worden
        rest = bestel_kabels % 10
        # != betekent: niet gelijk aan
        if rest != 0:
            # Rond naar boven af naar een veelvoud van 10
            bestel_kabels = bestel_kabels + (10 - rest)
        print("Bestel", bestel_kabels, "ethernetkabels Cat 6")
    else:
        # Anders is de voorraad genoeg
        print("Kabels: geen bestelling nodig")

    # Laat de huidige voorraad zien op het scherm
    print("\nHuidige voorraad:")
    print("Switches:", switches)
    print("Routers:", routers)
    print("Kabels:", kabels)

    # Vraag of de gebruiker nog een bestelling wil invoeren
    doorgaan = input("\nNog een bestelling? (ja/nee): ").lower()

print("Programma gestopt")