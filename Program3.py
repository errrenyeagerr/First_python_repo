def get_pay(num_hours):
    # Pre-tax pay, based on receiving $15/hour
    pay_pretax = num_hours * 15
    # After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (1 - 0.12)
    return pay_aftertax


# Calculate pay based on working 40 hours
pay_fulltime = get_pay(int(input("enter no. of hrs.:")))
print(pay_fulltime)


pay_parttime = get_pay(32)
print(pay_parttime)

