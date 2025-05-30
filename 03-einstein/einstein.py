# Prompt the user for mass as an integer (in kilograms)
mass = int(input("Enter mass in kilograms: "))
c = 300000000
# Calculate the Einstein formula (don't forget to convert the input from str to
# int)

energy = mass * c * c
# Print the result

print(f"E: {energy}")