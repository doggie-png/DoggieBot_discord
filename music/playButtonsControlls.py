import discord
from music.state import get_queue

class Play(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Play", style=discord.ButtonStyle.red)

    async def callback(self, interaction: discord.integrations):
        voice_client = interaction.guild.voice_client

        if voice_client is None:
            return await interaction.response.send_message("joven, acaso me ve aca en un canal de voz?", delete_after=10)
    
        if not voice_client.is_paused():
            return await interaction.response.send_message("no hay nada en pausa", delete_after=10)
    
        voice_client.resume()
        await interaction.response.send_message("cancion sonando de nuevo!!", delete_after=10)


class Pause(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Pause", style=discord.ButtonStyle.red)

    async def callback(self,interaction: discord.Interaction):
        #await button.response.send_message("se comenzo la reproduccion xd")
        voice_client = interaction.guild.voice_client
        if voice_client is None:
            return await interaction.response.send_message("joven, acaso me ve aca en un canal de voz?", delete_after=10)
    
        if not voice_client.is_playing():
            return await interaction.response.send_message("acaso escuchas algo sonando para pausarlo?", delete_after=10)
    
        voice_client.pause()
        await interaction.response.send_message("cancion pausada", delete_after=10)


class Skip(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Next", style=discord.ButtonStyle.red)

    async def callback(self,interaction: discord.Interaction):
        
        if interaction.guild.voice_client and (interaction.guild.voice_client.is_playing() or interaction.guild.voice_client.is_paused()):
            interaction.guild.voice_client.stop()
            await interaction.response.send_message("Siguiente cancion", delete_after=10)
        else:
            await interaction.response.send_message("no hay nada sonando para saltar de cancnion", delete_after=10)


class Stop(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Stop", style=discord.ButtonStyle.red)

    async def callback(self,interaction: discord.Interaction):
        
        await interaction.response.defer()
        voice_client = interaction.guild.voice_client

        if not voice_client or not voice_client.is_connected():
            await interaction.followup.send("me vez en un canal de voz?", delete_after=10)
            return 

        SONG_QUEUES = get_queue(interaction.guild_id)
        SONG_QUEUES.clear()

        if voice_client.is_playing() or voice_client.is_paused():
            voice_client.stop()
    
        await interaction.response.send_message("dejo de reprodicir canciones y me voy, que lastima pero adios", delete_after=10)

        await voice_client.disconnect()