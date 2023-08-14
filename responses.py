import random
import csv
import os.path


# ------------------------------------------------
# section that handles inventory
# ------------------------------------------------
# The inventory save file (.csv) is indiidualy created for each user, the name is the users discord ID
# it is saved in a folder but it does not check for server id, meaning it is shared across servers! (or guilds by the new discord sintax)

# function that lists the user inventory 
def list_inventory(userId):
    
    # list created as a placeholder for the items name and quantity to then print
    nameList = []
    # csv headers
    name = ""
    amount = ""

    # searches for a folder (inventories) in the current directory and if there's a csv file with the user id as name, opens it  
    if os.path.isfile("inventories/"+str(userId)+".csv"):
        #opens the csv, saves the csv data (csvFile)into a variable (csvData) 
        #then transforms that data into a list of lists (moves_list), separated by comas
        csv_file = open("inventories/"+str(userId)+".csv", "r", encoding="utf-8")
        csv_Data = csv.reader(csv_file)
        # skips the header in the csv
        inventory = list(csv_Data)[1:]

        # for each line inside the csv, write that line in the placeholder list
        for line in inventory:
            name = line[0]
            amount = line[1]
            nameList.append(amount + ":   "+ name)
        # if the placehodler list is not empty, call the "list_a_list" function, otherwise, say that the inventory is pprobably empty
        if  nameList:  
            return list_a_list(nameList)
        else: return str("inventory is probably empty")
    # if no file is found in that directory, call the "create_inventory" function
    else:
        return create_inventory(userId)

# function to add an "X" amount of an item to the user inventory
def add_to_inventory(userId, itemName, itemAmount):
    # to avoid problems with capitalization, the name of the item is checked in lowercase
    itemName = itemName.lower()
    # lists created as a placeholder for the items name and quantity of both user to then write on the .csv
    intermediaryList = []
    # bool used to track if the item already exists in the inventory or not
    oldEntry = False
    
    
    # searches for a folder (inventories) in the current directory and if there's a csv file with the user id as name, opens it  
    if os.path.isfile("inventories/"+str(userId)+".csv"):
        
        # opens the csv, saves the csv data (csvFile)into a variable (csvData) 
        # then transforms that data into a list of lists (moves_list), separated by comas
        csv_file = open("inventories/"+str(userId)+".csv", "r", encoding="utf-8")
        csv_Data = csv.reader(csv_file)
        inventory = list(csv_Data)


        # for each line in the .csv file, if the first element (name) in lower case is an exact match to the item name the user
        # submitted, then it gets the amount that exists of that item in the inventory and adds the amount the user specified
        # ,turning the "oldEntry" boolean true (if this happens, the item name and new ammmount is added to a placeholder list)
        # otherwise the "oldEntry" keeps it's False state and adds the line without changes to the placeholder list.
        for line in inventory:
            if line[0].lower() == itemName:
                amount = str( (int(line[1]) + int(itemAmount) ))
                intermediaryList.append(itemName + ","+ amount)
                oldEntry = True
            else: 
                name = line[0]
                amount = line[1]
                intermediaryList.append(name + ","+ amount)
        # checks if the item is a new item by checking if the "oldEntry" boolean kept it's False status and if so, adds the item and 
        # amount the user specified to the placeholder list
        if oldEntry == False:
            intermediaryList.append(itemName + ","+ itemAmount)
        csv_file.close()

        csv_file = open("inventories/"+str(userId)+".csv", "w", encoding="utf-8")
    # for each line in the placeholder list, write a line in the original .csv (will substitute everything since we open the .csv with "W")
        for line in intermediaryList:
            csv_file.write(line + "\n")
        return str("inventory updated, to check the new inventory type \"€inventory\"")
    # if no file is found in that directory, call the "create_inventory" function
    else:
        return create_inventory(userId)

# function to remove an "X" amount of an item from the user inventory
def use_from_inventory(userId, itemName, itemAmount):
    # to avoid problems with capitalization, the name of the item is checked in lowercase 
    itemName = itemName.lower()
    # lists created as a placeholder for the items name and quantity of both user to then write on the .csv
    intermediaryList = []
    # bool used to track if the item already exists in the inventory or not
    oldEntry = False

    # searches for a folder (inventories) in the current directory and if there's a csv file with the user id as name, opens it  
    if os.path.isfile("inventories/"+str(userId)+".csv"):

        # opens the csv, saves the csv data (csvFile)into a variable (csvData) 
        # then transforms that data into a list of lists (moves_list), separated by comas
        csv_file = open("inventories/"+str(userId)+".csv", "r", encoding="utf-8")
        csv_Data = csv.reader(csv_file)
        inventory = list(csv_Data)


        # for each line in the .csv file, if the first element (name) in lower case is an exact match to the item name the user
        # submitted, then it gets the amount that exists of that item in the inventory and subtracts the amount the user specified
        # ,turning the "oldEntry" boolean true (if this happens and the amount is greater than 0, the item name and new ammmount is 
        # added to a placeholder list, if the amount is 0, then it is not added to the placeholder list in order to be removed)
        # otherwise the "oldEntry" keeps it's False state and adds the line without changes to the placeholder list.
        for line in inventory:
            
            if line[0].lower() == itemName:
                amount = str( (int(line[1]) - int(itemAmount) ))
                if int(amount) > 0:
                    intermediaryList.append(itemName + ","+ amount)
                    oldEntry = True
                elif int(amount) == 0:
                    oldEntry = True
            else: 
                name = line[0]
                amount = line[1]
                intermediaryList.append(name + ","+ amount)
            

        csv_file.close()
        
        #if the item existed in the inventory, open the .csv and replace eveything with the placeholder list otherwise, says that 
        # there was no such item in the inventory
        if oldEntry == True:
    
            csv_file = open("inventories/"+str(userId)+".csv", "w", encoding="utf-8")

            for line in intermediaryList:
                csv_file.write(line + "\n")
            return str("inventory updated, to check the new inventory type \"€inventory\"")
        else: return str("there's no such item in the inventory")
    # if the file does not exist, create a new inventory    
    else:
        return create_inventory(userId)

# function that removes an "X" amount of an item from the user inventory and add it to the inventory of another user
def give_item(userId, friendID, itemName, itemAmount):

    # to avoid problems with capitalization, the name of the item is checked in lowercase 
    itemName = itemName.lower()
    # lists created as a placeholder for the items name and quantity of both user to then write on the .csv
    intermediaryListUser = []
    intermediaryListFriend = []
    # bool used to track if the item already exists in both inventories or not
    oldEntryUser = False
    oldEntryFriend = False



    # searches for a folder (inventories) in the current directory and if there's a csv file with the user id as name, and 
    # another that has the user that was tagged id, opens the user id  
    if os.path.isfile("inventories/"+str(userId)+".csv") and os.path.isfile("inventories/"+str(friendID)+".csv"):

        csv_file_user = open("inventories/"+str(userId)+".csv", "r", encoding="utf-8")
        csv_Data_user = csv.reader(csv_file_user)
        inventory_user = list(csv_Data_user)
        amount = ""

        # for each line in the .csv file, if the first element (name) in lower case is an exact match to the item name the user
        # submitted, then it gets the amount that exists of that item in the inventory and subtracts the amount the user specified
        # ,turning the "oldEntry" boolean for the user true. If this happens and the amount is greater than 0, the item name and new ammmount is 
        # added to a placeholder list, if the amount is 0, then it is not added to the placeholder list in order to be removed, but if it is lower than 0
        # then it returns a msg saying the amount to give needs to be lowered and interrupts the funtion, if the item is not the correct one,
        # the "oldEntry" keeps it's False state and adds the line without changes to the placeholder list.
        for line in inventory_user:
            if line[0].lower() == itemName:
                amount = str( (int(line[1]) - int(itemAmount) ))
                if int(amount) < 0:
                    return str("not enough items, pls try again with a lower ammount")
                elif int(amount) > 0:
                    intermediaryListUser.append(itemName + "," + amount)    
                    oldEntryUser = True
                elif int(amount) == 0:
                    oldEntryUser = True
            else: 
                name = line[0]
                amount = line[1]
                intermediaryListUser.append(name + ","+ amount)
        print("amount" + amount)
            
        
        csv_file_user.close()
        # if the item was found in the user inventory, opens the mentioned user inventory 
        if oldEntryUser == True:
            csv_file_friend = open("inventories/"+str(friendID)+".csv", "r", encoding="utf-8")
            csv_Data_friend = csv.reader(csv_file_friend)
            inventory_friend = list(csv_Data_friend)


        # for each line in the .csv file, if the first element (name) in lower case is an exact match to the item name the user
        # submitted, then it gets the amount that exists of that item in the inventory and adds the amount the user specified,
        # turning the "oldEntry" boolean for the mentioned user true (if this happens, the item name and new ammmount is added to 
        # a placeholder list) otherwise the "oldEntry" keeps it's False state and adds the line without changes to the placeholder list.
            for line in inventory_friend:

                if line[0].lower() == itemName:
                    amount = str( (int(line[1]) + int(itemAmount) ))
                    intermediaryListFriend.append(itemName + "," + amount)    
                    oldEntryFriend = True
                else: 
                    name = line[0]
                    amount = line[1]
                    intermediaryListFriend.append(name + ","+ amount)
            # replaces the old inventory with the inventory in the palceholder list for the user
            csv_file_user = open("inventories/"+str(userId)+".csv", "w", encoding="utf-8")
            for line in intermediaryListUser:
                    csv_file_user.write(line + "\n")
            #if there was already the item in question in the mentioned user inventory, it replaces the .csv inventory with the one
            # inside the placehodler list for the mentioned userm otherwise, it just adds a new line with the item anme and amount 
            # to the old .csv.
            if oldEntryFriend == True:

                
                csv_file_friend = open("inventories/"+str(friendID)+".csv", "w", encoding="utf-8")

                for line in intermediaryListFriend:
                    csv_file_friend.write(line + "\n")
                return str("inventory updated, to check the new inventory type \"€inventory\"")
            else: 
                csv_file_friend = open("inventories/"+str(friendID)+".csv", "a", encoding="utf-8")
                csv_file_friend.write("\n" + itemName + ","+ itemAmount)
                return str("inventory updated, to check the new inventory type \"€inventory\"")
        #if it fails, it means the item does not exist in the user inventory
        else: return str("there's no such item in your inventory")
    # checks if the file that does not exist is the user's and if so, creates an inventory .csv file for them
    elif not os.path.isfile("inventories/"+str(userId)+".csv"):
        return create_inventory(userId)
    # checks if the file that does not exist is the tagged user's and if so, creates an inventory .csv file for them
    elif not os.path.isfile("inventories/"+str(friendID)+".csv"):
        return create_inventory(friendID)
    # if none of the above worked, i have no idea what happened...
    else: return str("idk what's happening, sorry")

# function that whipes the inventory of the mentioned user (should be reserved for moderators)
def wipe_invetory(friendID):
    csv_file = open("inventories/"+str(friendID)+".csv", "w", encoding="utf-8")
    csv_file.write("Name,Amount")
    return str("inventory was wipped")

# creates an inventory for a user if they didn't have one already.
def create_inventory(userId):

    csv_file = open("inventories/"+str(userId)+".csv", "w", encoding="utf-8")
    csv_file.write("Name,Amount")
    return str("no prior inventory, a new one was created, but it's empty")


# ------------------------------------------------
# section that handles commands information 
# ------------------------------------------------

# prints a list of the keywords a user can use with the "any" command
keywordList = ["type", "power", "time", "pp", "duration", "range", "save"]
def list_keywords():
    return list_a_list(keywordList)

# prints a list of the commands a user can use (besides this one)
commandList = ["roll", "move", "keywords", "any", "give", "use", "add", "xp"]
def list_commands():
    return list_a_list(commandList)


# ------------------------------------------------
# section that handles misc commands 
# ------------------------------------------------


# returns a number between 1 and the number given as a string
def dice_roll(number):     
    # checks if he number is not written with letters
    if number.isnumeric():
        return str(random. randint(1, int(number)))        
    
    else: return str("that's not a number")

# ------------------------------------------------
# section that handles moves
# ------------------------------------------------


# searches the moves csv to compare a variable to the name parameter and returns every information 
# from it (has to be a unique parameter) in a string format
def list_move(moveName):
    moveName = moveName.lower()
    
    # csv headers
    name = ""
    moveType = ""
    movePower = ""
    moveTime = ""
    pp = ""
    duration = ""
    moveRange = ""
    description = ""
    higherLevels = ""

    #opens the csv, saves the csv data (csvFile)into a variable (csvData) 
    #then transforms that data into a list of lists (moves_list), separated by comas
    csv_file = open("moves.csv", "r", encoding="utf-8")
    csv_Data = csv.reader(csv_file)
    moves_list = list(csv_Data)

    # runs every line of the csv
    for line in moves_list:
        
        # gives the variable name the information of the first thing in the line of the csv
        name = line[0].lower()

        # if the name searched is the same as the name in the line, it momentarely saves the 
        # information on variables and then return them in a string
        if name == moveName:
            moveType = line[1]
            movePower = line[2]
            moveTime = line[3]
            pp = line[4]
            duration = line[5]
            moveRange = line[6]
            description = line[7]
            higherLevels = line[8]
            save = line[9]
            print(str(f"Name: {name}\n Move Type: {moveType}\n Move Power: {movePower}\n Move Time: {moveTime}\n pp: {pp}\n duration: {duration}\n Move Range: {moveRange}\n Description: {description}\n Higher Levels: {higherLevels}\n Save: {save} \n"))
            return str(f"Name: {name}\n Move Type: {moveType}\n Move Power: {movePower}\n Move Time: {moveTime}\n pp: {pp}\n duration: {duration}\n Move Range: {moveRange}\n Description: {description}\n Higher Levels: {higherLevels}\n Save: {save} \n")

    return str("invalid format, if a move has more than one name, put both inside quotes ex.: \"Iron Tale\", the names are case sensitive and need to match perfectely")

# searches the moves csv to compare a variable to a parameter chosen by the user and returns a
#  list with all the names of the moves that have that parameter
def list_moves_by_something(parameter, search):
    parameter = parameter.lower()
    search = search.lower()
    # list to return
    nameList = []
    # csv headers
    name = ""
    moveType = ""
    movePower = ""
    moveTime = ""
    pp = ""
    duration = ""
    moveRange = ""
    save = ""
    #opens the csv, saves the csv data (csvFile)into a variable (csvData) 
    #then transforms that data into a list of lists (moves_list), separated by comas
    csv_file = open("moves.csv", "r", encoding="utf-8")
    csv_Data = csv.reader(csv_file)
    moves_list = list(csv_Data)

    # runs every line of the csv
    for line in moves_list:
        
        # assigns the variable to the matching information of the line
        name = line[0].lower()
        moveType = line[1].lower()
        movePower = line[2].lower()
        moveTime = line[3].lower()
        pp = line[4].lower()
        duration = line[5].lower()
        moveRange = line[6].lower()
        save = line[9].lower()
        #print(f"lista: {nameList} , parametro: {parameter}, o que procurar: {search}, name = {name} moveType = {moveType} movePower = {movePower} moveTime = {moveTime} pp = {pp} duration = {duration} moveRange = {moveRange}")

        # checks the parameter written by the user and based on that comapres the 
        # content of the rest of what was wrriten to what the line of the csv has 
        # and if it is a match, adds the name of the move to a list
        if parameter == "type":
            if search in moveType:
                nameList.append("\""+name+"\"")
        elif parameter == "power":
            if search in movePower:
                nameList.append("\""+name+"\"")
        elif parameter == "time":
            if search in moveTime:
                nameList.append("\""+name+"\"")       
        elif parameter == "pp":
            if search in pp:
                nameList.append("\""+name+"\"")
        elif parameter == "duration":
            if search in duration:
                nameList.append("\""+name+"\"")
        elif parameter == "range":
            if search in moveRange:
                nameList.append("\""+name+"\"")
        elif parameter == "save":
            if search in save:
                nameList.append("\""+name+"\"")
    if  nameList:  
            return list_a_list(nameList)
    else: return str("invalid format, write \"€any + pvt + Keyword + SearchWord\" for a dm or \"€any + Keyword + SearchWord\" for a public list (ex.: \"any pvt type Fighting\", use command \"€keywords\" to see the list of keywords, multiple search words need to be inside quotes, and remember it is caps sensitive)")



# ------------------------------------------------
# section that handles moves
# ------------------------------------------------

# creates a matrix based on a .csv file and then uses the matrix to calculate the xp value based on 
# the amount of arguments the user passed, the number of arguments have to be multiples of 3
def give_xp(arguments):


    #opens the csv, saves the csv data (csvFile) into a variable (csvData) 
    #then transforms that data into a list of lists (xpList), separated by comas
    csv_file = open("xpTable.csv", "r", encoding="utf-8")
    csv_Data = csv.reader(csv_file)
    xpList = list(csv_Data)


    xp = 0
    # variable to help count the number of iterations so the frist 3 are different
    i = 0
    placeholderList = []
    # variable to store the column to take from the .csv
    placeholderHeader = 0
    for word in arguments:
        
        # every number is placed in a placeholder list, if there are 3 elements on a lsit 
        # and it is part of the first 3 iterations, compares the value given by the user 
        # for the SR (first string in every 3 iterations) and if it get's a match, 
        # then thecolumn number is saved
        placeholderList.append(word)
        if i <  3:
            if len(placeholderList) == 3:
                if placeholderList[0] == "1/8": 
                    placeholderHeader = 1
                elif placeholderList[0] == "1/4": 
                    placeholderHeader = 2
                elif placeholderList[0] == "1/2": 
                    placeholderHeader = 3
                elif placeholderList[0] == "1": 
                    placeholderHeader = 4
                elif placeholderList[0] == "2": 
                    placeholderHeader = 5
                elif placeholderList[0] == "3": 
                    placeholderHeader = 6
                elif placeholderList[0] == "4": 
                    placeholderHeader = 7
                elif placeholderList[0] == "5": 
                    placeholderHeader = 8
                elif placeholderList[0] == "6": 
                    placeholderHeader = 9
                elif placeholderList[0] == "7": 
                    placeholderHeader = 10
                elif placeholderList[0] == "8": 
                    placeholderHeader = 11
                elif placeholderList[0] == "9": 
                    placeholderHeader = 12
                elif placeholderList[0] == "10": 
                    placeholderHeader = 13
                elif placeholderList[0] == "11": 
                    placeholderHeader = 14
                elif placeholderList[0] == "12": 
                    placeholderHeader = 15
                elif placeholderList[0] == "13": 
                    placeholderHeader = 16
                elif placeholderList[0] == "14": 
                    placeholderHeader = 17
                elif placeholderList[0] == "15": 
                    placeholderHeader = 18
                else: return str("aaawrong format, write \"€xp + SR + lvl + ammount\" where SR is the species rarity and amount the quantity of monsters battled of that SR and lvl, for more than 1 SR/lvl pairing use: \"€xp + SR + LvL + Ammount + €SR + LvL + Ammount\" note that the new SR is not spaced, you can repeat this how many times you'd like ex.: \"€xp 2 5 1 €3 3 1 €1/2 2 2\"")

            # compares the value given by the user for the lvl (second string in every 3 iterations) 
            # and if it get's a match, it uses that value as a row alongside the placeholder (column) 
            # to get the correct number of the matrix and multiply it by the number given by the user 
            # adding the total to a varialble "xp"
                if placeholderList[1] == "1": 
                    xp += int(xpList[1][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "2": 
                    xp += int(xpList[2][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "3": 
                    xp += int(xpList[3][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "4": 
                    xp += int(xpList[4][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "5": 
                    xp += int(xpList[5][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "6": 
                    xp += int(xpList[6][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "7": 
                    xp += int(xpList[7][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "8": 
                    xp += int(xpList[8][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "9": 
                    xp += int(xpList[9][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "10": 
                    xp += int(xpList[10][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "11": 
                    xp += int(xpList[11][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "12": 
                    xp += int(xpList[12][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "13": 
                    xp += int(xpList[13][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "14": 
                    xp += int(xpList[14][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "15": 
                    xp += int(xpList[15][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "13": 
                    xp += int(xpList[16][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "17": 
                    xp += int(xpList[17][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "18": 
                    xp += int(xpList[18][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "19": 
                    xp += int(xpList[19][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "20": 
                    xp += int(xpList[20][placeholderHeader]) * int(placeholderList[2])
                else: return str("aaawrong format, write \"€xp + SR + lvl + ammount\" where SR is the species rarity and amount the quantity of monsters battled of that SR and lvl, for more than 1 SR/lvl pairing use: \"€xp + SR + LvL + Ammount + €SR + LvL + Ammount\" note that the new SR is not spaced, you can repeat this how many times you'd like ex.: \"€xp 2 5 1 €3 3 1 €1/2 2 2\"")
                # cleans the list so it get's the next 3 iterations
                placeholderList.clear()
        else:
            # if there are 3 elements on a lsit and it is not part of the first 3 iterations,
            # compares the value given by the user for the SR (first string in every 3 iterations) 
            # without the first letter (as it should be "€") and if it get's a match, then the column number is saved

            if len(placeholderList) == 3:
                if placeholderList[0][1:] == "1/8": 
                    placeholderHeader = 1
                elif placeholderList[0][1:] == "1/4": 
                    placeholderHeader = 2
                elif placeholderList[0][1:] == "1/2": 
                    placeholderHeader = 3
                elif placeholderList[0][1:] == "1": 
                    placeholderHeader = 4
                elif placeholderList[0][1:] == "2": 
                    placeholderHeader = 5
                elif placeholderList[0][1:] == "3": 
                    placeholderHeader = 6
                elif placeholderList[0][1:] == "4": 
                    placeholderHeader = 7
                elif placeholderList[0][1:] == "5": 
                    placeholderHeader = 8
                elif placeholderList[0][1:] == "6": 
                    placeholderHeader = 9
                elif placeholderList[0][1:] == "7": 
                    placeholderHeader = 10
                elif placeholderList[0][1:] == "8": 
                    placeholderHeader = 11
                elif placeholderList[0][1:] == "9": 
                    placeholderHeader = 12
                elif placeholderList[0][1:] == "10": 
                    placeholderHeader = 13
                elif placeholderList[0][1:] == "11": 
                    placeholderHeader = 14
                elif placeholderList[0][1:] == "12": 
                    placeholderHeader = 15
                elif placeholderList[0][1:] == "13": 
                    placeholderHeader = 16
                elif placeholderList[0][1:] == "14": 
                    placeholderHeader = 17
                elif placeholderList[0][1:] == "15": 
                    placeholderHeader = 18
                else: return str("aaawrong format, write \"€xp + SR + lvl + ammount\" where SR is the species rarity and amount the quantity of monsters battled of that SR and lvl, for more than 1 SR/lvl pairing use: \"€xp + SR + LvL + Ammount + €SR + LvL + Ammount\" note that the new SR is not spaced, you can repeat this how many times you'd like ex.: \"€xp 2 5 1 €3 3 1 €1/2 2 2\"")

                # compares the value given by the user for the lvl (second string in every 3 iterations) 
                # and if it get's a match, it uses that value as a row alongside the placeholder (column) 
                # to get the correct number of the matrix and multiply it by the number given by the user 
                # adding the total to a varialble "xp"
                if placeholderList[1] == "1": 
                    xp += int(xpList[1][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "2": 
                    xp += int(xpList[2][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "3": 
                    xp += int(xpList[3][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "4": 
                    xp += int(xpList[4][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "5": 
                    xp += int(xpList[5][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "6": 
                    xp += int(xpList[6][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "7": 
                    xp += int(xpList[7][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "8": 
                    xp += int(xpList[8][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "9": 
                    xp += int(xpList[9][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "10": 
                    xp += int(xpList[10][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "11": 
                    xp += int(xpList[11][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "12": 
                    xp += int(xpList[12][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "13": 
                    xp += int(xpList[13][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "14": 
                    xp += int(xpList[14][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "15": 
                    xp += int(xpList[15][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "13": 
                    xp += int(xpList[16][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "17": 
                    xp += int(xpList[17][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "18": 
                    xp += int(xpList[18][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "19": 
                    xp += int(xpList[19][placeholderHeader]) * int(placeholderList[2])
                elif placeholderList[1] == "20": 
                    xp += int(xpList[20][placeholderHeader]) * int(placeholderList[2])
                else: return str("aaawrong format, write \"€xp + SR + lvl + ammount\" where SR is the species rarity and amount the quantity of monsters battled of that SR and lvl, for more than 1 SR/lvl pairing use: \"€xp + SR + LvL + Ammount + €SR + LvL + Ammount\" note that the new SR is not spaced, you can repeat this how many times you'd like ex.: \"€xp 2 5 1 €3 3 1 €1/2 2 2\"")
                # resets the placeholder lsit to get the next 3 iterations
                placeholderList.clear()
        i+=1    
    return str(f"the amount of xp to divide is : {xp}") 
        

# ------------------------------------------------
# section that handles utilities
# ------------------------------------------------


# returns a string with every entry on a list given that each entry is given in a new line
def list_a_list(listToList):
    newString = ""
    for item in listToList:
        newString += item 
        newString += "\n"
    return newString