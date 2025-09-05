from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

API_KEY = "AIzaSyCjD7ALwCl0uekZEd8xffcgAu5M7yQbsfs"

analyzer = SentimentIntensityAnalyzer()
transformer_analyzer = pipeline("sentiment-analysis")
multi_emotion_analyzer = pipeline(
    "text-classification",
    model="joeddav/distilbert-base-uncased-go-emotions-student",
    return_all_scores=True
)

LANGUAGE_VOICES = {
    "English (US)": {"lang": "en-US", "voice": "en-US-Wavenet-D"},
    "Hindi": {"lang": "hi-IN", "voice": "hi-IN-Wavenet-A"},
    "Spanish": {"lang": "es-ES", "voice": "es-ES-Wavenet-C"},
    "French": {"lang": "fr-FR", "voice": "fr-FR-Wavenet-B"},
    "German": {"lang": "de-DE", "voice": "de-DE-Wavenet-B"},
    "Italian": {"lang": "it-IT", "voice": "it-IT-Wavenet-C"},
    "Japanese": {"lang": "ja-JP", "voice": "ja-JP-Wavenet-B"},
}

EMOTION_KEYWORDS = {
    "very happy": ["ecstatic", "thrilled", "amazing", "wonderful", "fantastic", "awesome"],
    "happy": ["glad", "pleased", "good", "great", "nice", "joyful"],
    "very sad": ["devastated", "heartbroken", "miserable", "hopeless", "crying"],
    "sad": ["unhappy", "disappointed", "upset", "lonely"],
    "surprised": ["wow", "unbelievable", "shocking", "unexpected", "no way"],
    "inquisitive": ["why", "how", "what if", "curious", "wonder"],
    "concerned": ["worried", "anxious", "afraid", "nervous", "scared"],
}
