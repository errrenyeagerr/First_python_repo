# With the help of a Python Function "get_pay_with_more_inputs" input (num_hours, hourly_wage, tax_bracket).

# Let the num_hours be 40
# Let the hourly_wage be $250
# Let the tax_bracket be 22% ---> which is 0.22

def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    salary_before_tax = num_hours * hourly_wage
    salary_after_tax = salary_before_tax * (1-0.22)
    return salary_after_tax

salary_in_hand = get_pay_with_more_inputs(1,250,0.22)
print (salary_in_hand)

try:
    num_hours = float(input("Please Enter The 'Worked' Number Of Hours: "))
    hourly_wage = float(input("Please Enter The Hourly Wage Of Your Job: "))
    tax_bracket = 0.22
    print("The Tax Is Set At 22%.")
    ans = get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket)
    print(f"The In Hand Salary You Get Is : ${ans}")

except ValueError:
    print("Please Enter Valid Details")