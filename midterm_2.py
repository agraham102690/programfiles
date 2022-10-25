height = float(input("What is your height (inches)"))
weight = float(input("How much do you weight (pounds) "))
bmi = 703 * weight / (height**2)
if bmi <= 18.4:
    print("You're underweight and your bmi is " + str(bmi))
elif bmi >=18.5 and bmi <=24.9:
    print("You're considered normal weigh" + str(bmi))
elif bmi >25 and bmi <= 39.9:
    print("You're over weight and your bmi is " + str(bmi))
else:
    print("You're considered obese and your bmi is " + str(bmi))
#3500 calories is approx 1 pound
#calories = 3500
#pound = 1.0
weight_goal = float(input("How much do you want to weigh? (just the number of pounds) " ))
weeks_to_goal = float(input("In how many weeks do you want to achieve this goal? (use number) " ))
pound_per_week = weight_goal - weight

print("If you lost/gained 1 pound per week, it will take you " 
+ str(pound_per_week) + 
(" weeks to reach your goal"))
two_pound_per_week = pound_per_week/2
print("If you lost/gained two pounds per week it will take you " 
+str(two_pound_per_week) + (" week(s)to reach your goal"))
desired_weight_goal = pound_per_week/weeks_to_goal
print("You will need to lose/gain " + str(desired_weight_goal) +
(" pounds per week to reach your desired weight loss goal"))
