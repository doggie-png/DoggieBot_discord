import discord
from ui.rocola.allgenres_Select.generosElectronica import MenuTechno
from ui.rocola.allgenres_Select.generosRap import MenuRap

class MenuElectronica(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(MenuTechno())

class ViewMenuRap(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(MenuRap())