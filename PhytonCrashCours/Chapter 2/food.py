# I made that "Try it yourself" lesson a bit different
#I added a random to it

import random #import for random function
bestfood = ["Toast", "Leberkäsesemmel", "Burger"] #define list

#make random food 
a = (random.randint(0,2))
b = (random.randint(0,2))
c = (random.randint(0,2))
d = (random.randint(0,2))
e = (random.randint(0,2))

#print out the random values and put it in sentences
print(f"I want now an {bestfood[a]} to eat.")
print(f"I eat an {bestfood[b]} now.")
print(f"An {bestfood[c]} would be great now.")
print(f"{bestfood[d]} is the best food in the world.")
print(f"I will enjoy my  {bestfood[e]} now.")