import os

import discord
from discord import FFmpegPCMAudio
import yt_dlp

player_is_playing = False


def reset_player_is_playing():
    global player_is_playing
    player_is_playing = False


async def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': './audio_bucket/%(title)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    filename = ydl.prepare_filename(ydl.extract_info(url))

    return filename


async def play_audio(ctx, file_path):
    if not ctx.author.voice:
        embed_no_voice = discord.Embed(title="Erreur : Vous n'êtes pas en vocal !", color=0xe04f5f)
        embed_no_voice.set_author(name="Lecteur", icon_url="https://cdn-icons-png.flaticon.com/512/463/463612.png")
        embed_no_voice.set_footer(text="PySnout")
        await ctx.send(embed=embed_no_voice)
        return

    vc = ctx.author.voice.channel

    if ctx.voice_client is None:
        await vc.connect()

    source = FFmpegPCMAudio(file_path + '.mp3')

    def after_playing():
        os.remove(file_path + '.mp3')
        reset_player_is_playing()

    ctx.voice_client.play(source, after=after_playing)
