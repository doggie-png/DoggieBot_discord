import discord
from ui.rocola.allgenres_Select.view_genero_playlist import genero_seleccionado
from utils.controlls_Json.lectura import cargar_linksPlaylist

class MenuGenerosPlaylist(discord.ui.Select):
    def __init__(self):
        data = cargar_linksPlaylist()
        generos = list({track["genero"] for track in data })
        options = []

        for genero in generos:
            options.append(
                discord.SelectOption(
                    label=genero.capitalize(),
                    value=genero
                    
                )
            )

        
        super().__init__(placeholder="Selecciona un genero", min_values=1,max_values=1, options=options)

    async def callback(self, interaction:discord.Interaction):
        embed = discord.Embed(title="Modo Platlist", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
        embed.add_field(name="Selecciona el genero de la playlist", value="")
        selected_genero = self.values[0]
        await interaction.response.edit_message(embed=embed, view=genero_seleccionado(selected_genero), delete_after=180)