# -------------------------- MODULES -------------------------- #

import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

# -------------------------- MISC -------------------------- #

# Load the .env file in.
load_dotenv()

# -------------------------- BOT SETUP -------------------------- #

# Creates a client for the bot. prefix & command not needed when moved to slash commands.
bot = commands.Bot(debug_guilds=[690154666474209285])


@bot.event
# Simple confirmation that the bot is running.
async def on_ready():
    # Set what "game" the bot is "playing".
    await bot.change_presence(activity=discord.Game(name="Are beans real?"))
    # Console feedback.
    print(f"We have logged in as {bot.user}.")

# Load cogs extensions.
for file in os.listdir("src/cogs"):
    if file.endswith(".py"):
        bot.load_extension("cogs." + file[:-3])
        print(f"{file} cog has loaded.")

# -------------------------- RUN BOT -------------------------- #

# Run the bot with the token from the .env.
bot.run(os.environ['BOT_TOKEN'])
