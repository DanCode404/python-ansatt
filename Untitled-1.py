import json


def leggtil():
    print("Skriv inn navnet")
    kontroll_n = input("> ")
    print("Skriv inn etternavn")
    kontroll_en = input("> ")
    print("Skriv inn stilling")
    kontroll_s = input("> ")
    print("Skal", kontroll_s, kontroll_n, kontroll_en, "legges til? -  j/n" )
    kontroll_legger = input("> ")
    nyansatt = {0: {"fornavn": kontroll_n, "etternavn": kontroll_en, "stilling": kontroll_s}}

    if kontroll_legger == "n":
        print("Sender deg tilbake til meny")
        time.sleep(0.3)
        print(".")
        time.sleep(0.3)
        print("..")
        time.sleep(0.3)
        print("...")
        time.sleep(0.3)
        print("....")
        main()
    if kontroll_legger == "j":
        with open("save.json", "w") as f:
            json.dump(nyansatt, f)
    main()

def edit():
    print("Rediger ansatt")
    print("")
    lol = input("Hvem vil du redigere: ")
    main()

def remove():
    print("Fjern ansatt")
    print("")
    lol = input("Hvem vil du fjerne: ")
    main()

def close():
    exit

def lister():
    print(data["name"], data["age"])
    main()

def main():
    print("Ansatt Register")
    print("")
    print("1. Legg inn ansatt")
    print("2. Fjern ansatt")
    print("3. Rediger ansatte")
    print("4. List ansatte")
    print("5. Close")

    kontroll = input("> ")

    if kontroll == "1":
        leggtil()
    
    if kontroll == "2":
        fjerner()

    if kontroll == "3":
        edit()
    
    if kontroll == "4":
        listut()


main()


import json
import time

ansatt = {"stillingsnummer": 0, 0: {"fornavn": "Daniel", "etternavn": "myrvoll", "jobb": "vasker"}}
