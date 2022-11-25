user_names = []
eye_color = ("green", "blue", "brown", "hazel", "grey")
print("Eye colors: " + str(eye_color))
hair_color = ("brown", "black", "blonde", "red" )
print("Hair colors: " + str(hair_color))
city_state = {"":""}
while True:

    user_name_question = input("Enter a username: ")
    user_names.append(user_name_question)
    eye_color_question = input("What color are your eyes? : ")
    hair_color_question = input("What color is your hair")
    city_state_question = input("What city and state do you live in? :")
    user_profile = (user_names, eye_color_question, hair_color_question, city_state_question)
    user_profiles = []
    user_profiles.append(user_profile)
    print(user_profile)
    print(user_profiles)
#def user_profile(user_names, eye_color_question, hair_color_question, city_state_question):
    #user_name_question = input("Enter a username: ")
   # user_names.append(user_name_question)
    #eye_color_question = input("What color are your eyes? : ")
    #hair_color_question = input("What color is your hair")
    #city_state_question = input("What city and state do you live in? :")
    #return user_profile(user_names, eye_color_question, hair_color_question, city_state_question)
    
#user_profile()