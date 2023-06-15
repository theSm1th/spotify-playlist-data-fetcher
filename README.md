# spotify-playlist-data-fetcher
A small program for downloading the metadata (ID, name and album cover) of songs in a Spotify playlist. 
Made entirely because I have a 1200+ song playlist that I can't afford to lose - the names of the songs, atleast.

## Usage
Requires the python modules requests and spotipy.

### Setup:
1. Go to [Spotify's developer dashboard](https://developer.spotify.com/dashboard/) - log in and set up an app.
(For a more detailed explanation - you can see this guide at [codeproject.com](https://www.codeproject.com/Tips/5276627/HowTo-Setup-a-Spotify-API-App-in-the-Spotify-Devel))

This has to be done because Spotify does not allow unauthenticated access to their API. For more information on the Client Credentials Flow, see [this](https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow) article on Spotify's website.

2. Assign the two variables in variables.py, cli_id and cli_sec to your app ID and secret respectively.
3. Run the program and input your playlist ID (the latter part of an playlist link - see https://open.spotify.com/playlist/ ***37i9dQZF1DX5Q27plkaOQ3?si=83f21db5758f4136***)
4. The song_covers folder will be populated with song covers (where the file name is the song identifier) and the songs.txt file will be populated with song names, IDs and links to album cover.

