import json

ansatte = '''
{
    "navn": "Daniel",
    "etternavn": "Myrvoll",
    "stilling": "vasker"
}
'''



data = json.loads(ansatte)


def add():
    print("Legg inn ny ansatt")
    print("")
    lol = input("Ansatt navn: ")

def edit():
    print("Rediger ansatt")
    print("")
    lol = input("Hvem vil du redigere: ")

def remove():
    print("Fjern ansatt")
    print("")
    lol = input("Hvem vil du fjerne: ")

def close():
    exit

def lister():
    print(data["name"], data["age"])

def main():
    print("BlackTure ansatt liste")
    print("")
    print("1. Legg inn ny ansatt")
    print("2. Rediger ansatt")
    print("3. Slett ansatt")
    print("4. List ut alle ansatte")
    print("5. Avslutt")
    print("")
    
    lol = input("Hva vil du gjøre?:")
    
    if lol == "1":
        add()

    if lol == "2":
        edit()

    if lol == "3":
        remove()

    if lol == "4":
        lister()

    if lol == "5":
        close()


    main()



