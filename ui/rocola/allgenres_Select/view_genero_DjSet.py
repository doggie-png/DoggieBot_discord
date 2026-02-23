import discord
from ui.rocola.allgenres_Select.menu_hardtechno_djset import hardTechno
#from ui.rocola.allgenres_Select.generosRap import MenuRap

class MenuHardTechno(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(hardTechno())

#class ViewMenuRap(discord.ui.View):
 #   def __init__(self):
  #      super().__init__()
   #     self.add_item(MenuRap())