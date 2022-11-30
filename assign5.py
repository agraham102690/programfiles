#empty list for adding usernames later
user_names = []
#natural eye colors to be printed to choose from
eye_color = ("green", "blue", "brown", "hazel", "grey")
print("Eye colors: " + str(eye_color))
#nat hair colors to choose from
hair_color = ("brown", "black", "blonde", "red" )
print("Hair colors: " + str(hair_color))
city_state = {"City":"State"}

while True:

    user_name_question = input("Enter a username: ")
    user_names.append(user_name_question)
    eye_color_question = input("What color are your eyes?: ")
    hair_color_question = input("What color is your hair?: ")
    city_state_question = input("What city and state do you live in?: ")
    user_name_data = ("Username Data: " + str(user_names))
    user_profiles = {"Username":user_names, "Eye_color":eye_color_question, "Hair Color":hair_color_question,
    "City State":city_state_question}
    user_profiles.update({"Username":user_name_question, "Eye Color":eye_color_question, 
    "Hair Color":hair_color_question, "City State":city_state_question})
    user_profiles_data = {}
    user_profiles_data.update(user_profiles)
    print(user_name_data)
    print(user_profiles)
    print(user_profiles_data)
    
#def user_profile(user_names, eye_color_question, hair_color_question, city_state_question):
    #user_name_question = input("Enter a username: ")
   # user_names.append(user_name_question)
    #eye_color_question = input("What color are your eyes? : ")
    #hair_color_question = input("What color is your hair")
    #city_state_question = input("What city and state do you live in? :")
    #return user_profile(user_names, eye_color_question, hair_color_question, city_state_question)
    
#user_profile()