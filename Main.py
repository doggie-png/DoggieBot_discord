import discord
import random
import json
import os
import yt_dlp
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from collections import deque
from ui.rocola.view_rocola import ModeView
from music.PlayMode import playmode


class CLient(commands.Bot):
    async def on_ready(self):
        print(f'Lpgged on as {self.user}!')

        try: 
            #servidor de pruebas 1470355393455718402
            #server culto420 908881906777616384
            guild= discord.Object(id=908881906777616384)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} command to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')

    #Respuestas a mensajes
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('hola' or 'hello' or 'hi'):
            embed = discord.Embed(title= "Hola, Todo bien?", description="Toma es peligroso andar por ahi sin uno.", color = discord.Color.red())
            embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=bRzTMAMaPhdJ&format=png&color=000000")
            embed.set_author(name= message.author)
            await message.channel.send(embed=embed, delete_after=60)

        #mostrar las reglas
        if message.content == "!Reglas":
            await message.channel.send(embed=showrules())

        #ver los live sets
        if message.content == "!linksSets":
            data = cargar_links()

            if not data["links"]:
                embed = discord.Embed(title= "Live Sets", description="No hay links guardados, pero toma un cogollo y agrega unos.", color = discord.Color.red())
                embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=bRzTMAMaPhdJ&format=png&color=000000")
                await message.channel.send(embed=embed)
            else:
                texto = "\n".join(data["links"])
                await message.channel.send(f"Links guardados:\n{texto}")

        #ver las playlist
        if message.content == "!linksPlaylist":
            data = cargar_linksPlaylist()

            if not data["links"]:
                embed = discord.Embed(title= "Playlist", description="No hay links guardados, pero toma un cogollo y agrega unos.", color = discord.Color.red())
                embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=bRzTMAMaPhdJ&format=png&color=000000")
                await message.channel.send(embed=embed)
            else:
                texto = "\n".join(data["links"])
                await message.channel.send(f"Links guardados:\n{texto}")

        #ver las playlist
        if message.content == "!linksAllSongs":
            data = cargar_all_songs()

            if not data["links"]:
                embed = discord.Embed(title= "Apoco si escuchas de todo", description="No hay links guardados, pero toma un cogollo y agrega unos.", color = discord.Color.red())
                embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=bRzTMAMaPhdJ&format=png&color=000000")
                await message.channel.send(embed=embed)
            else:
                texto = "\n".join(data["links"]) #no se si esto funcione alch
                await message.channel.send(f"Links guardados:\n{texto}")


    

    #cuando el bot se une y deja el server
    async def on_guild_join(guild):
        await guild.owner.send(f'Hello {guild.owner.name}, eh llegado a tu server: **{guild.name}**, para mas info contacta a mi creador: DoggieWrither.')

    async def on_guild_remove(guild):
        await guild.owner.send(f'Hello {guild.owner.name}, eh dejado tu server: **{guild.name}**, El universo me llama a otros lugares, espero nos volvamos a ver.')

    


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
client = CLient(command_prefix="!", intents=intents)


#server pruebas 1470355393455718402
#server culto420 908881906777616384
GUILD_ID = discord.Object(id=908881906777616384)


#json para las funciones del bot
JSON_LIVESETS = "LiveSets.json"
JSON_PLAYLIST = "PLayList.json"
JSON_ALLSONGSPLAYLIST = "AllSongsPLaylist.json"


#reproduccion de muscia del bot
SONG_QUEUES = {}


#Eventos
#Gestion de miembros
@client.event
async def on_member_join(member):

    #id server pruebas 1470355394022080617
    #id septima puerta culto420  957768427647434812
    channel_id = 957768427647434812
    channel = client.get_channel(channel_id)
    embed = discord.Embed(title="Haz ingresado a este plano astral!", description="Quieres porro?", color = discord.Color.red())
    embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=Z6c5d0HR6LKq&format=png&color=000000")
    embed.set_author(name= member.name)
    #embed.set_footer(text= member.guild.name)
    role = discord.utils.get(member.guild.roles, name='MiembroDelCulto')
    await member.add_roles(role)
    await channel.send(embed=embed, view=ViewQuierePorro())


#Respuestas a edicion y eliminacion de mensajes pd: esta madre da error xd xd xd
#@client.event
#async def on_message_edit(before, after):
    #if after.author.bot:
        #return
        
    #if before.content == after.content:
        #return
        
    #await after.channel.send(f'{after.author.name} No sea culo, deje el mensaje original',delete_after=15 )

#@client.event
#async def on_message_delete(message):
    #await message.channel.send(f'Un mensaje de {message.author.name} fue eliminado', delete_after=15)



#Creacion de funciones por comando

#Ruleta de bongazo
@client.tree.command(name="bongazo", description="Ingresa un nuemero del 1 al 4 y prueba suerte para un bongazo", guild=GUILD_ID)
async def tocaBongazo(interaction: discord.Interaction, suerte: int):
    numero = random.randint(1, 4)
    embed = discord.Embed(title="Ruleta de Bongazo!", description="Veamos si te toca bongazo...", color = discord.Color.red())

    if numero == suerte:
        embed.add_field(name="Resultado", value= "Te mereces 2 por chingon", inline=False)
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=5dnDza1OuPoI&format=png&color=000000")
        
    else: 
        embed.add_field(name="Resultado", value= "Nel joven no le toca", inline=False)
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=rBFDe1eB8d5w&format=png&color=000000")
        

    embed.add_field(name ="Solicitado por: ", value= interaction.user.name, inline = False)
    embed.set_author(name= interaction.guild.name)
    await interaction.response.send_message(embed=embed, delete_after=60)
        

#Ruleta para decidir algo xd
@client.tree.command(name="ruleta", description="ingresa el tamano de la ruleta y las opciones separadas por una ,", guild=GUILD_ID)
async def Ruleta(interaction: discord.Interaction, size: int, opciones: str):
    CantidadOpciones = size
    elementos = [p.strip() for p in opciones.split(",")][:CantidadOpciones]
    numero = random.randint(1, CantidadOpciones)
    resultado = elementos[numero - 1]
    embed = discord.Embed(title="Ruleteando", color = discord.Color.red())
    embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=53wNQypE67z9&format=png&color=000000")
    embed.add_field(name ="De las siguientes opciones: ", value = opciones, inline = False)
    embed.add_field(name ="El resultado es: ", value= resultado, inline = False)
    embed.set_author(name= interaction.guild.name)
    await interaction.response.send_message(embed=embed, delete_after=300)

#Musica
#Reproducir una sola cancion
@client.tree.command(name="play", description="ingresa el nombre de una cancion", guild=GUILD_ID)
async def PlaySong(interaction: discord.Interaction, cancion: str):
    await playmode(interaction, cancion)
            


#Rocola con diferentes generos musicales
@client.tree.command(name="rocola", description="Selecciona si quieres modo playlist o modo dj-set",guild=GUILD_ID)
async def Rocola(interaction: discord.Interaction):
    embed = discord.Embed(title="Rocola", color = discord.Color.red())
    embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
    embed.add_field(name ="Selecciona el modo de la rocola", value="", inline = False) #modo dj-set incluir en el embed de repruccion, el nombre del canal del dj
    embed.add_field(name="Platlist:", value="Reproduce canciones de ese genero.")
    embed.add_field(name="Dj-set:", value="Reproduce un set de algun dj del genero que tu quieras")
    #embed.set_footer(text="Selecciona rapido xq me desaparezco en 1 minutos")
    await interaction.response.send_message(embed=embed, view=ModeView(), delete_after= 60) #view=View() es de los botones de los generos para el modo playlist  delete_after= 60  view=BotonesModoRocola()
    

#AgregaAPlaylist
@client.tree.command(name="agrega-a-playlist", description="Arega una playlist a una lista que contiene mas playlist xd",guild=GUILD_ID)
async def AddToPlaylist(interaction: discord.Interaction, name: str ,link: str):

    if not link.startswith("http"): #permmitir de otras plataformas como spoty y asi
        embed = discord.Embed(title="Playlists", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
        embed.add_field(name ="Joven, eso no es un enlace no mame", value="Todo meco el bato queriendo trollear al bot", inline = False)
        await interaction.response.send_message(embed=embed, delete_after=60)
        return

    data = cargar_linksPlaylist()

    if link in data["links"]:
        embed = discord.Embed(title="Playlists", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
        embed.add_field(name ="Joven, el enlace ya existe en la lista", value="El enlace de la playlist ya existe", inline = False)
        await interaction.response.send_message(embed=embed, delete_after=60)
        return

    data["links"].append(link)
    data["nombre"].append(name)
    guardar_linksPlaylist(data)
    embed = discord.Embed(title="Playlists", color = discord.Color.red())
    embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
    embed.add_field(name ="Se arego correctamente la playlist:", value=name, inline = False)
    await interaction.response.send_message(embed=embed, delete_after=60)

#AgregaALiveSet
@client.tree.command(name="agrega-a-live-set", description="Arega un live-set a la playlist, puedes consultar la lista en el canal de live set",guild=GUILD_ID)
async def AddToLiveSet(interaction: discord.Interaction, genero: str ,link: str):

    if not link.startswith("http"):
        embed = discord.Embed(title="LiveSets", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
        embed.add_field(name ="Joven, eso no es un enlace no mame", value="Todo meco el bato queriendo trollear al bot", inline = False)
        await interaction.response.send_message(embed=embed,delete_after=60)
        return

    data = cargar_links()

    if link in data["links"]:
        
        embed = discord.Embed(title="LiveSets", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
        embed.add_field(name ="Joven, el enlace ya existe en la lista", value="El enlace ya existe en el genero especificado o ya fue agregado a otro genero xd xd xd soy un bot we yo que se", inline = False)
        await interaction.response.send_message(embed=embed,delete_after=60)
        return

    data["links"].append(link)
    data["genero"].append(genero)
    guardar_links(data)
    #cuando se haya agregado correctamente
    embed = discord.Embed(title="LiveSets", color = discord.Color.red())
    embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
    embed.add_field(name ="Se arego correctamente el live set al genero", value=genero, inline = False)
    await interaction.response.send_message(embed=embed,delete_after=60)

#agrega a all songs
@client.tree.command(name="agrega-a-songs", description="Arega una cancion a una playlist donde hay varias canciones",guild=GUILD_ID)
async def AddToAllSongs(interaction: discord.Interaction, nombre: str ,host: str ,link: str):

    if not link.startswith("http"): ## de momento solo permite de youtube, agregar la validacion para deezer, spoty y soundcloud.
        embed = discord.Embed(title="PLaylist apoco si escuchas de todo", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
        embed.add_field(name ="Joven, eso no es un enlace no mame", value="Todo meco el bato queriendo trollear al bot", inline = False)
        await interaction.response.send_message(embed=embed,delete_after=60)
        return

    data = cargar_all_songs()

    if link in data["links"]:
        
        embed = discord.Embed(title="PLaylist apoco si escuchas de todo", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
        embed.add_field(name ="Joven, el enlace ya existe en la lista", value="El enlace de la cancion ya existe en la playlist", inline = False)
        await interaction.response.send_message(embed=embed,delete_after=60)
        return

    data["nombre"].append(nombre)
    data["host"].append(host)
    data["links"].append(link)
    
    
    guardar_all_songs(data)
    #cuando se haya agregado correctamente
    embed = discord.Embed(title="PLaylist apoco si escuchas de todo", color = discord.Color.red())
    embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
    embed.add_field(name ="Se arego correctamente la cancion", value=nombre, inline = False)
    await interaction.response.send_message(embed=embed,delete_after=60)



#Eliminar mensajes
@client.tree.command(name="eliminar-mensajes-bots", description="Elimina mensajes de bots en el canal",guild=GUILD_ID)
async def limpiar_mensajes_bots(interaction: discord.Interaction, limite: int):
    
    #await interaction.channel.purge(
        #limit=limite,
        #check=lambda m: m.author.bot
    #)

    async for message in interaction.channel.history(limit=limite):
        #await message.delete()
        if message.author.bot:
            await message.delete()


#VISTAS DE BOTONES

#vista botones para mensaje de bienvenida
class ViewQuierePorro(discord.ui.View):
    @discord.ui.button(label="SIIIII", style=discord.ButtonStyle.red)
    async def button_SI(self, button,interaction):
        embed = discord.Embed(title="Rolen el porro!", description="Alguien pasele un porro esos modales porfavor!", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=Z6c5d0HR6LKq&format=png&color=000000")
        embed.set_author(name= "ROLEEEEEEEEEEEN")
        await button.response.send_message(embed=embed, delete_after=120)

    @discord.ui.button(label="NOOOOOO", style=discord.ButtonStyle.red)
    async def button_NO(self, button,interaction):
        embed = discord.Embed(title="Otro vicio?", description="Cielos viejo tu si que estas loco", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=nnYQNoQSxszk&format=png&color=000000")
        embed.set_author(name= "Disfruta tu estadia aqui")
        await button.response.send_message(embed=embed,delete_after=120)

#MAQUETA DE VISTA DROP DOWN MENU

class MenuRap(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="C-kan"
                
            ),
            discord.SelectOption(
                label="Cancerbero"
                
            ),
            discord.SelectOption(
                label="Cartel de santa"
                
            )
        ]

        super().__init__(placeholder="Rap", min_values=1,max_values=1, options=options)

    async def callback(self, interaction:discord.Interaction):
        if self.values[0] == "C-kan":
            await interaction.response.send_message("reproduciendo: C kan", delete_after=20)

        elif self.values[0] == "Cancerbero":
            await interaction.response.send_message("reproduciendo: Cancerbero", delete_after=20)

        elif self.values[0] == "Cartel de santa":
            await interaction.response.send_message("reproduciendo: Cartel de santa", delete_after=20)
        
#funciones

#funciones para la escritura y lectura de lo json
#gestion de Live Sets
def cargar_links(): #seria solo para live sets
    if not os.path.exists(JSON_LIVESETS):
        return {"genero":[],"links": []}

    with open(JSON_LIVESETS, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_links(data): #seria solo para live sets
    with open(JSON_LIVESETS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


#gestion de playlist
def cargar_linksPlaylist(): #seria solo para playlist
    if not os.path.exists(JSON_PLAYLIST):
        return {"nombre":[],"links": []}

    with open(JSON_PLAYLIST, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_linksPlaylist(data): #seria solo para playlist
    with open(JSON_PLAYLIST, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

#gestion de playlist
def cargar_all_songs(): #seria solo para all songs
    if not os.path.exists(JSON_ALLSONGSPLAYLIST):
        return {"nombre":[],"host":[],"links": []}

    with open(JSON_ALLSONGSPLAYLIST, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_all_songs(data): #seria solo para all songs
    with open(JSON_ALLSONGSPLAYLIST, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


#funcion para imprimir las reglas
def showrules():
    embed = discord.Embed(title="Reglas del servidor", description="Es mas como un codigo de comportamiento", color = discord.Color.red())
    embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=6440&format=png&color=000000")
    embed.add_field(name ="Regla 1", value="Nada de flameos", inline = False)
    embed.add_field(name ="Regla 2", value="Si no consumes esta bien, solo no andes de castroso xd", inline = False)
    embed.add_field(name ="Regla 3", value="Manten el orden en los canales de texto", inline = False)
    embed.add_field(name ="Regla 4", value="Comparte tus canciones, no seas egoista", inline = False)
    embed.set_author(name= "Doggiewrither")
    return embed


load_dotenv()
client.run(os.getenv("token"))