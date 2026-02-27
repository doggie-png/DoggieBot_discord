import json
import os


JSON_LIVESETS = "LiveSets.json"
JSON_PLAYLIST = "PLayList.json"
JSON_ALLSONGSPLAYLIST = "AllSongsPLaylist.json"

def cargar_links_DjSet(): #seria solo para live sets
    if not os.path.exists(JSON_LIVESETS):
        return []

    try:
        with open(JSON_LIVESETS, "r", encoding="utf-8") as f:
            data = json.load(f)

            if not isinstance(data, list):
                return []

            return data

    except json.JSONDecodeError:
        return []
        
    


def cargar_linksPlaylist(): #seria solo para playlist
    if not os.path.exists(JSON_PLAYLIST):
        return []

    try:
        with open(JSON_PLAYLIST, "r", encoding="utf-8") as f:
            data = json.load(f)

            if not isinstance(data, list):
                return[]
            
            return data
        
    except json.JSONDecodeError:
        return []
    


def cargar_all_songs(): #seria solo para all songs
    if not os.path.exists(JSON_ALLSONGSPLAYLIST):
        return {"nombre":[],"host":[],"links": []}

    with open(JSON_ALLSONGSPLAYLIST, "r", encoding="utf-8") as f:
        return json.load(f)
    

