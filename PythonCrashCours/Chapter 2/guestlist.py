#This is a lesson to work with lists in python
#I did it again ^^
guestlist = ["Andy", "Sputz", "Nina", "Martin"]

cannot = guestlist.pop(0)
guestlist.insert(0, "Friedrich")
guestlist.insert(2, "Josef")
guestlist.append("Karl")

disable1 = guestlist.pop(5)
disable2 = guestlist.pop(4)
disable3 = guestlist.pop(3)
disable4 = guestlist.pop(2)
print(guestlist)
print("Hallo " + guestlist[0], "ich lade dich zum Essen ein.")
print("Servus " + guestlist[1], "ich würde dich gerne zum essen einladen.")
print(cannot, "kann leider nicht kommen.")
print("Lieber ", disable1, ",", disable2, ",", disable3 + ",", disable4, ",", "leider ist mein Esstisch zu klein und ich mus euch ausladen.")
del guestlist[0]
del guestlist[0]
print(guestlist)