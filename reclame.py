from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = format(prijs - prijs*korting, '.2f')
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro. "

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for i in inkomsten:
        totaal += i
    bedrag = format(totaal * btw, '.2f')
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    return hoog, laag

def gemiddelde(mijn_lijst):
    totaal = 0
    for i in mijn_lijst:
        totaal += i
    aantal = len(mijn_lijst)
    gemiddelde = format(totaal/aantal, '.2f')
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2) 
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])
