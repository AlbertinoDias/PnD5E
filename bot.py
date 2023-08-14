import os
import discord
import responses
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

# ------------------------------------------------
# section that handles the calls to other .py that handle the back office of the program
# ------------------------------------------------

# sends a call to the function "dice roll" and returns a response with the string it gets
# then it sends the string in the channel if it is not private or a private message if it is
async def send_dice_roll(message, user_message, is_private):
    try:
        response = responses.dice_roll(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
# sends a call to the function "list_move" and returns a response with the string it gets
# then it sends the string in the channel if it is not private or a private message if it is
async def search_move(message, user_message, is_private):
    try:
        response = responses.list_move(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# sends a call to the function "list_moves_by_something" and returns a response with the string it gets
# then it sends the string in the channel if it is not private or a private message if it is
async def search_something(message, *user_message, is_private):
    try:
        response = responses.list_moves_by_something(user_message[0], user_message[1])
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# sends a call to the function "list_keywords" and returns a response with the string it gets
# then it sends the string in the channel if it is not private or a private message if it is
async def search_keywords(message, is_private):
    try:
        response = responses.list_keywords()
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# sends a call to the function "list_commands" and returns a response with the string it gets
# then it sends the string in the channel if it is not private or a private message if it is
async def search_commands(message, is_private):
    try:
        response = responses.list_commands()
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# sends a call to the function "list_commands" and returns a response with the string it gets
# then it sends the string in the channel if it is not private or a private message if it is
async def search_inventory(message, userId, is_private):
    try:
        response = responses.list_inventory(userId)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# sends a call to the function "list_moves_by_something" and returns a response with the string it gets
# then it sends the string in the channel if it is not private or a private message if it is
async def inventory_add(message, userId, *user_message, is_private):
    try:
        response = responses.add_to_inventory(userId, user_message[0], user_message[1])
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# sends a call to the function "use_from_inventory" and returns a response with the string it gets
# then it sends the string in the channel if it is not private or a private message if it is
async def inventory_use(message, userId, *user_message, is_private):
    try:
        response = responses.use_from_inventory(userId, user_message[0], user_message[1])
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# sends a call to the function "give_item" and returns a response with the string it gets
# then it sends the string in the channel if it is not private or a private message if it is
async def inventory_give(message, userId, frienId, *user_message, is_private):
      
    try:
        response = responses.give_item(str(userId), frienId, user_message[0], user_message[1])
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# sends a call to the function "list_moves_by_something" and returns a response with the string it gets
# then it sends the string in the channel if it is not private or a private message if it is
async def inventory_wipe(message, frienId, is_private):
      
    try:
        response = responses.wipe_invetory(frienId)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# sends a call to the function "give_xp" and returns a response with the string it gets
# then it sends the string in the channel if it is not private or a private message if it is
async def show_xp(message, user_message):
    try:
        response = responses.give_xp(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

# ------------------------------------------------
# section that handles the received message and calls the functions that link that msg to the other .py 
# ------------------------------------------------


# main function that waits for calls from the users and connects to the server
def run_disc_bot():
    
    # uses a library to open a .env file and load a variable
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    # gives the variable the necessary class to work and specifies how to call the bot (prefix)
    bot_commands = commands.Bot(command_prefix="€", intents= discord.Intents.all())
    
# ------------------------------------------------
# section that handles misc commands
# ------------------------------------------------
    # debug code that when the bot starts prints a message to know if it starts
    @bot_commands.event
    async def on_ready():
        print(f'{bot_commands.user} has connected to Discord!')
    
    # function to roll a random number between 1 and the number typed
    @bot_commands.command()
    async def roll(message, *number):
        #checks if the inittial message is a user message (avoids infinite loops)
        if message.author == bot_commands.user:
            return
        
        # checks the number of arguments, if they are 2 checks for a keyword in the first 
        # and a numeric in the second, if correct, sends a pm, if not, gives an error msg
        if len(number) == 2:
            if number[0] == "pvt" and number[1].isnumeric():
                await send_dice_roll(message, number[1], is_private=True)
            else:                
                await message.channel.send("invalid format, write \"€roll + pvt + number\" for a private roll or \"€roll + number\" for a public roll (number has to be numeric, ex.: \"€roll pvt 20\")")
        # if the number of arguments is 1, checks if it's a numeric and sends a msg in the 
        # channel that the command was inputed if it is, or sends an error msg if it isn't
        elif len(number) == 1:
            if number[0].isnumeric():
                await send_dice_roll(message, number[0], is_private=False)
            else: await message.channel.send("invalid format, write \"€roll + pvt + number\" for a private roll or \"€roll + number\" for a public roll (number has to be numeric, ex.: \"€roll pvt 20\")")
        else: await message.channel.send("invalid format, write \"€roll + pvt + number\" for a private roll or \"€roll + number\" for a public roll (number has to be numeric, ex.: \"€roll pvt 20\")")


# ------------------------------------------------
# section that handles commands information
# ------------------------------------------------
    @bot_commands.command()
    async def keywords(message):
        #checks if the inittial message is a user message (avoids infinite loops)
        if message.author == bot_commands.user:
            return
        await search_keywords(message, is_private=False)
    

    @bot_commands.command()
    async def comands(message):
        #checks if the inittial message is a user message (avoids infinite loops)
        if message.author == bot_commands.user:
            return
        await search_commands(message, is_private=False)


# ------------------------------------------------
# section that handles moves
# ------------------------------------------------

    @bot_commands.command()
    async def move(message, moveName):
        #checks if the inittial message is a user message (avoids infinite loops)
        if message.author == bot_commands.user:
            return
        await search_move(message, moveName, is_private=False)

    @bot_commands.command()
    async def any(message, *trial):
        # checks if the inittial message is a user message (avoids infinite loops)
        if message.author == bot_commands.user:
            return
        
        # checks the number of arguments, if they are 2 checks for a keyword in the first 
        # and a numeric in the second, if correct, sends a pm, if not, gives an error msg
        print(len(trial))
        if len(trial) == 3:
            if trial[0] == "pvt":
                await search_something(message, trial[1], trial[2], is_private=True)                
            else:   
                await message.channel.send("invalid format, write \"€any + pvt + Keyword + SearchWord\" for a dm or \"€any + Keyword + SearchWord\" for a public list (ex.: \"any pvt type Fighting\", use command \"€keywords\" to see the list of keywords, multiple search words need to be inside quotes, and remember it is caps sensitive))")
        # if the number of arguments is 1, checks if it's a numeric and sends a msg in the 
        # channel that the command was inputed if it is, or sends an error msg if it isn't
        elif len(trial) == 2:
                await search_something(message, trial[0], trial[1], is_private=False)
        else: await message.channel.send("invalid format, write \"€any + pvt + Keyword + SearchWord\" for a dm or \"€any + Keyword + SearchWord\" for a public list (ex.: \"any pvt type Fighting\", use command \"€keywords\" to see the list of keywords, multiple search words need to be inside quotes, and remember it is caps sensitive))")
    

# ------------------------------------------------
# section that handles inventory
# ------------------------------------------------

    @bot_commands.command()
    async def inventory(message):
        #checks if the inittial message is a user message (avoids infinite loops)
        if message.author == bot_commands.user:
            return
        #discord.Member.id
        print(message.author.id)
        await search_inventory(message, message.author.id, is_private=False)


    @bot_commands.command()
    async def add(message, *trial):
        # checks if the inittial message is a user message (avoids infinite loops)
        if message.author == bot_commands.user:
            return
        
        # checks the number of arguments, if they are 2 checks for a keyword in the first 
        # and a numeric in the second, if correct, sends a pm, if not, gives an error msg
        if len(trial) == 2:
            if trial[0].isnumeric() == False and trial[1].isnumeric():
                await inventory_add(message, message.author.id, trial[0], trial[1], is_private=False)                
            else:   
                await message.channel.send("invalid format, write \"€add + itemName + amount\" (ex.: \"add rope 5\", to add 5 ropes, and item with multiple words need to be inside quotes, ex.: \"max revive\")")
        
        else: await message.channel.send("invalid format, write \"€add + itemName + amount\" (ex.: \"add rope 5\", to add 5 ropes, and item with multiple words need to be inside quotes, ex.: \"max revive\")")
    

    @bot_commands.command()
    async def use(message, *trial):
        # checks if the inittial message is a user message (avoids infinite loops)
        if message.author == bot_commands.user:
            return
        
        # checks the number of arguments, if they are 2 checks for a keyword in the first 
        # and a numeric in the second, if correct, sends a pm, if not, gives an error msg
        print(len(trial))
        if len(trial) == 2:
            if trial[0].isnumeric() == False and trial[1].isnumeric():
                await inventory_use(message, message.author.id, trial[0], trial[1], is_private=False)                
            else:   
                await message.channel.send("invalid format, write \"€add + itemName + amount\" (ex.: \"add rope 5\", to add 5 ropes, and item with multiple words need to be inside quotes, ex.: \"max revive\")")
        
        else: await message.channel.send("invalid format, write \"€add + itemName + amount\" (ex.: \"add rope 5\", to add 5 ropes, and item with multiple words need to be inside quotes, ex.: \"max revive\")")
    


    @bot_commands.command()
    async def give(message, *trial):
        # checks if the inittial message is a user message (avoids infinite loops)
        if message.author == bot_commands.user:
            return
        
        # checks the number of arguments, if they are 2 checks for a keyword in the first 
        # and a numeric in the second, if correct, sends a pm, if not, gives an error msg
        if len(trial) == 3:
            # as mentios are in this format "<@XXXXXXXXXX>" where X are numbers, using [2:-1] we can
            # get everything inside the string starting from the 2º character until 1 less of the end 
            friendID = trial[0][2:-1]


            if trial[1].isnumeric() == False and trial[2].isnumeric() and trial[0][1] =="@":
                print("entrou dentro")
                await inventory_give(message, message.author.id, friendID, trial[1], trial[2], is_private=False)  
                            
            else:   
                await message.channel.send("invalid format, write \"€give + @user + itemName + amount\" (ex.: \"give @AlbertinoDias rope 5\", to add 5 ropes, and item with multiple words need to be inside quotes, ex.: \"max revive\")")
        
        else: await message.channel.send("invalid format, write \"€give + @user + itemName + amount\" (ex.: \"give @AlbertinoDias rope 5\", to add 5 ropes, and item with multiple words need to be inside quotes, ex.: \"max revive\")")
    
    @commands.has_role("Dias")
    @bot_commands.command()
    async def wipe(message, name):
        # checks if the inittial message is a user message (avoids infinite loops)
        if message.author == bot_commands.user:
            return
        
        # as mentios are in this format "<@XXXXXXXXXX>" where X are numbers, using [2:-1] we can
        # get everything inside the string starting from the 2º character until 1 less of the end 
        friendID = name[2:-1]
        await inventory_wipe(message, friendID,is_private=False)  
             

# ------------------------------------------------
# section that handles xp
# ------------------------------------------------  
    

    @bot_commands.command()
    async def xp(message, *arguments):
        # checks if the inittial message is a user message (avoids infinite loops)
        if message.author == bot_commands.user:
            return
        
        # checks the number of arguments, if they are a multiple of 3, calls the "give_xp" function 
        # and if they are not a multiple of 3, returns a string saying the format is wrong.
        # To ensure eveything works correctely, every third word is checked to see if it starts with 
        # "€"followed by a number without spaces adn the otehr words are checked to see if they are numeric
        print(len(arguments))
        print(len(arguments) % 3)
        if (len(arguments) % 3) == 0:
            
            i = 0
            placeholderList = []
            checkIfFormatted = True
            
            for word in arguments:
                 

                
                placeholderList.append(word)
                if i < 3:

                    if len(placeholderList) == 3:
                        if not placeholderList[1].isnumeric() and not placeholderList[2].isnumeric(): 
                            checkIfFormatted = False
                        placeholderList.clear()
                else:
                    if len(placeholderList) == 3:
                        if placeholderList[0][0] != "€" and not placeholderList[1].isnumeric() and not placeholderList[2].isnumeric(): 
                            checkIfFormatted = False
                        placeholderList.clear()
                i+=1
                    
            
            if checkIfFormatted == True:
                await show_xp(message, arguments)                
            else:   
                await message.channel.send("wrong format, write \"€xp + SR + lvl + ammount\" where SR is the species rarity and amount the quantity of monsters battled of that SR and lvl, for more than 1 SR/lvl pairing use: \"€xp + SR + LvL + Ammount + €SR + LvL + Ammount\" note that the new SR is not spaced, you can repeat this how many times you'd like ex.: \"€xp 2 5 1 €3 3 1 €1/2 2 2\"")    

        else: await message.channel.send("wrong format, write \"€xp + SR + lvl + ammount\" where SR is the species rarity and amount the quantity of monsters battled of that SR and lvl, for more than 1 SR/lvl pairing use: \"€xp + SR + LvL + Ammount + €SR + LvL + Ammount\" note that the new SR is not spaced, you can repeat this how many times you'd like ex.: \"€xp 2 5 1 €3 3 1 €1/2 2 2\"")    

    
    

    # makes the bot work based on the token provided
    bot_commands.run(TOKEN)

