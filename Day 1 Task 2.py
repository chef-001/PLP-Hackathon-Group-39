#Day 1 Task Two
def Task_2_Day_1():
    num_of_feet = int(input("Enter the number of square feet of wall that you want to be painted: "))
    price_of_paint = int(input("Enter the price of the paint per gallon: "))
    num_of_gallons = num_of_feet / 115
    hours_of_labor = num_of_gallons * 8
    cost_of_paint = num_of_gallons * price_of_paint
    cost_of_labor = hours_of_labor * 20
    total_cost = cost_of_paint + cost_of_labor
    print("The number of gallons of paint required is: ",num_of_gallons)
    print("The hours of labour required is: ",hours_of_labor)
    print("The cost of paint is: $.",cost_of_paint)
    print("The labor charges is: $.",cost_of_labor)
    print("The total estimated price for the paint job is: $.",total_cost)

Task_2_Day_1()