weather_condition = input("What's the weather like today? (sunny, rainy, cold)")
if weather_condition.lower() == "sunny":
    print("Wear a T-shirt and sunglasses.")
elif weather_condition.lower() == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_condition.lower() == "cold":
    print("Make sure to weara warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
