import requests
import tempfile
import base64
from voice_utils import apply_ssml_enhancements

def synthesize_speech_with_api_key(text, params, api_key, language_code, use_ssml=False):
    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={api_key}"
    input_data = {"ssml": apply_ssml_enhancements(text)} if use_ssml else {"text": text}
    body = {
        "input": input_data,
        "voice": {"languageCode": language_code, "name": params["voice"]},
        "audioConfig": {
            "audioEncoding": "MP3",
            "pitch": params["pitch"],
            "speakingRate": params["speaking_rate"],
            "volumeGainDb": params["volume_gain_db"]
        }
    }
    response = requests.post(url, json=body)
    response.raise_for_status()
    audio_content = response.json()["audioContent"]
    audio_bytes = base64.b64decode(audio_content)
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    with open(tmp_file.name, "wb") as out:
        out.write(audio_bytes)
    return tmp_file.name
