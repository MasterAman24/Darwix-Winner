from config import analyzer, transformer_analyzer, multi_emotion_analyzer, EMOTION_KEYWORDS

def detect_emotion_vader(text):
    scores = analyzer.polarity_scores(text)
    comp, pos, neg = scores['compound'], scores['pos'], scores['neg']
    if pos > 0.7 and "!" in text:
        return "very happy", scores
    elif comp > 0.6:
        return "happy", scores
    elif -0.2 <= comp <= 0.2:
        return "neutral", scores
    elif neg > 0.6 or "😭" in text:
        return "very sad", scores
    elif comp < -0.2:
        return "sad", scores
    else:
        return "neutral", scores

def detect_emotion_transformer(text):
    result = transformer_analyzer(text)[0]
    label, score = result['label'], result['score']
    if label == "POSITIVE":
        return ("very happy" if score > 0.85 else "happy"), {"compound": score}
    elif label == "NEGATIVE":
        return ("very sad" if score > 0.85 else "sad"), {"compound": -score}
    else:
        return "neutral", {"compound": 0.0}

def detect_multi_emotions(text, threshold=0.25):
    results = multi_emotion_analyzer(text)[0]
    emotions = [(r['label'], r['score']) for r in results if r['score'] > threshold]
    return sorted(emotions, key=lambda x: x[1], reverse=True)

def keyword_boost(text, base_emotion):
    text_lower = text.lower()
    for emotion, words in EMOTION_KEYWORDS.items():
        if any(w in text_lower for w in words):
            return emotion
    return base_emotion
