import discord
from ui.rocola.allgenres_Select.generosElectronica import MenuTechno

class MenuElectronica(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(MenuTechno())