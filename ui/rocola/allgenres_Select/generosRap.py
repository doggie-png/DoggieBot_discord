import discord
from music.PlaylistMode import Play_genero_musical

class MenuRap(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="C-kan"
                
            ),
            discord.SelectOption(
                label="Cancerbero"
                
            ),
            discord.SelectOption(
                label="Cartel de santa"
                
            )
        ]

        super().__init__(placeholder="Rap", min_values=1,max_values=1, options=options)

    async def callback(self, interaction:discord.Interaction):
        if self.values[0] == "C-kan":
            #await interaction.response.send_message("reproduciendo: C kan", delete_after=20)
            url = "https://www.youtube.com/watch?v=A6iJsZoRO64&list=PLn4es56qjv_TOm7C45rJIyELn49chNQoT"
            await Play_genero_musical(interaction, url)

        elif self.values[0] == "Cancerbero":
            url = "https://www.youtube.com/watch?v=sq6oc066w14&list=PLar0gUcrS11jgF-EJKN9wof5xFGMFbMhv"
            await Play_genero_musical(interaction, url)

        elif self.values[0] == "Cartel de santa":
            url = "https://www.youtube.com/watch?v=j_tkv80LkO8&list=PL5IiYWHIq7Bz-IJ-LKR_CSnBH3xALOMbR"
            await Play_genero_musical(interaction, url)