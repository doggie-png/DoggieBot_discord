import discord
from collections import deque
from music.function import search_ytdlp_async, play_next_song
from music.state import get_queue

async def playmode(interaction, cancion):
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
        "noplaylist": True, #cambiar a false para permitir play list, en el caso de la rocola aqui es donde se marca la diferencia
        "youtube_include_dash_manifest": False,
        "youtube_include_hls_manifest": False,
    }

    #query = "ytsearch1: " + cancion
    entrada = cancion
    #query = entrada if es_url(entrada) else f"ytsearch1:{entrada}"
    if entrada.startswith(("https://")):
        query = entrada
    else:
        query = "ytsearch1: " + entrada
    results = await search_ytdlp_async(query, ydl_options)
    tracks = results.get("entries", [])

    if tracks is None:
        await interaction.followup.send("No se encontraron resultados", delete_after=10)
        return
    
    first_track = tracks[0] if tracks else results
    
    #todo lo que esta aqui abajo se ejecuta solo si se encontro resultados de la busqueda

    #first_track = tracks[0]
    audio_url = first_track["url"]
    title = first_track.get("title", "Untitled")
    duration = first_track.get("duration", 0)
    thumbnail = first_track.get("thumbnail")

    guild_id = str(interaction.guild_id)
    SONG_QUEUES = get_queue(guild_id)

    #if SONG_QUEUES.get(guild_id) is None:
        #SONG_QUEUES[guild_id] = deque()

    SONG_QUEUES.append((audio_url, title, duration,thumbnail))

    if voice_client.is_playing() or voice_client.is_paused():
        await interaction.followup.send(f"Added to queue: **{title}**", delete_after=20)
    else:
        await play_next_song(voice_client, guild_id, interaction.channel, interaction.user.name)