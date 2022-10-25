discussion_grade = input("What is your Discussion average?")
#journal grade should be no more than 32.5
#this will take users input
Journal_grade = input("What is your journal grade?")
#This takes the users input for a journal grade and should be a max of 3.5
Assignment_grade = input("What is your Assignment grade?")
#takes input for assign grade and should be no more than 44% or 440 points
Mid_proj = input("How many points did you receive on your Midterm project?")
#takes input for mid project and should be no more than 10% or 10 points
Final_proj = input("How many points did you receive for your final project?")
#takes input for final project and should be no more than 10% or 10 points
total_points = discussion_grade + Journal_grade + Assignment_grade + Mid_proj + Final_proj
if total_points >= 90:
    print("Congratulations you receive and A!")
    if total_points < 90 and total_points >= 80:
        print("Good Job you receive a B!")
        if total_points < 80 and total_points >= 70:
            print("You passed the class with a C!.")
            if total_points < 70 and total_points >= 60:
                print("You just passed, keep studying, I know you can do better!")
                print("You failed the Class")