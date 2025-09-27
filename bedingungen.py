antwort = input("Magst du Pizza? (ja/nein) ")

if antwort.lower() == "ja":
    print("Gute Wahl!")
elif antwort.lower() == "nein":
    print("Schade, mehr für mich!")
else:
    print("Bitte antworte mit 'ja' oder 'nein'.")
