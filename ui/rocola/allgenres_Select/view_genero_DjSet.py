import discord
from ui.rocola.allgenres_Select.genero_selected_sets import GeneroSets
#from ui.rocola.allgenres_Select.generosRap import MenuRap

class GeneroDjSet(discord.ui.View): #esta wea sera general para mostrar segun lo seleccionado
    def __init__(self, genero):
        super().__init__()
        self.genero = genero
        self.add_item(GeneroSets(genero)) #select sera universal par lo comentado arriba xd xd
