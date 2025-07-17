from flask import Flask, request, send_file
from TTS.api import TTS
import io
from scipy.io.wavfile import write as wav_write

app = Flask(__name__)

# Load default English model. Adjust model name as needed.
TTS_MODEL = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

@app.route('/tts')
def tts_route():
    text = request.args.get('text', '').strip()
    if not text:
        return 'No text', 400
    wav = TTS_MODEL.tts(text)
    memfile = io.BytesIO()
    wav_write(memfile, TTS_MODEL.synthesizer.output_sample_rate, wav)
    memfile.seek(0)
    return send_file(memfile, mimetype='audio/wav')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
