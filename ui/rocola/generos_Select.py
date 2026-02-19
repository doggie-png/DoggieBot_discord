import discord
from ui.rocola.allgenres_Select.view_genero import MenuElectronica

class MenuGeneros(discord.ui.Select):
    def __init__(self):
        options = [
            #aqui se deberia llenar con la informacion de los json, se deberia extraer de ellos el genero de cada playlist
            discord.SelectOption(
                label="Electronica"
                #description="Hard Techno"
            ),
            discord.SelectOption(
                label="Rap",
                
            ),
            discord.SelectOption(
                label="Trap",
                
            ),
            discord.SelectOption(
                label="Metal"
                
            ),
            discord.SelectOption(
                label="Pop"
                
            ),
            discord.SelectOption(
                label="Urbano"
                
            )
        ]

        super().__init__(placeholder="Generos Musicales", min_values=1,max_values=1, options=options)

    async def callback(self, interaction:discord.Interaction):
        if self.values[0] == "Electronica":
            #await interaction.response.send_message("seleccionaste hardtechno", delete_after=120)
            embed = discord.Embed(title="Modo Playlist", color = discord.Color.red())
            embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
            embed.add_field(name="Selecciona el subgenero", value="")
            await interaction.response.edit_message(embed=embed, view=MenuElectronica(), delete_after=180)
            

        elif self.values[0] == "Rap":
            await interaction.response.send_message("seleccionaste acid techno", delete_after=120)

        elif self.values[0] == "Trap":
            await interaction.response.send_message("seleccionaste melodic techno", delete_after=120)

        elif self.values[0] == "Metal":
            #Play_genero_musical(interaction, 3)
            await interaction.response.send_message("seleccionaste melodic techno", delete_after=120)

        elif self.values[0] == "Pop":
            await interaction.response.send_message("seleccionaste melodic techno", delete_after=120)

        elif self.values[0] == "Urbano":
            await interaction.response.send_message("seleccionaste melodic techno", delete_after=120)