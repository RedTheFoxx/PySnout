from discord import FFmpegPCMAudio
import yt_dlp


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
        await ctx.send("Vous devez être connecté dans un canal vocal pour utiliser cette commande !")
        return

    vc = ctx.author.voice.channel

    if ctx.voice_client is None:
        await vc.connect()

    source = FFmpegPCMAudio(file_path + '.mp3')

    ctx.voice_client.play(source)
