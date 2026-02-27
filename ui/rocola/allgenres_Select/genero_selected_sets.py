import discord
from music.PlaylistMode import Play_genero_musical
from music.PlayMode import playmode
from utils.controlls_Json.lectura import cargar_links_DjSet

class GeneroSets(discord.ui.Select):
    def __init__(self, genero):
        data = cargar_links_DjSet()
        hardTechnoSets = [track for track in data if track["genero"] == genero]
        options = []

        for track in hardTechnoSets:
            options.append(
                discord.SelectOption(
                    label=track["nombre"],
                    value=track["links"],
                    description="Live set"
                )
            )

        
        super().__init__(placeholder="Selecciona un Dj Set", min_values=1,max_values=1, options=options)

    async def callback(self, interaction:discord.Interaction):

        selected_link = self.values[0]
        #await playmode(interaction, selected_link)
        await Play_genero_musical(interaction, selected_link)
