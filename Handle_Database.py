import sqlalchemy
from ID3_mutagen import AudioTag
from random import randint


class DataBase:
    def __init__ (self, username, user_password, name_db):
        self.db = f'postgresql://{username}:{user_password}@localhost:5432/{name_db}'
        
        
    
    
    def add_to_db (self, song_tags):
        engine = sqlalchemy.create_engine(self.db)
        connection = engine.connect()  
        
        
        search = connection.execute(f"""SELECT genre_id, name_genre 
        FROM Genre 
        WHERE name_genre = '{song_tags['genre']}'
        ;""").fetchall()
        if search != []: 
            print('Уже есть в бд')
            temp_genre = search[0][0]
        else:
            print('Данного жанра нет в БД, но будет')
            connection.execute(f"""INSERT INTO Genre(name_genre)
            VALUES ('{song_tags['genre']}')
            ; """)
            search = connection.execute(f"""SELECT genre_id, name_genre 
            FROM Genre 
            WHERE name_genre = '{song_tags['genre']}'
            ;""").fetchall()
            temp_genre = search[0][0]
        
        
        search = connection.execute(f"""SELECT artist_id, name_artist 
        FROM artist 
        WHERE name_artist = '{song_tags['artist']}'
        ;""").fetchall()
        if search != []: 
            print('Уже есть в бд')
            temp_artist = search[0][0]
        else:
            print('Данного исполнителя нет в БД, но будет')
            connection.execute(f"""INSERT INTO artist(name_artist)
            VALUES ('{song_tags['artist']}')
            ; """)
            search = connection.execute(f"""SELECT artist_id, name_artist 
            FROM artist 
            WHERE name_artist = '{song_tags['artist']}'
            ;""").fetchall()
            temp_artist = search[0][0]

        search = connection.execute(f"""SELECT album_id, album_name 
        FROM album 
        WHERE album_name = '{song_tags['album']}'
        ;""").fetchall()
        if search != []: 
            print('Уже есть в бд')
            temp_album = search[0][0]
        else:
            print('Данного альбома нет в БД, но будет')
            connection.execute(f"""INSERT INTO album(album_name, year, rate)
            VALUES ('{song_tags['album']}', '{song_tags['year']}', '{randint(300, 500)/100}')
            ; """)
            search = connection.execute(f"""SELECT album_id, album_name
            FROM album 
            WHERE album_name = '{song_tags['album']}'
            ;""").fetchall()
            temp_album = search[0][0]

        search = connection.execute(f"""SELECT track_id, name_track 
        FROM track 
        WHERE name_track = '{song_tags['title']}'
        ;""").fetchall()
        if search != []: 
            print('Уже есть в бд')
            temp_track = search[0][0]
        else:
            print('Данного трeка нет в БД, но будет')
            connection.execute(f"""INSERT INTO track(name_track, duration, album)
            VALUES ('{song_tags['title']}', '{song_tags['duration']:.{2}f}', {temp_album})
            ; """)
            
            search = connection.execute(f"""SELECT track_id, name_track 
            FROM track 
            WHERE name_track = '{song_tags['title']}'
            ;""").fetchall()
            temp_track = search[0][0]

    
    
    
    def create_mixtape(self, name, year):
        engine = sqlalchemy.create_engine(self.db)
        connection = engine.connect() 
        connection.execute(f"""INSERT INTO mixtape(name, year) 
        VALUES ('{name}', {year});""")
        id_mixtape = connection.execute(f"""SELECT id 
        FROM mixtape 
        WHERE name = '{name}'""").fetchone()[0]
        for i in range(5):
            a = randint(1, 55)
            connection.execute(f"""INSERT INTO mixtrack(track, mixtape)
            VALUES ({a}, {id_mixtape})""") 
        return id_mixtape       

    
    
    
    
    def fill_genreartist(self, artist_id, genre_id):
        engine = sqlalchemy.create_engine(self.db)
        connection = engine.connect() 
        connection.execute(f"""INSERT INTO genreartist (genre, artist) 
        VALUES ({genre_id}, {artist_id});""")
        print('Успешно')

    
    
    
    def fill_albumartist(self, album_id, artist_id):
        engine = sqlalchemy.create_engine(self.db)
        connection = engine.connect() 
        connection.execute(f"""INSERT INTO albumartist (album, artist) 
        VALUES ({album_id}, {artist_id});""")
        print('Успешно')



    
    def requests(self, var):
        engine = sqlalchemy.create_engine(self.db)
        connection = engine.connect()    
        
        if var == 1:
            search = connection.execute("""SELECT album_name, year 
            FROM album
            WHERE year = 2020;""").fetchall()
            return(search)
        
        if var == 2:
            search = connection.execute("""SELECT name_track, duration 
            FROM track
            ORDER BY duration DESC, name_track LIMIT 1;""").fetchall()
            return(search)
        
        if var == 3:
            search = connection.execute("""SELECT name_track, duration
            FROM TRACK
            WHERE duration >= 210;""").fetchall()
            return(search)
        
        if var == 4:
            search = connection.execute("""SELECT name
            FROM mixtape
            WHERE year BETWEEN 2018 and 2020;""").fetchall()
            return(search)
        
        if var == 5:
            search = connection.execute("""SELECT name_artist
            FROM artist
            WHERE name_artist not LIKE '%% %%' ;""").fetchall()
            return(search)
        
        
        if var == 6:
            search = connection.execute("""SELECT name_track
            FROM track
            WHERE name_track LIKE '%%Be %%';""").fetchall()
            return(search)
    