import raw, clear
data=raw.Data()
data_list = data.join_data('raw_data')
data_list = data.filter(data_list)
data.clear_and_save(data_list)
del data
data=clear.Data()
data_list=data.load_data('data.json')
artist_list=data.create_artists_list(data_list)
tracks_list=data.create_tracks_list(data_list)
albums_list=data.create_albums_list(data_list)






