import json
import os
from utils.controlls_Json.lectura import cargar_links_DjSet

JSON_LIVESETS = "LiveSets.json"
JSON_PLAYLIST = "PLayList.json"
JSON_ALLSONGSPLAYLIST = "AllSongsPLaylist.json"

def guardar_links_DjSets(nombre, genero, url): #seria solo para live sets
   data = cargar_links_DjSet()

   if( any(track["links"]==url for track in data)):
       return False
   
   data.append({
       "nombre": nombre,
       "genero": genero,
       "links": url
    })
   
   with open(JSON_LIVESETS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        return True

def guardar_linksPlaylist(data): #seria solo para playlist
    with open(JSON_PLAYLIST, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)



def guardar_all_songs(data): #seria solo para all songs
    with open(JSON_ALLSONGSPLAYLIST, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)



