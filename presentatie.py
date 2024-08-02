from helper import *

def presenteer(aantal, totaal):
    print()
    for k, v in aantal.items():
        print(f"{k} : {v} euro")
    print(26*"=")
    print(f"totaal : {totaal} euro")
