# Documentation

1. Setup

-To get an API, you need to go to https://discord.com/developers/applications and create a new application.
-Within your newly created application you will look to the left side of your screen and select "Bot" 
-After choosing a name for your bot, and a profile picture to represent it, you will click the button called "click to reveal token", copy that and be prepared to add it to your code. The best way to integrate it with your code is to create a file in the same project folder named .env, and create a variable in there such as DISCORD_TOKEN="YOURTOKEN"
-Referencing your token in python is easily done with TOKEN = os.getenv('DISCORD_TOKEN'), and the benefit of the .end file is that you can easily add it to your .gitignore list, because otherwise Discord will delete your token if it's published to github.
 
 2. Usage
 
 -The messaging portion of this project was updated so that it outputs quotes from books and authors that I enjoy, if the command "quote" is used.
 -Images can now be sent by the bot if you use the command "dog". This command outputs a randomly chosen picture of a dog saved in the projects folder. Here is the code related to that: 
 
  dogs = [
        'goodboy1.jpg',
        'goodboy2.jpg',
        'goodboy3.png',
    ]
    
     if message.content == 'dog':
        chosenDog = random.choice(dogs)
        await message.channel.send(file=discord.File(chosenDog)
        )
        
3. Research

-PM2 is a good option for keeping a bot running all the time on an AWS instance. PM2 allows ubuntu users to daemonize applications, which means that they will run as a background service on the users machine. This would be perfect for a lightweight discord bot that could be left running on an AWS instance for 24/7 usage in a discord server. 

-Raspberry Pi boards are another great option for keeping a discord bot online 24/7. Discord bots normally don't require too much computing power, if they're just being used for a couple of servers, so you could pick up a Raspberry Pi board for $50 and set up your Discord Bot on it. 
