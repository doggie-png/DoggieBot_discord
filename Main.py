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
    await interaction.response.defer()
    
    if interaction.user.voice is None:
        await interaction.followup.send("Mame joven, unase a un canal de voz primero", delete_after=10)
        return

    voice_channel = interaction.user.voice.channel

    if voice_channel is None:
        await interaction.followup.send("Mame joven, unase a un canal de voz primero", delete_after=10)
        return
    
    voice_client = interaction.guild.voice_client

    if voice_client is None:
        voice_client = await voice_channel.connect()
    elif voice_channel != voice_client.channel:
        await voice_client.move_to(voice_channel)

    ydl_options = {
        "format": "bestaudio[abr<=96]/bestaudio",
        "noplaylist": True, #cambiar a false para permitir play list, en el caso de la rocola aqui es donde se marca la diferencia
        "youtube_include_dash_manifest": False,
        "youtube_include_hls_manifest": False,
    }

    #query = "ytsearch1: " + cancion
    entrada = cancion
    #query = entrada if es_url(entrada) else f"ytsearch1:{entrada}"
    if entrada.startswith(("https://")):
        query = entrada
    else:
        query = "ytsearch1: " + entrada
    results = await search_ytdlp_async(query, ydl_options)
    tracks = results.get("entries", [])

    if tracks is None:
        await interaction.followup.send("No se encontraron resultados", delete_after=10)
        return
    
    first_track = tracks[0] if tracks else results
    
    #todo lo que esta aqui abajo se ejecuta solo si se encontro resultados de la busqueda

    #first_track = tracks[0]
    audio_url = first_track["url"]
    title = first_track.get("title", "Untitled")
    duration = first_track.get("duration", 0)
    thumbnail = first_track.get("thumbnail")

    guild_id = str(interaction.guild_id)
    if SONG_QUEUES.get(guild_id) is None:
        SONG_QUEUES[guild_id] = deque()

    SONG_QUEUES[guild_id].append((audio_url, title, duration,thumbnail))

    if voice_client.is_playing() or voice_client.is_paused():
        await interaction.followup.send(f"Added to queue: **{title}**", delete_after=20)
    else:
        await play_next_song(voice_client, guild_id, interaction.channel, interaction.user.name)
            


#Rocola con diferentes generos musicales
@client.tree.command(name="rocola", description="Selecciona si quieres modo playlist o modo dj-set",guild=GUILD_ID)
async def Rocola(interaction: discord.Interaction):
    embed = discord.Embed(title="Rocola", color = discord.Color.red())
    embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
    embed.add_field(name ="Selecciona el modo de la rocola", value="", inline = False) #modo dj-set incluir en el embed de repruccion, el nombre del canal del dj
    embed.add_field(name="Platlist:", value="Reproduce canciones de ese genero.")
    embed.add_field(name="Dj-set:", value="Reproduce un set de algun dj del genero que tu quieras")
    #embed.set_footer(text="Selecciona rapido xq me desaparezco en 1 minutos")
    await interaction.response.send_message(embed=embed, view=BotonesModoRocola(), delete_after= 60) #view=View() es de los botones de los generos para el modo playlist  delete_after= 60
    

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


#DroDown menu
@client.tree.command(name="display-dropdown-menu", description="Soy una prueba",guild=GUILD_ID)
async def dropdownMenu(interaction: discord.Interaction):
    embed = discord.Embed(title="DropDown Menu", color = discord.Color.red())
    embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
    embed.add_field(name ="Prueba de dropdown menu", value="selecciona una opcion", inline = False)
    embed.set_footer(text="Selecciona rapido xq me desaparezco en 1 minuto o menos")
    await interaction.response.send_message(embed=embed, delete_after = 30)


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

#vista botones de reproduccion
class ViewPlaying(discord.ui.View):
    @discord.ui.button(label="Play", style=discord.ButtonStyle.red)
    async def button_Play(self,interaction:discord.Interaction, button):
        #await button.response.send_message("se comenzo la reproduccion xd")
        voice_client = interaction.guild.voice_client

        if voice_client is None:
            return await interaction.response.send_message("joven, acaso me ve aca en un canal de voz?", delete_after=10)
    
        if not voice_client.is_paused():
            return await interaction.response.send_message("no hay nada en pausa", delete_after=10)
    
        voice_client.resume()
        await interaction.response.send_message("cancion sonando de nuevo!!", delete_after=10)

    @discord.ui.button(label="Pause", style=discord.ButtonStyle.red)
    async def button_Pause(self,interaction: discord.Interaction, button):
        #await button.response.send_message("se comenzo la reproduccion xd")
        voice_client = interaction.guild.voice_client
        if voice_client is None:
            return await interaction.response.send_message("joven, acaso me ve aca en un canal de voz?", delete_after=10)
    
        if not voice_client.is_playing():
            return await interaction.response.send_message("acaso escuchas algo sonando para pausarlo?", delete_after=10)
    
        voice_client.pause()
        await interaction.response.send_message("cancion pausada", delete_after=10)
        

    @discord.ui.button(label="Stop", style=discord.ButtonStyle.red)
    async def button_Stop(self,interaction: discord.Interaction, button):
        #await button.response.send_message("se comenzo la reproduccion xd")
        await interaction.response.defer()
        voice_client = interaction.guild.voice_client

        if not voice_client or not voice_client.is_connected():
            await interaction.followup.send("me vez en un canal de voz?", delete_after=10)
            return 
    

        guild_id_str = str(interaction.guild_id)
        if guild_id_str in SONG_QUEUES: 
            SONG_QUEUES[guild_id_str].clear()

        if voice_client.is_playing() or voice_client.is_paused():
            voice_client.stop()
    
        await interaction.response.send_message("dejo de reprodicir canciones y me voy, que lastima pero adios", delete_after=10)

        await voice_client.disconnect()

    @discord.ui.button(label="Next", style=discord.ButtonStyle.red)
    async def button_Next(self,interaction: discord.Interaction, button):
        #await button.response.send_message("se comenzo la reproduccion xd")
        if interaction.guild.voice_client and (interaction.guild.voice_client.is_playing() or interaction.guild.voice_client.is_paused()):
            interaction.guild.voice_client.stop()
            await interaction.response.send_message("Siguiente cancion", delete_after=10)
        else:
            await interaction.response.send_message("no hay nada sonando para saltar de cancnion", delete_after=10)

    #@discord.ui.button(label="Back", style=discord.ButtonStyle.red)
    #async def button_Back(self, button,interaction):
        #await button.response.send_message("se comenzo la reproduccion xd")

#vista de botones para la rocola
class View(discord.ui.View):
    
    #botones
    @discord.ui.button(label="Techno", style=discord.ButtonStyle.red)
    async def button_Techno(self,interaction: discord.Interaction, button):
        #await button.response.send_message("se comenzo la reproduccion xd")
        await Play_genero_musical(interaction, 0)

    @discord.ui.button(label="Rap", style=discord.ButtonStyle.red)
    async def button_Rap(self,interaction, button):
        #await button.response.send_message("se comenzo la reproduccion xd")
        await Play_genero_musical(interaction, 1)

    @discord.ui.button(label="Rock", style=discord.ButtonStyle.red)
    async def button_Rock(self,interaction, button):
        #await button.response.send_message("se comenzo la reproduccion xd")
        await Play_genero_musical(interaction, 2)

    @discord.ui.button(label="Metal", style=discord.ButtonStyle.red)
    async def button_Metal(self,interaction, button):
        #await button.response.send_message("se comenzo la reproduccion xd")
        await Play_genero_musical(interaction, 3)

    @discord.ui.button(label="Pop", style=discord.ButtonStyle.red)
    async def button_Pop(self,interaction, button):
        #await button.response.send_message("se comenzo la reproduccion xd")
        await Play_genero_musical(interaction, 4)


#vista libre para usar
class BotonesModoRocola(discord.ui.View):
    @discord.ui.button(label="Playlist", style=discord.ButtonStyle.red)
    async def button_Playlist(self, button,interaction):
        
        embed = discord.Embed(title="Modo Playlist", color = discord.Color.red())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
        embed.add_field(name="Selecciona un Genero", value="")
        await button.response.send_message(embed=embed ,view=ViewGeneros())


    @discord.ui.button(label="DJ-SET", style=discord.ButtonStyle.red)
    async def button_DJSet(self, button,interaction):
        await button.response.send_message("se comenzo la reproduccion xd")


#VISTAS PARA DROPDOWN MENU

#MAQUETA DE VISTA DROP DOWN MENU
class MenuTechno(discord.ui.Select):
    def __init__(self):
        options = [
            #aqui se deberia llenar con la informacion de los json, se deberia extraer de ellos el genero de cada playlist
            discord.SelectOption(
                label="Hard Techno"
                #description="Hard Techno"
            ),
            discord.SelectOption(
                label="Acid Techno",
                
            ),
            discord.SelectOption(
                label="Melodic Techno"
                
            ),
            discord.SelectOption(
                label="Early Techno"
                
            )
        ]

        super().__init__(placeholder="Techno", min_values=1,max_values=1, options=options)

    async def callback(self, interaction:discord.Interaction):
        if self.values[0] == "Hard Techno":
            await interaction.response.send_message("seleccionaste hardtechno", delete_after=120)
            

        elif self.values[0] == "Acid Techno":
            await interaction.response.send_message("seleccionaste acid techno", delete_after=120)

        elif self.values[0] == "Melodic Techno":
            await interaction.response.send_message("seleccionaste melodic techno", delete_after=120)

        elif self.values[0] == "Early Techno":
            Play_genero_musical(interaction, 3)


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
        

class MenuGeneros(discord.ui.Select):
    def __init__(self):
        options = [
            #aqui se deberia llenar con la informacion de los json, se deberia extraer de ellos el genero de cada playlist
            discord.SelectOption(
                label="Electronica"
                #description="Hard Techno"
            ),
            discord.SelectOption(
                label="Rap",
                
            ),
            discord.SelectOption(
                label="Trap",
                
            ),
            discord.SelectOption(
                label="Metal"
                
            ),
            discord.SelectOption(
                label="Pop"
                
            ),
            discord.SelectOption(
                label="Urbano"
                
            )
        ]

        super().__init__(placeholder="Generos Musicales", min_values=1,max_values=1, options=options)

    async def callback(self, interaction:discord.Interaction):
        if self.values[0] == "Electronica":
            #await interaction.response.send_message("seleccionaste hardtechno", delete_after=120)
            embed = discord.Embed(title="Modo Playlist", color = discord.Color.red())
            embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")
            embed.add_field(name="Selecciona el subgenero", value="")
            await interaction.response.edit_message(embed=embed, view=MenuElectronica())
            

        elif self.values[0] == "Rap":
            await interaction.response.send_message("seleccionaste acid techno", delete_after=120)

        elif self.values[0] == "Trap":
            await interaction.response.send_message("seleccionaste melodic techno", delete_after=120)

        elif self.values[0] == "Metal":
            Play_genero_musical(interaction, 3)

        elif self.values[0] == "Pop":
            await interaction.response.send_message("seleccionaste melodic techno", delete_after=120)

        elif self.values[0] == "Urbano":
            await interaction.response.send_message("seleccionaste melodic techno", delete_after=120)


class MenuElectronica(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(MenuTechno())


class ViewGeneros(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(MenuGeneros())

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

#reproduccion de rocola
async def Play_genero_musical(interaction, genero: int):
    await interaction.response.defer()
    
    if interaction.user.voice is None:
        await interaction.followup.send("Mame joven, unase a un canal de voz primero", delete_after=10)
        return

    voice_channel = interaction.user.voice.channel

    if voice_channel is None:
        await interaction.followup.send("Mame joven, unase a un canal de voz primero", delete_after=10)
        return
    
    voice_client = interaction.guild.voice_client

    if voice_client is None:
        voice_client = await voice_channel.connect()
    elif voice_channel != voice_client.channel:
        await voice_client.move_to(voice_channel)

    ydl_options = {
        "format": "bestaudio[abr<=96]/bestaudio",
        "noplaylist": False,
        "ignoreerrors": True,
        "quiet": True,
        "playlistend": 25,
        "youtube_include_dash_manifest": False,
        "youtube_include_hls_manifest": False,
    }

    generos_musicales = [
        "hardtechno",
        "acidtechno",
        "melodictechno",
        "https://www.youtube.com/watch?v=84sHTvn6xf8&list=PL8uhM5Q8xUMoj4yoX2hWCbvLKIcm4vBt-",#earlytechno
        "banda",
        "pop"
    ]

    #query = "ytsearch1: " + generos_musicales[genero]
    entrada = generos_musicales[genero]
    query = entrada if es_url(entrada) else f"ytsearch1:{entrada}"
    results = await search_ytdlp_async(query, ydl_options)
    #tracks = results.get("entries", [])
    tracks = results

    if tracks is None:
        await interaction.followup.send("No se encontraron resultados", delete_after=10)
        return
    
    #todo lo que esta aqui abajo se ejecuta solo si se encontro resultados de la busqueda
    #first_track = tracks[0]
    guild_id = str(interaction.guild_id)
    if SONG_QUEUES.get(guild_id) is None:
        SONG_QUEUES[guild_id] = deque()

    for track in tracks:
        if track is None:
            continue

        audio_url = track["url"]
        title = track.get("title", "Untitled")
        duration = track.get("duration", 0)
        thumbnail = track.get("thumbnail")
        SONG_QUEUES[guild_id].append((audio_url, title, duration,thumbnail))


    if voice_client.is_playing() or voice_client.is_paused():
        await interaction.followup.send(f"Platlist de: **{generos_musicales[genero]}**", delete_after=20)
    else:
        await play_next_song(voice_client, guild_id, interaction.channel, interaction.user.name)


#weas de youtube

def es_url(texto):
    return texto.startswith(("https://"))

async def search_ytdlp_async(query, ydl_opts):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, lambda: _extract(query, ydl_opts))

async def play_next_song(voice_client, guild_id, channel, socilitado_por): #la comparte la rocola y el modo reproduccion por cancniones
    if SONG_QUEUES[guild_id]:
        audio_url, title, duration,thumbnail = SONG_QUEUES[guild_id].popleft()
        mins, secs = divmod(duration, 60)
        duration_str = f"{mins}:{secs:02}"
        ffmpeg_options = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn -c:a libopus -b:a 96k"
        }
        source = discord.FFmpegOpusAudio(audio_url, executable= "bin\\ffmpeg\\ffmpeg.exe", **ffmpeg_options)

        def after_play(error):
            if error:
                print(f"Error playing {title}: {error}")
            asyncio.run_coroutine_threadsafe(play_next_song(voice_client,guild_id, channel, socilitado_por), client.loop)

        ##embed palying##
        embed_playing = discord.Embed(title="Reproduciendo", color = discord.Color.red())
        if thumbnail:
            embed_playing.set_thumbnail(url=thumbnail)
        else:
            embed_playing.set_thumbnail(url="https://img.icons8.com/?size=100&id=VfM1DGzeu9I8&format=png&color=000000")            
        embed_playing.add_field(name =title, value="De Youtube", inline = False)
        embed_playing.add_field(name="Duracion", value= duration_str, inline=True)
        embed_playing.add_field(name="Numero", value="2", inline=True)
        embed_playing.add_field(name="Volumen", value="100%", inline=True)
        embed_playing.add_field(name ="Solicitado por: ", value= socilitado_por, inline = False)
        embed_playing.set_author(name= socilitado_por)
        ##embed playing##

        voice_client.play(source, after=after_play)
        asyncio.create_task(channel.send(embed=embed_playing, view= ViewPlaying(), delete_after=duration))

    else:
        await voice_client.disconnect()
        SONG_QUEUES[guild_id] = deque()

        
def _extract(query, ydl_opts):
    tracks = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #return ydl.extract_info(query, download=False)

        info = ydl.extract_info(query, download=False)

        for entry in info['entries']:
            if entry is None:
                continue

            if entry.get('url') is None:
                continue

            tracks.append(entry)

    return tracks

    
#fin weas youtube

load_dotenv()
client.run(os.getenv("token"))