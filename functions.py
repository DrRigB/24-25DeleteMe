#Functions are essentially a blokc of code that is nothing until it is called someewhere.
#DRY! Dont" Repeat Yourself.
#DRY! Dont" Repeat Yourself.
#DRY! Dont" Repeat Yourself.
#DRY! Dont" Repeat Yourself.
#DRY! Dont" Repeat Yourself.

# "def" is what notifies the code that a function is about to start


def my_function():
    print("my function has run")


my_function()


def npc_greeting(): 
    print("Hello travaler. Would you like to browse my wares?")

npc_greeting()

def player_response(the_response):
    print(the_response)


answer_no = "Nah. I'm good man"

answer_yes = "Oh yes. No Skibidi Ohio stuff tho"
player_response(answer_no)
player_response(answer_yes)

npc_greeting()
player_response(answer_no)

def approach_vender():
    npc_greeting()
    player_response = input("Enter 1 for yes, 2 for no.")
    player_response = int(player_response)

    if (player_response == 1):
        print("I'd like to buy a skibidi toilet please")

    elif (player_response == 2):
        print("Player Ninja fell off hard")
    else:
        print("I'm sorry I don't speak that language, do you have any vegemite sanwiches?")

approach_vender()