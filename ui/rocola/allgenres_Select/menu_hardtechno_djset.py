import discord
from music.PlaylistMode import Play_genero_musical
from music.PlayMode import playmode

class hardTechno(discord.ui.Select):
    def __init__(self):
        options = [
            #aqui se deberia llenar con la informacion de los json, se deberia extraer de ellos el genero de cada playlist
            discord.SelectOption(
                label="Nina Bender - DJ Set"
                #description="Hard Techno"
            ),
            discord.SelectOption(
                label="TBA - Nikolina | HÖR - September 11 / 2025",
                
            ),
            discord.SelectOption(
                label="ROÜGE | HÖR - Jan 7 / 2023"
                
            ),
            discord.SelectOption(
                label="Early Techno"
                
            )
        ]

        super().__init__(placeholder="Techno", min_values=1,max_values=1, options=options)

    async def callback(self, interaction:discord.Interaction):
        if self.values[0] == "Nina Bender - DJ Set":
            url = "https://www.youtube.com/watch?v=jelaEwcewXY&list=RDjelaEwcewXY&start_radio=1&t=1594s"
            await Play_genero_musical(interaction, url)
            

        elif self.values[0] == "TBA - Nikolina | HÖR - September 11 / 2025":
            url = "https://www.youtube.com/watch?v=6gRXToZhO1A&list=RD6gRXToZhO1A&start_radio=1&t=2536s"
            await Play_genero_musical(interaction, url)

        elif self.values[0] == "ROÜGE | HÖR - Jan 7 / 2023":
            url = "https://www.youtube.com/watch?v=t_8-teUU_yg"
            await Play_genero_musical(interaction, url)

        elif self.values[0] == "Early Techno":
            url = "https://www.youtube.com/watch?v=84sHTvn6xf8&list=PL8uhM5Q8xUMoj4yoX2hWCbvLKIcm4vBt-"
            await playmode(interaction, url)
            #await interaction.response.send_message("los modulos funcionan peor no hay acceso a reproducir musica", delete_after=20)