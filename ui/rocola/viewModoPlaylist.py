import discord
from ui.rocola.generos_Select import MenuGeneros

class ModoPlaylist(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(MenuGeneros())