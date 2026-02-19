import discord
import yt_dlp
import asyncio
from collections import deque
from music.state import get_queue



def es_url(texto):
    return texto.startswith(("https://"))

async def search_ytdlp_async(query, ydl_opts):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, lambda: _extract(query, ydl_opts))

async def play_next_song(voice_client, guild_id, channel, socilitado_por): #la comparte la rocola y el modo reproduccion por cancniones
    SONG_QUEUES = get_queue(guild_id)
    bot = voice_client.client
    if SONG_QUEUES:
        audio_url, title, duration,thumbnail = SONG_QUEUES.popleft()
        mins, secs = divmod(duration, 60)
        duration_str = f"{mins}:{secs:02}"
        ffmpeg_options = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn -c:a libopus -b:a 96k"
        }
        source = discord.FFmpegOpusAudio(audio_url, executable= "bin\\ffmpeg\\ffmpeg.exe", **ffmpeg_options)

        def after_play(error):
            if error:
                print(f"Error playing {title}: {error}")
            asyncio.run_coroutine_threadsafe(play_next_song(voice_client,guild_id, channel, socilitado_por), bot.loop)

        ##embed palying##
        embed_playing = discord.Embed(title="Reproduciendo", color = discord.Color.red())
        if thumbnail:
            embed_playing.set_thumbnail(url=thumbnail)
        else:
            embed_playing.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")            
        embed_playing.add_field(name =title, value="De Youtube", inline = False)
        embed_playing.add_field(name="Duracion", value= duration_str, inline=True)
        embed_playing.add_field(name="Numero", value="2", inline=True)
        embed_playing.add_field(name="Volumen", value="100%", inline=True)
        embed_playing.add_field(name ="Solicitado por: ", value= socilitado_por, inline = False)
        embed_playing.set_author(name= socilitado_por)
        ##embed playing##

        voice_client.play(source, after=after_play)
        asyncio.create_task(channel.send(embed=embed_playing, delete_after=duration))

    else:
        await voice_client.disconnect()
        SONG_QUEUES = deque()


def _extract(query, ydl_opts):
    tracks = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #return ydl.extract_info(query, download=False)

        info = ydl.extract_info(query, download=False)

        for entry in info['entries']:
            if entry is None:
                continue

            if entry.get('url') is None:
                continue

            tracks.append(entry)

    return tracks
