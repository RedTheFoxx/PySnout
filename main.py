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

TOKEN = "..."


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
        embed_already_playing = discord.Embed(title="Element ajouté à la liste de lecture !", color=0xe04f5f)
        embed_already_playing.set_author(name="Lecteur",
                                         icon_url="https://cdn-icons-png.flaticon.com/512/7826/7826802.png")
        embed_already_playing.set_footer(text="PySnout")
        await ctx.send(embed=embed_already_playing)

        engine.queue.append(url)
        return

    engine.queue.append(url)
    queue_not_empty = True

    while queue_not_empty:

        engine.player_is_playing = True

        url = engine.queue.pop(0)

        embed_download = discord.Embed(title="Téléchargement ...", color=0x3b77b1)
        embed_download.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/6995/6995413.png")
        embed_download.set_footer(text="PySnout")
        await ctx.send(embed=embed_download)

        filename = await download_audio(url)

        embed_playing = discord.Embed(title="Lecture du prochain élément", color=0x4eb03b)
        embed_playing.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/7826/7826802.png")
        embed_playing.set_footer(text="PySnout")
        await ctx.send(embed=embed_playing)

        await play_audio(ctx, filename)

        if not engine.queue:  # condition pour arrêter la boucle
            queue_not_empty = False

    engine.reset_player_is_playing()


@bot.command("stop")
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        engine.reset_player_is_playing()
    else:
        embed_no_playing = discord.Embed(title="Erreur : Aucune lecture en cours !", color=0xe04f5f)
        embed_no_playing.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/463/463612.png")
        embed_no_playing.set_footer(text="PySnout")
        await ctx.send(embed=embed_no_playing)


@bot.command("clear")
async def clear(ctx):
    engine.queue.clear()
    embed_cleared = discord.Embed(title="Liste de lecture purgée", color=0x4eb03b)
    embed_cleared.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/7826/7826802.png")
    embed_cleared.set_footer(text="PySnout")
    await ctx.send(embed=embed_cleared)

bot.run(TOKEN)
