# Tubify

## Language Versions
[![English](https://img.shields.io/badge/English-English-blue)](readme.md)
[![German](https://img.shields.io/badge/Deutsch-German-blue)](readme_de.md)
[![Spanish](https://img.shields.io/badge/Español-Spanish-blue)](readme_es.md)

## Summary

Tubify is a Python-based utility that allows users to work with both Spotify and YouTube, enabling the retrieval and download of song lists from Spotify playlists and the download of audio from YouTube playlists or videos. It's a versatile tool for music enthusiasts who want to create offline collections of their favorite songs.

## Practical Implementations

In a world where music is an essential part of our lives, our utility provides a cost-effective alternative to enjoying your favorite tunes without the need for premium subscriptions. Here are some practical implementations:

- **Offline Listening**: You can save your preferred songs directly to your device, eliminating the need for a constant internet connection and reducing data usage.

- **Personal Collections**: Curate your own personalized collection of songs from various platforms to enjoy offline. No more reliance on streaming services with limited availability.

- **Backup and Redundancy**: Keep a backup of your cherished music in case it's ever removed or becomes unavailable on streaming platforms. Your music, your control.

- **Ad-Free Experience**: Say goodbye to interruptions from ads during your music sessions. Downloaded music means an uninterrupted listening experience.

- **Custom Mixtapes**: Create your custom mixtapes or playlists by handpicking your favorite tracks and organizing them just the way you like.

Our utility empowers you to take charge of your music experience, offering a more flexible and personalized way to enjoy music on your own terms.


## How to Use

1. **Prerequisites**:
   - Python installed on your system.
   - Install the required libraries: `spotipy`, `youtubesearchpython`, `pytube`, and `moviepy`.

2. **Obtaining API Credentials**:
   - If you plan to use the Spotify functionality, you need to obtain Spotify API credentials.
   - If you're working with YouTube, no API key is needed.

3. **Configuring API Credentials**:
   - To use the Spotify functionality, you need to obtain Spotify API credentials, which include a **Client ID** and a **Client Secret**. Follow these steps to obtain them:

     1. **Create a Spotify Developer Account**:
        - Visit the [Spotify for Developers](https://developer.spotify.com/dashboard/) website.
        - Log in or create a Spotify account if you don't already have one.

     2. **Create a New Spotify App**:
        - Once logged in, go to the Spotify Developer Dashboard.
        - Click on the "Create an App" or "Create a Client ID" button.
        - Fill in the required information for your app, such as its name and description.
        - You may be asked to agree to the developer terms and conditions.

     3. **Obtain Your Credentials**:
        - After creating the app, you will be provided with a **Client ID** and a **Client Secret**.
        - Replace `YOUR_SPOTIFY_CLIENT_ID` and `YOUR_SPOTIFY_CLIENT_SECRET` in the code with the credentials you received.

   - If you're using the utility solely for YouTube-related tasks, you can skip this step, as YouTube functionality does not require API credentials.

4. **Running the Tool**:
   - Execute the Python script.
   - You will be prompted to enter a Spotify or YouTube playlist URL.
   - The utility will identify the URL type and perform the corresponding action:
     - For Spotify playlists, it fetches song names and download them from YouTube.
     - For YouTube playlists, it downloads audio from each video.
     - For YouTube videos, it directly downloads the audio.

5. **Output**:
   - The songs or audio files are saved to the specified directory (`save_directory`).

6. **Enjoy**:
   - You can now enjoy your downloaded music offline or for any other purpose.

## Note

- Be aware of the terms of use and copyright restrictions when downloading content from online platforms like Spotify and YouTube. Respect the rights of content creators and adhere to all legal regulations.

## License

This project is licensed under the [GNU General Public License, version 3.0](LICENSE). You can find the full license text [here](https://www.gnu.org/licenses/gpl-3.0.html).
