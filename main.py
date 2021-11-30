import os
from ID3_mutagen import AudioTag
from Handle_Database import DataBase



folder = ''
database = 'musicshop'
username = 'akvasnikov'
password = '123456'

def fill_db():
    db = DataBase(username, password, database)
    files = os.listdir(folder)
    for file in files:
        if file.split('.')[-1] == 'mp3':
            file_path = os.path.join(folder, file)
            audio = AudioTag(file_path)
            tags = audio.get_tags()
            db.add_to_db(tags)

if __name__ == '__main__':
    db = DataBase(username, password, database)
    print(db.requests(1))
    print(db.requests(2))
    print(db.requests(3))
    print(db.requests(4))
    print(db.requests(5))
    print(db.requests(6))




           