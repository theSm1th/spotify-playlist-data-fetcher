import requests
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
import os

import variables

s = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(client_id=variables.cli_id, client_secret=variables.cli_sec))

while True:
    playlist_id = input("Playlist ID : ")
    try:
        data = s.playlist_items(playlist_id)
        break
    except spotipy.exceptions.SpotifyException:
        pass


current_path = os.getcwd()


def write_tracks(text_file, tracks):
    with open(text_file, 'a') as file_out:
        while True:
            for item in tracks['items']:
                if 'track' in item:
                    track = item['track']
                else:
                    track = item
                try:
                    track_url = track['external_urls']['spotify']

                    track_info = s.track(track_url)
                    try:
                        count = 0
                        artistString = ""
                        songString = ""

                        for _ in track_info["artists"]:
                            artistString = artistString + " & " + track_info["artists"][count]["name"]
                            count += 1
                        artistString = artistString[3:]

                        songString = artistString + " - " + track_info["name"]
                        cover_url = track_info["album"]["images"][0]["url"]
                        song_id = track_info["album"]["id"]

                        print("LOG : Found {}, url {}".format(songString, cover_url))

                        with open(r"{}\\song_covers\\{}.jpg".format(current_path, song_id), 'wb') as handle:
                            response = requests.get(cover_url, stream=True)

                            if not response.ok:
                                print(response)

                            for block in response.iter_content(1024):
                                if not block:
                                    break

                                handle.write(block)
                        file_out.write("{} , {} , {} \n".format(songString, song_id, cover_url))

                    except UnicodeEncodeError:
                        pass
                except KeyError:
                    print(u'Skipping track {0} by {1} (local only?)'.format(
                        track['name'], track['artists'][0]['name']))
            if tracks['next']:
                tracks = s.next(tracks)
            else:
                break


write_tracks("songs.txt", data["tracks"])
