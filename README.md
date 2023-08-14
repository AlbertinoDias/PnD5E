# PnD5E
 Discord bot to facilitate a monster-catching DnD campaign
<header>
<h1>Hello and welcome to PnD5E</h1>
This is a bot created to help a dungeon master run a Dungeons and Dragons(DnD) homebrew campaign. I am new to dungeons and dragons and no one in my group has ever been a dungeon master, because of that, I decided to create a bot to help me get some key information without having to search through the books and keep the game running. The bot was created for me and might not be useful for everyone, especially for a veteran dungeon master.
 Since this bot was created with me in mind as the final user and for only 1 server, some of the logic behind it is not necessarily the most versatile, ex.: the inventory is a .csv file that has the user Discord ID as the name and the bot does not check for the server ID, which means the user file will be shared across servers.
 <h4>As of 14/08/2023 the bot is considered completed, Until I run a game of DnD with it, I will not update it as I don't know if my thoughts about what I will need are correct or not.<h4>

<h1>How to try the bot</h1>

To try the bot, you first need to get a Discord token. Go to the Discord developer portal and create a bot (you can follow any tutorial you can find online).
Once you've created the bot, click on these options and generate your token:
![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/27cf4b26-e503-480f-963d-a8c9eee98004)


after this is done, go to the .env file and switch the string with your Token


<h1>What can the bot do?</h1>

<h2>€roll</h2>

Use "€roll + pvt + number" for a dm or "€roll + number" for a response on the channel, then the bot will give you a random number between 1 and the number you chose

![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/7dba3f27-cfd9-4c82-bf71-f161f9f83542)

<h2>€comands</h2>

Use "€comands" to list the commands you can use

![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/c0d0eb7d-14ef-4e7f-8d09-b362277998a2)

<h2>€move</h2>

Use "€move + name" where "name" has to be an exact match of a move, if the move has 2 names you have to put it inside quotes ("")

![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/200409b6-729a-4b43-8cb6-52e20a6cd2c3)

<h2>€any</h2>

Use "€any + keyword + name"</h3> to search every move to see if the name is inside (does not need to be an exact match) the keyword parameter

![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/d6fe35bb-4fd2-4857-ae6c-f7a36e500af7)

<h2>€keywords</h2>

Use "€keywords" to list the keywords you can use for "€any"

![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/78cc6dfe-f161-487e-a209-259406c91030)

<h2>€inventory</h2>

Use "€inventory" to list your inventory, if you don't have one yet, it is created

![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/d856ce05-589c-45b8-94bb-93826beff348)

<h2>€add</h2>

Use "€add + name + amount" to add the amount of the name to your inventory, if the move has 2 names you have to put it inside quotes ("")

![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/5d06d175-7b0e-4445-aa0b-993502cf7151)

<h2>€use</h2>

Use "€use + name + amount" to remove the amount of the name from your inventory, if the item has 2 names you have to put it inside quotes (""), if you put a number above the one in your inventory, it removes the item from the inventory instead of subtracting the number

![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/d1fa2f5a-a116-4bbb-b0dc-668f4282ef07)

<h2>€give</h2>

Use "€give + mention + name + amount" to give an X amount of the item you chose to someone you mention, if the item has 2 names you have to put it inside quotes (""), you need to have a sufficient amount of items to trade otherwise it will not work

![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/3b196d54-25cb-4af5-811b-46ea3c1cdbf1)

<h2>€wipe</h2>

Use "wipe + mention" to remove an inventory from the mentioned player, this command is role restricted and the role should be specified inside the code

![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/086f61b1-fe8f-4c40-9b17-5bf5c4d8eb8d)

<h2>€xp</h2>

Use "XP + SR + LvL + amount", SR (species rating of the monster) and LvL (the level of the monster) are values present in a document not available in the repository but they go from 1 to 15 and 1 to 20 respectively, and the amount is the number of monsters that have that SR+LvL pairing. you can put more than 1 set of 3 values given that every time you start a new set you use "€" before the number without spaces like.: "XP + SR + LvL + amount + €SR + LvL + amount"

![image](https://github.com/AlbertinoDias/PnD5E/assets/36789123/f33a257a-36e8-461d-b201-bf4f2934b7f5)

</header>
