import discord
from ui.rocola.allgenres_Select.genero_selected_playlist import genero_playlists

class genero_seleccionado(discord.ui.View): #esta wea sera general para mostrar segun lo seleccionado
    def __init__(self, genero):
        super().__init__()
        self.genero = genero
        self.add_item(genero_playlists(genero)) #select sera universal par lo comentado arriba xd xd
