import os
import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import VideosSearch
from pytube import Playlist
from pytube import YouTube
from moviepy.editor import VideoFileClip

# Replace these with your own credentials
client_id = 'REPLACE_THIS'
client_secret = 'REPLACE_THIS'
save_directory = "Downloads"

# Initialize the Spotipy client with your credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def convert_to_playlist_uri(url):
    # Check if the input URL starts with the expected pattern for Spotify playlists
    if url.startswith("https://open.spotify.com/playlist/"):
        # Split the URL using "/" as the delimiter and get the last part (the unique identifier)
        parts = url.split("/")
        playlist_id = parts[-1]

        # Construct the correct Spotify playlist URI
        playlist_uri = f"spotify:playlist:{playlist_id}"
        return playlist_uri
    # Check if the input URL starts with the pattern for YouTube playlists
    elif "list=" in url:
        return "YouTube Playlist URL"
    # Check if the input URL starts with the pattern for YouTube songs
    elif "watch?v=" in url:
        return "YouTube Song URL"
    else:
        return None

# Spotify
def get_song_names_from_playlist(playlist_uri):
    results = sp.playlist_tracks(playlist_uri)
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    song_names = [track['track']['name'] for track in tracks]

    return song_names

# Youtube
def get_playlist_video_links(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

        video_links = [f'https://www.youtube.com{url}' for url in playlist.video_urls]

        return video_links
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def search_song_on_youtube(song_name):
    try:
        videos_search = VideosSearch(song_name, limit=1)
        results = videos_search.result()

        if results and "result" in results:
            video_url = results["result"][0]["link"]
            return video_url
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def download_youtube_audio_as_mp3(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()

        # Create the directory if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        audio_file = stream.download(output_path=save_path)
        mp3_file = os.path.splitext(os.path.basename(audio_file))[0] + ".mp3"

        # Rename the downloaded audio file to have an MP3 extension
        os.rename(os.path.join(save_path, os.path.basename(audio_file)), os.path.join(save_path, mp3_file))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    user_input = input("Enter a Spotify playlist or YouTube playlist URL: ")
    playlist_uri = convert_to_playlist_uri(user_input)

    if playlist_uri == "YouTube Playlist URL":
        video_links = get_playlist_video_links(user_input)
        if video_links:
            print(f"Video Links in the Playlist:")
            for i, link in enumerate(video_links, start=1):
                # Clean up the link
                link = link.replace("https://www.youtube.comhttps://www.youtube.com", "https://www.youtube.com")
                video = YouTube(link)
                video_name = video.title
                download_youtube_audio_as_mp3(link, save_directory)
                print(f"{i}. Video: {video_name}")
                print(f"   Download and conversion of {link} completed.")
        else:
            print("Error fetching video links.")
    elif playlist_uri == "YouTube Song URL":
        download_youtube_audio_as_mp3(user_input, save_directory)
        print("Download and conversion of the YouTube song completed.")
    elif playlist_uri:
        song_names = get_song_names_from_playlist(playlist_uri)
        if song_names:
            print("Songs in the playlist:")
            for i, song in enumerate(song_names, start=1):
                video_url = search_song_on_youtube(song)
                if video_url:
                    download_youtube_audio_as_mp3(video_url, save_directory)
                    print(f"{i}. {song}")
                    print(f"Download and conversion of {video_url} completed.")
                else:
                    print(f"{i}. {song}")
                    print("Song not found on YouTube.")
        else:
            print("Error fetching playlist songs.")
    else:
        print("Invalid URL format. Please use a valid Spotify or YouTube URL.")
