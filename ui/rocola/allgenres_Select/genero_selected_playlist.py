import discord
from utils.controlls_Json.lectura import cargar_linksPlaylist
from music.PlaylistMode import Play_genero_musical

class genero_playlists(discord.ui.Select):
    def __init__(self, genero):
        data = cargar_linksPlaylist()
        playlists = [track for track in data if track["genero"] == genero]
        options = []

        for track in playlists:
            options.append(
                discord.SelectOption(
                    label=track["nombre"],
                    value=track["links"],
                    description="selecciona la playlist"
                )
            )

        
        super().__init__(placeholder="Selecciona una Playlist", min_values=1,max_values=1, options=options)

    async def callback(self, interaction:discord.Interaction):

        selected_link = self.values[0]
        await Play_genero_musical(interaction, selected_link)
