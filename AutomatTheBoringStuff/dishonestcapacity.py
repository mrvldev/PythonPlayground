print("Enter TB or BG for the advertised unit:")
unit = input(">")

# Calculate the amount that the advertised capacity lies:
if unit == "TB" or unit == "tb":
    discrepancy = 1000000000000 / 1099511627776
elif unit == "GB" or unit == "gb":
    discrepancy = 1000000000 / 1073741824
else:
    print("You must enter TB or GB.")

print("Enter the advertised capacity:")
advertised_capacity = input(">")
advertised_capacity = float(advertised_capacity)

# Calculate the real Capacity, round it to the neareat hundreths,
# and convert it to a string so it can be concatented:
real_capacity = str(round(advertised_capacity * discrepancy, 2))
print("The actual capacity is " + real_capacity + " " + unit)
