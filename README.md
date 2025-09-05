# Darwix-Winner (DEMO LINK: https://darwix-ai.streamlit.app/)
Text to Emotional Language


Got it 👍
Here’s your full **README.md** file content right here (you can just copy-paste into a file named `README.md` inside your project):

---

# 🎭 Empathy Engine

A Streamlit-based application for **multilingual emotion detection and expressive speech synthesis**.
It can analyze emotions in text (English, Hindi, and more), show emotion intensity, and convert text to expressive audio using Google Cloud Text-to-Speech.

---

## ✨ Features

1. **Emotion Detection**

   * Uses **VADER Sentiment Analyzer** (rule-based) for quick polarity detection.
   * Uses **Hugging Face Transformers** (pre-trained model) for advanced multilingual emotion classification.
   * Supports **multiple emotions at the same time**, showing percentages for each.

2. **Multilingual Support**

   * Works for English, Hindi, and other major languages supported by the Hugging Face model.
   * Example: `"मैं बहुत खुश हूँ"` → correctly detected as **happy**.

3. **Text-to-Speech (TTS)**

   * Uses **Google Cloud Text-to-Speech API**.
   * Adjustable **rate (speed)**, **pitch**, and **volume**.
   * Generates natural-sounding audio that matches detected emotions.

4. **Interactive UI (Streamlit)**

   * Clean layout with a **background image**.
   * Upload your own `background.jpg` to customize.
   * Choose single or multiple emotion detection modes.

---

## 📂 Project Structure

```
empathy_engine/
│── app.py                # Main Streamlit application
│── requirements.txt      # Python dependencies
│── README.md             # Documentation
│── background.jpg        # Background image (replace with your own)
```

---

## ⚙️ Installation

1. **Clone / Extract Project**

   ```bash
   unzip empathy_engine.zip
   cd empathy_engine
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Cloud TTS API Key**

   * Go to [Google Cloud Console](https://console.cloud.google.com/).
   * Enable **Text-to-Speech API**.
   * Create an **API Key** (no JSON needed).
   * Replace the placeholder `API_KEY` in `app.py` with your actual key:

     ```python
     API_KEY = "YOUR_GOOGLE_CLOUD_TTS_API_KEY"
     ```

---

## 🚀 Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

---

## 🎤 Example Workflow

1. Enter text: `"I am very excited today!"`
2. Select **Multiple Emotions** → You’ll see:

   * Happy: 70%
   * Excited: 20%
   * Neutral: 10%
3. Adjust **Speed = 0.9, Pitch = +2, Volume = 1.0**.
4. Click **Generate Audio** → Hear expressive speech output.

---

## 📊 Tech Stack

* **Streamlit** → UI
* **VADER** → Basic sentiment analysis
* **Hugging Face Transformers** → Emotion detection model
* **Google Cloud TTS API** → Expressive speech synthesis
* **Base64 / Tempfile** → Audio file handling

---

## 🛠️ Customization

* Replace `background.jpg` with your own wallpaper.
* Add more languages by loading multilingual Hugging Face models.
* Tweak emotion-to-voice mapping to better reflect emotions in TTS.

---

✅ With this app, you can turn text into **emotion-aware speech** in multiple languages!

---

Do you also want me to expand the README with a **detailed explanation of each code section in `app.py` line-by-line** so anyone can understand the full workflow?
