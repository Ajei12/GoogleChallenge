"""A video playlist class."""
from .video import Video
from typing import Sequence

class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_id):
        self._playlist_id = playlist_id
        self._videos = {}

    @property
    def playlist_id(self) -> str:
        return self._playlist_id

    @property
    def videos(self) -> Sequence[Video]:
        return list(self._videos.values())

    def add_to_playlist(self,video) -> bool:
        if video.video_id in self._videos:
            return False
        self._videos[video.video_id] = video
        return True

    def remove_from_playlist(self,video_id) -> bool:
        if video_id not in self._videos:
            return False
        self._videos.pop(video_id)
        return True


