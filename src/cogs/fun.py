# -------------------------- MODULES -------------------------- #
import discord
from discord.ext import commands

import random
import requests

# -------------------------- FUN COMMANDS -------------------------- #


# This is a special method that is called when the cog is loaded.
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(guild_ids=[690154666474209285], name='hellothere', description='Responds with a greeting')
    async def hellothere(self, ctx):
        response = 'General Kenobi'
        await ctx.respond(response)

    @discord.slash_command(guild_ids=[690154666474209285], name='roll', description='Roll between two numbers')
    async def roll(self, ctx, num1: int, num2: int):
        response = random.randrange(num1, num2 + 1)
        await ctx.respond(response)

    @discord.slash_command(guild_ids=[690154666474209285], name='eightball', description='Consult the magic 8ball')
    async def eightball(self, ctx):
        outcomes = ['Yes', 'No', 'Maybe', 'It\'s not that deep', 'Oh shoot, I forgot my crystal ball', 'Beans',
                    'Concentrate and ask again', 'Doubt it', '50/50', 'That\'s a no chief', 'Absolutely',
                    'You\'re not that guy pal', 'Trust me']
        response = random.choice(outcomes)
        await ctx.respond(response)

    @discord.slash_command(guild_ids=[690154666474209285], name='kanye', description='Random Kanye West quote')
    async def kanye(self, ctx):
        # Contact the API.
        api_response = requests.get(url="https://api.kanye.rest")
        # Capture the data in a .json.
        data = api_response.json()
        # Narrow the data down from the .json dictionary.
        response = data["quote"]
        await ctx.respond(f"{response} - Kanye West")

    @discord.slash_command(guild_ids=[690154666474209285], name='story', description='The tragedy of Darth Plagueis The Wise')
    async def story(self, ctx, member: discord.Member):
        response = '"Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It\'s not a story the Jedi would tell you. It\'s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself." - Sheev Palpatine or Darth Sidious.'
        await ctx.respond(f"{member.mention}\n\n{response}")


def setup(bot):
    bot.add_cog(Fun(bot))
