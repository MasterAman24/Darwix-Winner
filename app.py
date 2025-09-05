import streamlit as st
import os

from config import API_KEY, LANGUAGE_VOICES
from utils import add_bg_from_local
from emotion_detection import (
    detect_emotion_vader,
    detect_emotion_transformer,
    detect_multi_emotions,
    keyword_boost,
)
from voice_utils import (
    get_voice_params,
    scale_voice_params,
    blend_voice_params,
)
from tts_service import synthesize_speech_with_api_key

add_bg_from_local("background.jpg")

st.title("🎙️ Empathy Engine - Multilingual Emotional Speech by Aman Agarwal")

text = st.text_area("Enter your text:", "I am Aman Agarwal, I am very happy to get this opportunity. Thank You Darwix")
multi_mode = st.checkbox("Detect multiple emotions?")
model_choice = st.radio("Choose Base Emotion Detection Model:", ["VADER (fast)", "Transformer (accurate)"])
use_ssml = st.checkbox("Use SSML for advanced speech control", value=True)
user_rate = st.slider("Speaking Speed (slower ← → faster)", 0.8, 1.2, 1.0, step=0.05)
language_choice = st.selectbox("Choose Output Language:", list(LANGUAGE_VOICES.keys()))

if st.button("Generate Speech"):
    lang_data = LANGUAGE_VOICES[language_choice]
    lang_code, base_voice = lang_data["lang"], lang_data["voice"]

    if multi_mode:
        emotions = detect_multi_emotions(text)
        st.write("### 🎭 Detected Multiple Emotions (all)")
        for e, score in emotions:
            st.write(f"- {e}: {score*100:.1f}%")
        top_emotions = emotions[:2]
        params = blend_voice_params(top_emotions, base_voice)

    else:
        if model_choice == "VADER (fast)":
            emotion, scores = detect_emotion_vader(text)
        else:
            emotion, scores = detect_emotion_transformer(text)
        emotion = keyword_boost(text, emotion)
        st.write(f"**Detected Emotion:** {emotion}")
        confidence = abs(scores.get("compound", 0.5))
        params = scale_voice_params(get_voice_params(emotion, base_voice), confidence, user_rate, emotion)

    st.write(f"**Final Voice Parameters:** {params}")

    audio_path = synthesize_speech_with_api_key(text, params, API_KEY, lang_code, use_ssml)
    with open(audio_path, "rb") as audio_file:
        st.audio(audio_file.read(), format="audio/mp3")
    os.remove(audio_path)
