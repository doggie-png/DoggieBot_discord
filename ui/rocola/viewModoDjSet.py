import discord
from ui.rocola.generos_DjSet_select import MenuGenerosDjSet

class ModoDjSet(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(MenuGenerosDjSet())