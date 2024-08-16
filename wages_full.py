# Define hourly wage for all workers
HOURLY_RATE = 15.20

# Get hours worked for each employee from user
dave_hours = float(input("Enter the number of hours worked by Dave: "))
mary_hours = float(input("Enter the number of hours worked by Mary: "))
jake_hours = float(input("Enter the number of hours worked by Jake: "))
lexi_hours = float(input("Enter the number of hours worked by Lexi: "))

# Calculate the gross pay for each employee
dave_pay = dave_hours * HOURLY_RATE
mary_pay = mary_hours * HOURLY_RATE
jake_pay = jake_hours * HOURLY_RATE
lexi_pay = lexi_hours * HOURLY_RATE

# Return net pay for each employee to user
print(f"Dave's gross income is ${dave_pay:.2f}")
print(f"Mary's gross income is ${mary_pay:.2f}")
print(f"Jake's gross income is ${jake_pay:.2f}")
print(f"Lexi's gross income is ${lexi_pay:.2f}")