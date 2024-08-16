# Get number of minutes from user
minutes = float(input("Enter number of minutes: "))

# Convert to hours
hours = minutes // 60 

# Convert to minutes
min = minutes % 60

# Print both hours and minutes
print(minutes, "is", hours, "hours and",
min, "minutes." )