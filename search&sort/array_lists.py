class Album():
    def __init__(self,album_name,number_of_songs,album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"Album Name: {self.album_name} \n" \
                f"Album Artist: {self.album_artist} \n" \
                f"Number of Songs: {self.number_of_songs} \n" \
            "-----------------------------------------"



albums1 = [Album('Take Care', 15, 'Drake'),
           Album('Trapsoul', 14, 'Bryson Tiller'),
           Album('Stoney', 11, 'Post Malone'),
           Album('SOS', 18, 'SZA'),
           Album('Falling or Flying', 16, 'Jorja Smith')
           ]

albums1 = sorted(albums1, key=lambda Album:Album.number_of_songs)

# for album in albums1:
#     print(str(album))


holding = albums1[1]

albums1[1] = albums1[2]
albums1[2] = holding

albums2 = [
    Album('Views',16,'Drake'),
    Album('Forrest Hills', 14, 'J cole'),
    Album('Pyschodrama', 17, 'Dave'),
    Album('College Dropout', 18, 'Kanye West'),
    Album('Channel Orange', 16, 'Frank Ocean')
]

albums2.extend(albums1)

extra_albums = [
    Album('Dark Side Of The Moon',9, 'Pink Floyd'),
    Album('Opps I Did it Again', 16, 'Britney Spears')
]

albums2.extend(extra_albums)

albums2 = sorted(albums2, key=lambda Album:Album.album_name)

# for albums in albums2:
#     print(str(albums))


for index, album in enumerate(albums2):
    if album.album_name == 'Dark Side Of The Moon':
        print(index)
    



