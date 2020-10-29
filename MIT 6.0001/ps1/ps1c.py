
semi_annual_raise = 0.07
r = 0.04
total_cost =10**6
annual_salary = float(input("Enter the starting salary"))

down_payment = total_cost * 0.25
current_savings = 0
number_of_steps = 0
number_of_months = 0
up = 10000
down = 0
interest_rate = 0


def saving_calculator(salary, current, rate):
    for months in range(1, 37):
        current += (salary / 12) * rate + (current * r / 12)
        if months % 6 == 0:
            salary += salary * (semi_annual_raise)

    return current


while abs(current_savings - down_payment) >= 100 and number_of_steps < 100:
    interest_rate = float(up + down) / 2
    interest = interest_rate / 10000.0
    current_savings = saving_calculator(annual_salary, current_savings, interest)
    if current_savings < down_payment:
        down = interest_rate
        current_savings = 0
    elif current_savings > down_payment+100:
        up = interest_rate
        current_savings = 0
    number_of_steps += 1

if number_of_steps == 100:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate : %.4f" % interest)
    print("Steps in bisection search", number_of_steps)
