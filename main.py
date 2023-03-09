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


TOKEN = "..."

# Globals
player_is_playing = False


@bot.event
async def on_ready():
    print("PySnout est en ligne !")


@bot.command("play")
async def play(ctx, url=None):
    if url is None:
        embed_no_url = discord.Embed(title="Erreur : URL non renseignée !", color=0xe04f5f)
        embed_no_url.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/463/463612.png")
        embed_no_url.set_footer(text="PySnout - P1")
        await ctx.send(embed=embed_no_url)
        return
    if not url.startswith('https://www.youtube.com/watch?v='):
        embed_bad_format = discord.Embed(title="Erreur : L'URL n'est pas du bon format (YouTube uniquement)", color=0xe04f5f)
        embed_bad_format.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/463/463612.png")
        embed_bad_format.set_footer(text="PySnout - P1")
        await ctx.send(embed=embed_bad_format)
        return

    embed_download = discord.Embed(title="Téléchargement ...", color=0x3b77b1)
    embed_download.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/6995/6995413.png")
    embed_download.set_footer(text="PySnout - P1")

    await ctx.send(embed=embed_download)

    pathtoplay = await download_audio(url)

    embed_playing = discord.Embed(title="Lecture en cours", color=0x4eb03b)
    embed_playing.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/7826/7826802.png")
    embed_playing.set_footer(text="PySnout - P1")
    await ctx.send(embed=embed_playing)

    await play_audio(ctx, pathtoplay)

    global player_is_playing
    player_is_playing = True

bot.run(TOKEN)
