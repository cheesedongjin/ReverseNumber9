# ReverseNumber9

ReverseNumber9 instantly reverses TTS-generated speech and recorded audio in your browser. You can record audio, play it normally or reversed, and download the result. Text entered on the page is synthesized with a self-hosted Coqui TTS server and can also be played forward or backward.

## Setup

1. Install Python dependencies (preferably in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
2. Start the TTS server (optionally set `PORT` to choose the port):
   ```bash
   PORT=5000 python tts_server.py
   ```
   The server listens on `0.0.0.0:$PORT` and provides a `/tts?text=...` endpoint returning a WAV file.

3. Open `static/index.html` in your browser. Use HTTPS or serve the files with a local web server if your browser blocks microphone access over `file://`.

## Features

- Record audio in the browser and play or download it normally or reversed.
- Enter text which is synthesized using Coqui TTS and played back forward or backward.
- Download links are provided for both recorded and synthesized audio.
