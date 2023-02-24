# spotify-analytics
Spotify Extended Playback History Analytics

This code helps you deal with extended playback statistics from Spotify. You can obtain these statistics by sending a request in your account's privacy settings. All you need to do is put the text files you receive into the "raw_data" folder, but only those files that contain the word "song" in their names.
After running the code, you will be prompted to provide the time range you're interested in, and after a while, you'll be able to see your top artists, songs, and albums within that range. Here are a few reasons why this approach is better than using hundreds of apps and online services:
1. Online, you can only choose from three time ranges: month, six months, and all time. With this code, you can specify the exact range of time you want to analyze.
2. This code includes an extra feature - the best albums - which is unique.
3. It's more enjoyable to obtain your own statistics.
Please note:
To use this code, run the "app.py" file.
This code uses MusicBrainz files, which are included. Alternatively, you can install them via pip. For more information, visit the MusicBrainz website.
Once the data has been filtered, it is stored in the "data.json" file in the main folder. If you want to use this data without making any changes, you don't need to run lines 2-6 in the "app.py" file.
I have included some samples in the "raw_data" folder that have been cleared of my personal information. If you use your own files, it is recommended that you uncomment lines 67-83 in "raw.py" to keep the files smaller.
