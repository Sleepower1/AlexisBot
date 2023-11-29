import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import os
from keep_alive import keep_alive
import random
from generate_meme import generate_meme
keep_alive()
bot_token = 'MTE3Njg3MjIyNzQwMTEwNTQ4MA.GZzNgR.qB600iZ8Z8N-xp4emWT43VYCtsM2Ce9ktFWh5k'

allowed_user_id = ['525108125615783966','445819178151313428']

# Define the intents
intents = discord.Intents.default()
intents.message_content = True  # Add this line if you want to access message content

# Create an instance of the bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)
affirmations = {0:"Every day in every way I am getting better, better and better",
                1:"I am grateful for the opportunity to be alive",
               2:"I’m grateful to the people who I have met, each one of them have shaped me into who I am today",
               3:"I am fei Chang generic",
               4:"Time is not a waste of life and life is not a waste of time so let’s get wasted and have the time of our lives\n-Pitbull",
               5:"The world is cruel, therefore I won’t be"}
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Check if the message is from the specific user
    message.content = message.content.lower()
    if str(message.author.id) in allowed_user_id and "hate" in message.content.split():
        # Respond with a specific phrase
        await generate_meme(message.content, message.channel)
        num = random.randrange(0,len(affirmations))
        await message.channel.send("<@" + str(445819178151313428) + "> "+affirmations[num])
        #await message.channel.send("<@" + str(525108125615783966) + ">")
    elif str(message.author.id) == '284274156399362048' and message.content == "ping":
        await message.channel.send('Hello! This is a specific response for you.')

    # Let the bot process commands as well
    await bot.process_commands(message)

# Run the bot with the token
bot.run(bot_token)
