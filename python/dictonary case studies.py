# # Inventory Management System:

# inventry={
#     'apple':{'quantity':100,'price':0.5},
#     'banna':{'quantity':75,'price':0.3},
#     'orange':{'quantity':50,'price':0.4},
#     'pinepple':{'quantity':80,'price':0.6}
# }
# # display inventry 
# def display_inventry():
#    print("current_inventry:")
#    for item,details in inventry.items():
#       {f"{item}:Quantity - {details['quantity']}, Price - ${details['price']}"}
# # add new items
# def add_item(name,quantity,price):
#    if name in inventry:
#       print("item already exists in inventy.Updating quantity and price")
#       inventry[name]['quantity'] += quantity
#       inventry[name]['price'] = price
#    else:  
#       inventry[name]={'quantity':quantity,'price':price}
#       print(f"added {quantity} {name} (s) to inventry")# sell item
# def sell_item(name,quantity):
#   if name in inventry:
#      if inventry[name]['quantity'] >= quantity:
#         inventry[name]['quantity'] -= quantity
#         print(f"Sold {quantity} {name}")
#      else:  
#         print("insufficient quantity")
#   else:     
#      print("item not found ")

# display_inventry()
# add_item('grapes',20,1.2)
# sell_item('banana',10)
# sell_item('apple',99)
# display_inventry()


# laungauge translater

# english to french
# eng_to_french={
#     'hello':'bonjour',
#     'goodbye':'au revoir',
#     'thanku':'merci',
# }
# def translate_to_french(word):
#     return eng_to_french.get(word,' sorry!transalation not avaible')

# word=input("enter a word in english:-")
# print(f"the transalation in french is:- {translate_to_french(word)}")

# weather forcasting system
# weather_data={
#     'india':{'temperature':42,'humidity':60,'wind_speed':5},
#     'london':{'temperature':32,'humidity':56,'wind_speed':8},
#     'tokyo':{'temperature':10,'humidity':70,'wind_speed':6},
#     'new york':{'temperature':20,'humidity':50,'wind_speed':10},
# }
# def get_weather(city):
#     return weather_data.get(city,'city not found')
# city=input("enter your city:-")
# weather_info=get_weather(city)
# if weather_info != 'city not found':
#     print(f"weather in {city}:")
#     for key,value in weather_info.items():
#         print(f"{key} : {value}")
# else:
#         print("city not found")

# student gradebook

# Student grades
# gradebook = {
#     'parulparul': {'math': 85, 'science': 90, 'history': 80},
#     'Jane Smith': {'math': 90, 'science': 95, 'history': 85},
#     # Add more students and grades
# }

# def calculate_average_grades(student_name):
#     grades = gradebook.get(student_name)
#     if grades:
#         return sum(grades.values()) / len(grades)
#     else:
#         return "Student not found"

# student = input("Enter student name: ")
# average_grade = calculate_average_grades(student)
# if average_grade != "Student not found":
#     print(f"Average grade for {student}: {average_grade}")
# else:
#     print("Student not found")

