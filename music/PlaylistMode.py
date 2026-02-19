import discord
from collections import deque
from music.function import es_url, search_ytdlp_async, play_next_song
from music.state import get_queue

async def Play_genero_musical(interaction, genero: int):
    await interaction.response.defer()

    if interaction.user.voice is None:
        await interaction.followup.send("Mame joven, unase a un canal de voz primero", delete_after=10)
        return

    voice_channel = interaction.user.voice.channel

    if voice_channel is None:
        await interaction.followup.send("Mame joven, unase a un canal de voz primero", delete_after=10)
        return
    
    voice_client = interaction.guild.voice_client

    if voice_client is None:
        voice_client = await voice_channel.connect()
    elif voice_channel != voice_client.channel:
        await voice_client.move_to(voice_channel)

    ydl_options = {
        "format": "bestaudio[abr<=96]/bestaudio",
        "noplaylist": False,
        "ignoreerrors": True,
        "quiet": True,
        "playlistend": 25,
        "youtube_include_dash_manifest": False,
        "youtube_include_hls_manifest": False,
    }

    generos_musicales = [
        "hardtechno",
        "acidtechno",
        "melodictechno",
        "https://www.youtube.com/watch?v=84sHTvn6xf8&list=PL8uhM5Q8xUMoj4yoX2hWCbvLKIcm4vBt-",#earlytechno
        "banda",
        "pop"
    ]

    #query = "ytsearch1: " + generos_musicales[genero]
    entrada = generos_musicales[genero]
    query = entrada if es_url(entrada) else f"ytsearch1:{entrada}"
    results = await search_ytdlp_async(query, ydl_options)
    #tracks = results.get("entries", [])
    tracks = results

    if tracks is None:
        await interaction.followup.send("No se encontraron resultados", delete_after=10)
        return
    
    #todo lo que esta aqui abajo se ejecuta solo si se encontro resultados de la busqueda
    #first_track = tracks[0]
    guild_id = str(interaction.guild_id)
    SONG_QUEUES = get_queue(guild_id)

    #if SONG_QUEUES.get(guild_id) is None: #.get(guild_id)
        #SONG_QUEUES[guild_id] = deque()

    for track in tracks:
        if track is None:
            continue

        audio_url = track["url"]
        title = track.get("title", "Untitled")
        duration = track.get("duration", 0)
        thumbnail = track.get("thumbnail")
        SONG_QUEUES.append((audio_url, title, duration,thumbnail))


    if voice_client.is_playing() or voice_client.is_paused():
        await interaction.followup.send(f"Platlist de: **{generos_musicales[genero]}**", delete_after=20)
    else:
        await play_next_song(voice_client, guild_id, interaction.channel, interaction.user.name)
