class Songs:
  def __init__(self, name):
    self.song=name
    self.performers=[]

  def add_performer_of_song(self, new_performer):
    self.performers.append(Performers(new_performer))
      
  def create_album_of_song(self, name_of_album):
    self.create_album_song= Album(name_of_album, self.song, self.performers)
    return self.create_album_song

class Album:
  def placement_album(self, main_object, objects):
    pod_album=[]
    pod_album.append((main_object))
    pod_album.append(objects)
    return pod_album

  def __init__(self, name_of_album, main_object, objects):
    self.album=[(name_of_album)]
    self.album.append(self.placement_album(main_object, objects))
    
  def add_new_object(self, new_object, main_object):
    for m_obj in range(1, len(self.album)):
      if self.album[m_obj][0]==main_object:
        self.album[m_obj][1].append(new_object)
        return self.album

  def add_new_song(self, new_collection):
    self.album.append(self.placement_album(new_collection.song, new_collection.performers))
    return self.album

  def add_new_performer(self, new_collection):
    self.album.append(self.placement_album(new_collection.performer, new_collection.songs))
    return self.album

class Performers:
  def __init__(self, name_of_performer):
    self.performer=name_of_performer
    self.songs=[]
  
  def add_song_of_performer(self, new_song):
    self.songs.append(Songs(new_song))
  
  def create_album_of_performer(self, name_of_album):
    self.create_album_performer= Album(name_of_album, self.performer, self.songs)
    return self.create_album_performer

class Playlists:
  def __init__(self, name):
    self.playlist=name
    self.list_of_songs=[]

  def add_song(self, name_of_song):
    self.list_of_songs.append(Songs(name_of_song))
    return self.list_of_songs[-1]

def example():
  song_1, song_2, song_3, song_6, song_7,  song_4, song_5="1", "2", "3",  "6", "7", Songs("4"), Songs("5")

  performer_1, performer_2, performer_3, performer_4=Performers("X"), Performers("Y"), "Z", "W"

  performer_1.add_song_of_performer(song_1)
  performer_1.add_song_of_performer(song_2)
  album_1=performer_1.create_album_of_performer("1x")
  performer_2.add_song_of_performer(song_3)
  album_1.add_new_performer(performer_2)

  song_4.add_performer_of_song(performer_3)
  song_5.add_performer_of_song(performer_4)
  album_2=song_4.create_album_of_song("2x")
  album_2.add_new_song(song_5)

  playlist_1, playlist_2=Playlists("x1"), Playlists("x2")
  playlist_1.add_song(song_6)
  playlist_2.add_song(song_7)

  print("Альбом 1:", album_1.album)
  print("Альбом 2:", album_2.album)
  print("Песни в плейлистах:", playlist_1.list_of_songs, playlist_2.list_of_songs)

example()
  