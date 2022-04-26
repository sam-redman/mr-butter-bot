# -------------------------- MODULES -------------------------- #

# Discord modules.
import discord
from discord.ext import commands

# Regular modules.
import os
from dotenv import load_dotenv
import random
import requests

# -------------------------- MISC -------------------------- #

# Load the .env file in.
load_dotenv()

# -------------------------- BOT SETUP -------------------------- #

# Creates a client for the bot. prefix & command not needed when moved to slash commands.
bot = commands.Bot()


@bot.event
# Simple confirmation that the bot is running.
async def on_ready():
    # Set what "game" the bot is "playing".
    await bot.change_presence(activity=discord.Game(name="Are beans real?"))
    # Console feedback.
    print(f"We have logged in as {bot.user}.")
    print("_________________________________________")


# -------------------------- FUN COMMANDS -------------------------- #


@bot.slash_command(guild_ids=[690154666474209285], name='hellothere', description='Responds with a greeting')
async def hellothere(ctx):
    response = 'General Kenobi'
    await ctx.respond(response)


@bot.slash_command(guild_ids=[690154666474209285], name='roll', description='Roll between two numbers')
async def roll(ctx, num1: int, num2: int):
    response = random.randrange(num1, num2+1)
    await ctx.respond(response)


@bot.slash_command(guild_ids=[690154666474209285], name='eightball', description='Consult the magic 8ball')
async def eightball(ctx):
    outcomes = ['Yes', 'No', 'Maybe', 'It\'s not that deep', 'Oh shoot, I forgot my crystal ball', 'Beans', 'Concentrate and ask again', 'Doubt it', '50/50', 'That\'s a no chief', 'Absolutely', 'You\'re not that guy pal', 'Trust me']
    response = random.choice(outcomes)
    await ctx.respond(response)


@bot.slash_command(guild_ids=[690154666474209285], name='kanye', description='Random Kanye West quote')
async def kanye(ctx):
    # Contact the API.
    api_response = requests.get(url="https://api.kanye.rest")
    # Capture the data in a .json.
    data = api_response.json()
    # Narrow the data down from the .json dictionary.
    response = data["quote"]
    await ctx.respond(f"{response} - Kanye West")


@bot.slash_command(guild_ids=[690154666474209285], name='story', description='The tragedy of Darth Plagueis The Wise')
async def story(ctx, member: discord.Member):
    response = '"Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It\'s not a story the Jedi would tell you. It\'s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself." - Sheev Palpatine or Darth Sidious.'
    await ctx.respond(f"{member.mention}\n\n{response}")


# -------------------------- RUN BOT -------------------------- #

# Run the bot with the token from the .env.
bot.run(os.environ['BOT_TOKEN'])