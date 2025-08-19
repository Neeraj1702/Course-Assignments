# Create a Personalized Greeting

a=input("Enter your First Name: ")
b=input("Enter your Last Name: ")

# Print a formatted welcome message using an f-string.
# An f-string allows you to easily embed variables inside a string
print(f"\nHello, {a} {b}!,Welcome to Python Program.")

#other method using .format()
print("\nHello, {} {}!,Welcome to Python Program.".format(a,b))
