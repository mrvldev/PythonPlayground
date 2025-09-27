# Definieren der Klasse Auto
class Auto:
    def __init__(self, marke, model, jahr):
        self.marke = marke
        self.model = model
        self.jahr = jahr
# Vorstellen
    def vorstellen(self):
       print("Ich bin ein ", self.marke, self.model, "aus dem Jahr", self.jahr)

# Objekt der Klasse Auto erstellen
markeinp = input("Marke des Fahrzeuges: " ) 
modlinp = input("Modell des Fahrzeuges: " )
jahreinp = input("Baujahr des Fahrzeuges: " )
mein_auto = Auto(markeinp, modlinp,jahreinp)
mein_auto.vorstellen()