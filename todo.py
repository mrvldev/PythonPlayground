#Schreiben
with open("todo.txt", "w") as f:
    f.write("Hallo Welt!")

#Lesen
with open("todo.txt", "r") as f:
    inhalt = f.read()
    print(inhalt)