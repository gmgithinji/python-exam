def calculate_salary(hourly_rate, hours_worked, tax_rate=0.15):
  """
Calculate the net salary after the deduction

Parameters:
hourly_rate(float): The rate per hour.
hours_worked(float):The number of hours worked.
tax_rate(float): The tax rate is to be applied on the gross salary.(0.15%)

Returns:
float: The net salary after tax deduction.
"""
#Compute the gross salary
gross_salary = hourly_rate * hours_worked
#Deduct tax from gross salary
tax_amount = gross_salary * tax_rate
#Calculate the net salary
net_salary = gross_salary - tax_amount

return net_salary

def main():

 Mainfunctiontodrivetheprogramexecution
""
try:
    #Prompt the user to enter their hourly rates and hours worked
    hourly_rate = float(input("Enter hourly rate: "))
    hours_worked = float(input("Enter hours worked: "))

    #Validate input to ensure non-negative values
    if hourly_rate <0 or hours_worked <0:
        raise ValueError("Hourly rate and hours worked must be non-negative")

    #Call calculate_salary() and print the formatted net_salary
     net_salary = calculate_salary(hourly_rate, hours_worked)
     print(f"Net Salary: (net _salary:,...2f)")

except ValueError as e:
    print(f"Invalid Input: (e)")

#Ensure proper function naming conventions and comments
    if__name__=="__main__":
        main()
