import json
import musicbrainzngs
class Data():
    def __init__(self) -> None:
        pass
    def load_data(self, data:str):
        f=open(data)
        data_list=json.load(f)
        return data_list
    
    def create_artists_list(self, data_list):
        artists_dict=dict()
        for x in data_list:
            artist = x['master_metadata_album_artist_name']
            artists_dict[artist] = artists_dict.get(artist,0)+1
        
        artists_list=[x for x in artists_dict.items() if x[0]!=None]
        artists_list = sorted(artists_list, key=lambda x: x[1], reverse=True)[0:10]
        print("\nYour favourite artists are:\n")
        for i, x in enumerate(artists_list,start=1):
            print(str(i).zfill(2), x[0])

        return artists_list

    def create_tracks_list(self, data_list):
        tracks_dict=dict()
        for x in data_list:
            artist = x['master_metadata_album_artist_name']
            album = x['master_metadata_album_album_name']
            track = x['master_metadata_track_name']
            tracks_dict[(artist, album, track)] = tracks_dict.get((artist, album, track),0)+1
        tracks_list=sorted(tracks_dict.items(), key=lambda x:x[1], reverse=True)
        tracks_list=[x for x in tracks_list if x[0]!=(None, None, None)][0:50]
        print("\nYour favourite tracks are:\n")
        for x,y in enumerate(tracks_list, start=1):
            print(f"{str(x).zfill(2)}: {y[0][2]} by {y[0][0]} from the album {y[0][1]}" )
        
        return tracks_list

    def create_albums_list(self, data_list):
        musicbrainzngs.set_useragent("my_album_app", 3.0,"xxx@gmail.com" )
        albums_dict=dict()
        for x in data_list:
            artist = x['master_metadata_album_artist_name']
            album = x['master_metadata_album_album_name']
            albums_dict[(artist, album)] = albums_dict.get((artist, album),0)+1

        albums_list = sorted(albums_dict.items(), key=lambda x:x[1], reverse=True)
        albums_list = [list(x) for x in albums_list if x[0] != (None, None)]
        albums_list = [list(x) for x in albums_list if (len(albums_list) < 21 or x[1] >= albums_list[20][1])]

        print("\nCollecting albums info from MusicBrainz ...")

        for x in albums_list:
            result = musicbrainzngs.search_releases(artist=x[0][0], release=x[0][1],limit=0)['release-list'][0]['medium-track-count']
            x.append(result)
        
        albums_list=[x for x in albums_list if x[2]>3]
        for x in albums_list:
            x[1]=x[1]//x[2]
            x.remove(x[2])
        
        albums_list=sorted(albums_list, key=lambda x:x[1], reverse=True)
        if len(albums_list)>=10:
            albums_list=albums_list[0:10]

        print("\nYour favourite albums are:\n")
        for x,y in enumerate(albums_list, start=1):
            print(f"{str(x).zfill(2)}: {y[0][1]} by {y[0][0]}" )
        return albums_list