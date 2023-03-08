# Required :
# ffmpeg + PATH (for audio processing)
# PyNaCl (for audio connection in a channel)
# yt-dlp (for video to audio)

# TODO : add a command to stop the audio

import discord
from discord.ext import commands

from engine import play_audio, download_audio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


TOKEN = "MTA1MDU4NTA4ODI2MzQ2Mjk2NA.GHtEV1.sFbxSfgyJtSuONrZ_smcngxtGadnRICps4pANQ"


@bot.event
async def on_ready():
    print("PySnout est en ligne !")


@bot.command("play")
async def play(ctx, url):
    if not url.startswith('https://www.youtube.com/watch?v='):
        await ctx.send('Mauvais format d\'URL !')
        return

    await ctx.send("Chargement ...")
    pathtoplay = await download_audio(url)
    await ctx.send("Terminé. Lecture en cours ...")
    await play_audio(ctx, pathtoplay)


bot.run(TOKEN)
