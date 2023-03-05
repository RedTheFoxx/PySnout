import discord
from discord.ext import commands
from engine import *

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "TOKEN_HERE"


@bot.event
async def on_ready():
    print("PySnout est en ligne !")


bot.run(TOKEN)
