import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    quotes = [
        '"EASTER HAS BEEN CANCELED - THEY FOUND THE BODY" ― Jim Butcher, Storm Front',
        '“He can move faster than Severus Snape confronted with shampoo.” - JK Rowling, Harry Potter',
        '“Besides Getting my ass kicked, my main accomplishment on this trip has been to massacre an incredible number of completely innocent clothes. I\'m the Joseph Stalin of laundry.” ― Richard Kadrey, Sandman Slim',
        '“If you want to write a negative review, don\'t tickle me gently with your aesthetic displeasure about my work. Unleash the goddamn Kraken." ― Scott Lynch',
    ]

    dogs = [
        'goodboy1.jpg',
        'goodboy2.jpg',
        'goodboy3.png',
    ]

    if message.content == 'quote':
        response = random.choice(quotes)
        await message.channel.send(response)

    if message.content == 'dog':
        chosenDog = random.choice(dogs)
        await message.channel.send(file=discord.File(chosenDog)
        )
client.run(TOKEN)