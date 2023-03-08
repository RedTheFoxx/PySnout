from discord import FFmpegPCMAudio


async def play_audio(ctx, file_path):
    if not ctx.author.voice:
        await ctx.send("Vous devez être connecté dans un canal vocal pour utiliser cette commande !")
        return

    vc = ctx.author.voice.channel

    if ctx.voice_client is None:
        await vc.connect()

    source = FFmpegPCMAudio(file_path)

    ctx.voice_client.play(source)
