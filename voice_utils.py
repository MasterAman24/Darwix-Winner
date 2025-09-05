from config import EMOTION_KEYWORDS

def get_voice_params(emotion, base_voice="en-US-Wavenet-D"):
    mapping = {
        "very happy": {"voice": base_voice, "pitch": 6.0, "speaking_rate": 1.2, "volume_gain_db": 5.0},
        "happy": {"voice": base_voice, "pitch": 3.0, "speaking_rate": 1.1, "volume_gain_db": 3.0},
        "neutral": {"voice": base_voice, "pitch": 0.0, "speaking_rate": 1.0, "volume_gain_db": 0.0},
        "sad": {"voice": base_voice, "pitch": -3.0, "speaking_rate": 0.9, "volume_gain_db": -2.0},
        "very sad": {"voice": base_voice, "pitch": -6.0, "speaking_rate": 0.8, "volume_gain_db": -4.0},
        "surprised": {"voice": base_voice, "pitch": 5.0, "speaking_rate": 1.15, "volume_gain_db": 4.0},
        "inquisitive": {"voice": base_voice, "pitch": 2.0, "speaking_rate": 1.05, "volume_gain_db": 2.0},
        "concerned": {"voice": base_voice, "pitch": -2.0, "speaking_rate": 0.9, "volume_gain_db": -1.0},
    }
    return mapping.get(emotion, mapping["neutral"])

def scale_voice_params(base_params, intensity, user_rate=1.0, emotion="neutral"):
    scaled = base_params.copy()
    scaled["pitch"] += intensity * 1.5
    rate = user_rate * base_params["speaking_rate"]
    if emotion in ["sad", "very sad"]:
        rate = min(rate, 0.9)
    scaled["speaking_rate"] = min(max(rate, 0.8), 1.2)
    scaled["volume_gain_db"] = min(base_params["volume_gain_db"] + intensity * 1.5, 8.0)
    return scaled

def blend_voice_params(emotions, base_voice="en-US-Wavenet-D"):
    if not emotions:
        return get_voice_params("neutral", base_voice)
    params = [get_voice_params(e[0].lower(), base_voice) for e in emotions]
    weights = [e[1] for e in emotions]
    total = sum(weights)
    blended = {k: sum(p[k] * w for p, w in zip(params, weights)) / total for k in params[0] if k != "voice"}
    blended["voice"] = params[0]["voice"]
    return blended

def apply_ssml_enhancements(text):
    for _, words in EMOTION_KEYWORDS.items():
        for w in words:
            if w in text.lower():
                text = text.replace(w, f'<emphasis level="strong">{w}</emphasis>')
    return f"<speak>{text}</speak>"
