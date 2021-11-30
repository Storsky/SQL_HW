from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os

class AudioTag:
    
    def __init__(self, path):
        self.genre = EasyID3(path)['genre'][0]
        self.artist = EasyID3(path)['artist'][0]
        self.album = EasyID3(path)['album'][0]
        self.title = EasyID3(path)['title'][0]
        self.year = EasyID3(path)['date'][0]
        self.duration = MP3(path).info.length
       
    def get_tags(self):
        tags_dict = {'genre': self.genre, 'artist': self.artist, 'album': self.album, 'title':self.title, 'year': self.year, 'duration': self.duration}
        return tags_dict   
        

