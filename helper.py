def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = format(bedrag/personen,"0.2f")
    except:
        bedrag_pp = "??"
    return f"Het bedrag per persoon is {bedrag_pp} euro"

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    aantal_streep = len(tekst)
    uit.append(aantal_streep * "=")
    return uit

def som(ijsjes):
    totaal = 0
    for i in ijsjes.values():
        totaal += i
    return totaal


