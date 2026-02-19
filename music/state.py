from collections import deque

SONG_QUEUES = {}

def get_queue(guild_id):
    if guild_id not in SONG_QUEUES:
        SONG_QUEUES[guild_id] = deque()
    return SONG_QUEUES[guild_id]