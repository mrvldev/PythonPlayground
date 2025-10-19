while True:
    print("1. Kontakt hinzufügen.")
    print("2. Kontakt anzeigen.")
    print("3. Beenden.")
    wahl = input("Wählen Sie eine Aktion (1-3): ")

    if wahl == "1":
        name = input("Name: ")
        nummer = input("Nummer: ")
        with open("contacts.txt", "a") as file:
            file.write(f"{name},{nummer}\n")
            print("Kontakt hinzugefügt.")
    if wahl == "2":
        with open("contacts.txt", "r") as file:
            inhalt = file.read()
            print("Kontakte:")
            print(inhalt)
    break