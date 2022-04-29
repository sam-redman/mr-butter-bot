# -------------------------- MODULES -------------------------- #

from discord.ext import commands

import os
from dotenv import load_dotenv

# -------------------------- MISC -------------------------- #

# Load the .env file in.
load_dotenv()

# -------------------------- BOT SETUP -------------------------- #

# Creates a client for the bot.
bot = commands.Bot(debug_guilds=[690154666474209285])


@bot.event
# Simple confirmation that the bot is running.
async def on_ready():
    # Console feedback.
    print(f"We have logged in as {bot.user}.")

# Load cogs extensions.
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        bot.load_extension("cogs." + file[:-3])
        print(f"{file} cog has loaded.")

# -------------------------- RUN BOT -------------------------- #

# Run the bot with the token from the .env.
bot.run(os.environ['BOT_TOKEN'])
