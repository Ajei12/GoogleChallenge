"""A video player class."""
import random # importing standard package required to randomly play a video


from .video_library import VideoLibrary

class PlayStatus:

    def __init__(self,v=None):
        self.video = v
        self.pause = False

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playing_currently = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all videos:")
        for v in sorted(self._video_library.get_all_videos(), key=lambda v: v.title):
            print(f" {v.format()}")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video is None:
            print("Cannot play video: Video does not exist")
            return
        if video.flag:
            print(f"Cannot play video: Video is currently flagged (reason: {video.flag})")
            return
        self.stop_video(silent=True)
        print("Playing video:", video.title)
        self._playing_currently = PlayStatus(video)


    def stop_video(self, silent=False, very_silent=False):
        """Stops the current video."""
        if self._playing_currently is None:
            if not silent and not very_silent:
                print("Cannot stop video: No video is currently playing")
            return False
        if not very_silent:
                print("Stopping video:", self._playing_currently.video.title)
        self._playing_currently = None
        self._pause = False
        return True

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_unflagged()
        if not videos:
            print("No videos available")
            return
        v = random.choice(videos)
        self.play_video(v.video_id)

    def pause_video(self):
        """Pauses the current video."""
        if self._playing_currently is None:
            print("Cannot pause video: No video is currently playing")
            return
        if self._playing_currently.pause:
            print("Video is already paused:", self._playing_currently.video.title)
            return
        self._playing_currently.pause = True
        print("Pausing video:", self._playing_currently.video.title)


    def continue_video(self):
        """Resumes playing the current video."""
        if self._playing_currently is None:
            print("Cannot continue video: No video is currently playing")
            return
        if not self._playing_currently.pause:
            print("Cannot continue video: Video is not paused")
            return
        print("Continuing video:", self._playing_currently.video.title)
        self._playing_currently.pause = False


    def show_playing(self):
        """Displays video currently playing."""
        if self._playing_currently is None:
            print("No video is currently playing")
            return
        print("Currently playing:", self._playing_currently.video.format(), "- PAUSED" * self._playing_currently.pause)


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
