import discord
from music.PlaylistMode import Play_genero_musical

class MenuTechno(discord.ui.Select):
    def __init__(self):
        options = [
            #aqui se deberia llenar con la informacion de los json, se deberia extraer de ellos el genero de cada playlist
            discord.SelectOption(
                label="Hard Techno"
                #description="Hard Techno"
            ),
            discord.SelectOption(
                label="Acid Techno",
                
            ),
            discord.SelectOption(
                label="Melodic Techno"
                
            ),
            discord.SelectOption(
                label="Early Techno"
                
            )
        ]

        super().__init__(placeholder="Techno", min_values=1,max_values=1, options=options)

    async def callback(self, interaction:discord.Interaction):
        if self.values[0] == "Hard Techno":
            await interaction.response.send_message("seleccionaste hardtechno", delete_after=120)
            

        elif self.values[0] == "Acid Techno":
            await interaction.response.send_message("seleccionaste acid techno", delete_after=120)

        elif self.values[0] == "Melodic Techno":
            await interaction.response.send_message("seleccionaste melodic techno", delete_after=120)

        elif self.values[0] == "Early Techno":
            url = "https://www.youtube.com/watch?v=84sHTvn6xf8&list=PL8uhM5Q8xUMoj4yoX2hWCbvLKIcm4vBt-"
            await Play_genero_musical(interaction, url)
            #await interaction.response.send_message("los modulos funcionan peor no hay acceso a reproducir musica", delete_after=20)