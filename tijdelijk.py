prijzen = {
    "aardbij" : 3,
    "vanille" : 4,
    "chocolade" : 5
}

aanbieding = float(prijzen["vanille"]) * 0.800001 #aangepast om een langer getal te krijgen, 4*0,8 = 3,2

reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")
for el in reclame_tekst4:
    if len(el) >= 5 :
        print(el)
    else:
        print(el.lower())




