import discord
from ui.rocola.allgenres_Select.generosElectronica import GeneroPlaylist

class VIewGeneroPlaylist(discord.ui.View): 
    def __init__(self):
        super().__init__()
        #self.genero = genero
        self.add_item(GeneroPlaylist())
