# Get input for the check amount.
# Convert to float.
meal_cost = float(input("Enter meal cost: "))

# Get input for the tip percent. Convert to int.
tip_percent = int(input("Enter tip percent: "))

# Calculate the tip amount.  Don't forget to divide by 100 to a *real* percent.
tip_amount = meal_cost * (tip_percent / 100)

# Print the tip results in the format `A PCT% tip on $CHECK is $AMOUNT`. Except
# for the tip PCT (which should be an int), just let the number of decimal
# places run long or short. We'll learn how to round and format these numbers
# later. You may want to construct an output string a step at a time to avoice a
# really long concatenation.
print(f"A {tip_percent}% tip on ${meal_cost} is ${tip_amount}")
