# Required params :
# ffmpeg + PATH + ffmpeg.exe
# PyNaCl (for audio capablities)
# youtube-dl or yt-dlp (for audio download)

# TODO : add a command to stop the audio
# TODO : download audio via !play command
# TODO : display audio preparation progress in current channel

import discord
from discord.ext import commands

from engine import play_audio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


TOKEN = "..."


@bot.event
async def on_ready():
    print("PySnout est en ligne !")


@bot.command("play")
async def play(ctx):
    await ctx.send("Bientôt, je diffuserais de l'audio ! :musical_note:")
    await play_audio(ctx, 'audio_bucket/foreigner_demo.mp3')

bot.run(TOKEN)

