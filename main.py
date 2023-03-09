# Required :
# ffmpeg + PATH (for audio processing)
# PyNaCl (for audio connection in a channel)
# yt-dlp (for video to audio)

import discord
from discord.ext import commands

import engine
from engine import play_audio, download_audio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "MTA1MDU4NTA4ODI2MzQ2Mjk2NA.Ge9PlF.0yO2_Ox5-ZUC5NV90Gg-ZpcnT15QhUlcvIDeNs"


@bot.event
async def on_ready():
    print("PySnout est en ligne !")


@bot.command("play")
async def play(ctx, url=None):

    if url is None:
        embed_no_url = discord.Embed(title="Erreur : URL non renseignée !", color=0xe04f5f)
        embed_no_url.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/463/463612.png")
        embed_no_url.set_footer(text="PySnout")
        await ctx.send(embed=embed_no_url)
        return
    if not url.startswith('https://www.youtube.com/watch?v='):
        embed_bad_format = discord.Embed(title="Erreur : L'URL n'est pas du bon format (YouTube uniquement)",
                                         color=0xe04f5f)
        embed_bad_format.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/463/463612.png")
        embed_bad_format.set_footer(text="PySnout")
        await ctx.send(embed=embed_bad_format)
        return
    if engine.player_is_playing:
        # TODO : Ajouter l'URL à la liste d'attente
        embed_already_playing = discord.Embed(title="Erreur : Une lecture est déjà en cours !", color=0xe04f5f)
        embed_already_playing.set_author(name="Lecteur",
                                         icon_url="https://cdn-icons-png.flaticon.com/512/463/463612.png")
        embed_already_playing.set_footer(text="PySnout")
        await ctx.send(embed=embed_already_playing)
        return

# TODO : Prendre le dernier titre de la liste de lecture et le passer à download_audio
# TODO : Boucler cette section tant que la liste de lecture n'est pas vide
# Début de boucle

    embed_download = discord.Embed(title="Téléchargement ...", color=0x3b77b1)
    embed_download.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/6995/6995413.png")
    embed_download.set_footer(text="PySnout")
    await ctx.send(embed=embed_download)

    pathtoplay = await download_audio(url)

    embed_playing = discord.Embed(title="Lecture en cours", color=0x4eb03b)
    embed_playing.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/7826/7826802.png")
    embed_playing.set_footer(text="PySnout")
    await ctx.send(embed=embed_playing)

    engine.player_is_playing = True

    await play_audio(ctx, pathtoplay)

# Fin de boucle


@bot.command("stop")
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        engine.player_is_playing = False
    else:
        embed_no_playing = discord.Embed(title="Erreur : Aucune lecture en cours !", color=0xe04f5f)
        embed_no_playing.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/463/463612.png")
        embed_no_playing.set_footer(text="PySnout")
        await ctx.send(embed=embed_no_playing)


bot.run(TOKEN)
