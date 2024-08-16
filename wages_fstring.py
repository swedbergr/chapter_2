# Get the pay rate and hours from the user
rate = float(input("What is the pay rate per hour? "))
hours = float(input("What is the number of hours worked? "))

# Calculate the gross income
income = rate * hours

# Print income
print(f"The gross income is ${income:.2f}")