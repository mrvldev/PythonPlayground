# This is my first project out of the book "Python Crashcours" by Eric Matthes

# Asking for user input , correct the title, remove space in the beginning and format the input.
first_name = input("Enter your first name: ")
first_name = first_name.strip()
first_name = first_name.lower()


last_name = input("Enter your lastname: ")
last_name = last_name.strip()
last_name = last_name.lower()


# Make a full name of it
full_name = f"{first_name} {last_name}"

print(f"Hello, {full_name.title()} welcome to my first, self coded programm.")
print(f"All Big, {full_name.upper()}")
print(f"All low, {full_name.lower()}")
print(f"Your name is {len(full_name)-1} letters long.")

