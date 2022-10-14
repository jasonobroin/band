"Report band stats from setlist.fm"

import config

apiKey = 'x-api-key'
REQ_URL = 'https://api.setlist.fm/rest/1.0/artist'
SETLIST_REQ = 'setlists?p=1'
artist_id = 'a1812f41-871c-4a8a-b669-bafa5e9f2c8f'

import json
import requests
import pprint as pp

def load_setlist_data_from_setlist_fm(artist_id):
    "Load setlist data as JSON from setlist.fm based on an artist ID"
    headers = {
              'Accept': 'application/json',
              f'{apiKey}': f'{config.API_KEY}'
    }
    rsp = requests.get(f'{REQ_URL}/{artist_id}/{SETLIST_REQ}' , headers=headers, auth=None)

    return json.loads(rsp.content)

if __name__ == '__main__':
    setlist_json = load_setlist_data_from_setlist_fm(artist_id)
#    print(json.dumps(setlist_json, indent=2))

    songs = {}

    shows = setlist_json["setlist"]
    for show in shows:
        for set in show["sets"]["set"]:
            for song in set["song"]:
                try:
                    songs[song["name"]] +=1
                except KeyError:
                    songs[song["name"]] = 1
#                print(json.dumps(song["name"], indent=2))

    print("\n\nSorted list - most played\n\n")
    for song, count in sorted(songs.items(), key=lambda x:x[1], reverse=True):
        print(f'{song} : {count}')
#    print(songs)
