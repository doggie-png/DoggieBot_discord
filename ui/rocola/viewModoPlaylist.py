import discord
from ui.rocola.generos_playlist_Select import MenuGenerosPlaylist

class ModoPlaylist(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(MenuGenerosPlaylist())