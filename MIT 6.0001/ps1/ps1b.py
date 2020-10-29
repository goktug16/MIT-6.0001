

portion_down_payment = 0.25 # ratio of down payment
current_savings = 0 # amount of money you saves
r = 0.04  # annual rate of investment
annual_salary = float(input("Enter your annual salary"))   # your annual salary
portion_saved =  float(input("Enter the percent of your salary to save , as a decimal"))
total_cost = float(input("Enter the total cost of your dream home")) # cost of dream home
semi_annual_raise = float(input("Enter semi annual raise "))
number_of_months = 0;
portion_down_payment = 0.25 * total_cost

while current_savings <= portion_down_payment:
    current_savings += (annual_salary/12)*(portion_saved/100) + (current_savings * r/12)
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary += annual_salary*(semi_annual_raise/100)

print("Number of months", number_of_months)