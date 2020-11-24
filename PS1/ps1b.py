starting_annual_salary = int(input("What is your annual salary? "))
portion_saved = int(input("What percentage of your salary do you want to save each month?" ))/100
total_cost = int(input("What is the cost of your dream house? "))
semi_annual_raise = int(input("By what percentage does your salary increase by every 6 months? "))/100

down_payment  = 0.25*total_cost
current_savings = 0
r = 0.04
months = 0
counter = 0
annual_salary = starting_annual_salary



while (current_savings<down_payment):
	investment = current_savings*r/12
	counter = months//6
	annual_salary = starting_annual_salary * ((semi_annual_raise+1)**counter)
	current_savings = current_savings + investment + portion_saved*annual_salary/12
	months = months + 1



print("The number of months you will need to save to buy this house is: ",months)