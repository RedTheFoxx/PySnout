import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "MTA1MDU4NTA4ODI2MzQ2Mjk2NA.G1VIM_.zM24VrWVwjOng10o2D_cxaa6-hP94jzZTSsPG0"


@bot.event
async def on_ready():
    print("PySnout est en ligne !")


bot.run(TOKEN)
