import discord
from ui.rocola.buttons import PlaylistButton, DjSetButton

class ModeView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(PlaylistButton())
        self.add_item(DjSetButton())
