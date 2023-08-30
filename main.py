bot_name = "Bob"
bot_age = 16
bot_color = "Yellow"
bot_food = "Spaghetti"
bot_subject = "Biology"
bot_hobby = "playing sports"
bot_song = "Megalovania"
bot_birthday = "January 20, 2007"
bot_game = "Undertale"
bot_gwa = 1.47

print("Hello! My name is " + bot_name + ". What's your name?")
user_name = str(input())

print("Nice to meet you " + user_name + "! I am " + str(bot_age) + " years old! How old are you?")
user_age = int(input())

print("My favorite color is " + bot_color + ". What is your favorite color?")
user_color = str(input())

print(user_color + " is a wonderful color! I love to eat " + bot_food + ". What is your favorite food?")
user_food = str(input())

print("That is delicious. My favorite subject is " + bot_subject + ". What is yours?")
user_subject = str(input())

print("My hobby is " + bot_hobby + ". What is your hobby?")
user_hobby = str(input())

print("My favorite song is " + bot_song + " which is from my favorite game " + bot_game)
print("What is your favorite song?")
user_song = str(input())
print("Your favorite game?")
user_game = str(input())

print("I was born on " + bot_birthday + ". What about you?")
user_birthday = str(input())

print("I got a GWA of " + str(bot_gwa) + " in Grade 10. What was your final GWA in Grade 10?")
user_gwa = float(input())

print(str(user_gwa) + " isn't a bad grade. Let's do better nxt school year!")
print("It was fun chatting with you " + user_name + "! What would you like to say before we go?")
user_last_words = str(input())

print("See you later " + user_name + "!")
