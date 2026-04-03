# Spotify Playlist Maker 🎵

[![Python](https://img.shields.io/badge/python-3.8+-blue?logo=python)](https://www.python.org/) 
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Automatically creates a Spotify playlist from the **Billboard Hot 100** for any date you choose.

---

## 🚀 Features

- Scrapes Billboard Hot 100 songs for a specified date.
- Searches for each song on Spotify.
- Creates a **private playlist** in your Spotify account.
- Adds all found songs automatically.
- Handles featured artists and complex song titles.

---

## 🛠 Requirements

- Python 3.8+
- Spotify Developer Account
- Dependencies:

```bash
pip install beautifulsoup4 requests spotipy
```
⚙️ Setup
Create a Spotify App
Go to the Spotify Developer Dashboard
 and create a new app to get:
Client ID
Client Secret
Redirect URI (example: http://127.0.0.1:8888/callback)

