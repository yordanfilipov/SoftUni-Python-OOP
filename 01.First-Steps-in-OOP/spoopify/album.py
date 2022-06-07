from spoopify.band import Band
from spoopify.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song in self.songs:
            return f"Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        songs_to_be_removed = [s for s in self.songs if song_name == s.name]
        if not songs_to_be_removed:
            return "Song is not in the album."
        self.songs.remove(songs_to_be_removed[0])
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        result = f"Album {self.name}\n"
        for s in self.songs:
            result += "== " + s.get_info() + "\n"
        return result


