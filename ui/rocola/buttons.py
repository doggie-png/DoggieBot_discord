import discord
from ui.rocola.viewModoPlaylist import ModoPlaylist

class PlaylistButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Playlist Mode", style=discord.ButtonStyle.red)

    async def callback(self, interaction: discord.integrations):
        embed = discord.Embed(title="Modo Playlist", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
        embed.add_field(name="Selecciona un Genero", value="")
        await interaction.response.send_message(embed=embed ,view=ModoPlaylist())


class DjSetButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="DJ-Set Mode", style=discord.ButtonStyle.red)

    async def callback(self, interaction: discord.integrations):
        embed = discord.Embed(title="DJ-Set Mode", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
        embed.add_field(name="Selecciona un set", value="")
        await interaction.response.send_message(embed=embed)