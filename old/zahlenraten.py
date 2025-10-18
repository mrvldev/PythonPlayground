import random

geheim = random.randint(1,100)
rate = 0
while rate != geheim:
    rate = int(input("Rate eine Zahl zwischen 1 und 100:"))
    
    if rate < geheim:
        print("Zu klein!")

    if rate > geheim:
        print("Zu gross!")
else:
    print("Richtig!!!!")        