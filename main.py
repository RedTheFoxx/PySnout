import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


TOKEN = "..."


@bot.event
async def on_ready():
    print("PySnout est en ligne !")


@bot.command("play")
async def play(ctx):
    await ctx.send("Bientôt, je diffuserais de l'audio ! :musical_note:")

bot.run(TOKEN)
