import discord
from music.playButtonsControlls import Play, Pause, Skip, Stop

class ControllButtons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Play())
        self.add_item(Pause())
        self.add_item(Skip())
        self.add_item(Stop())