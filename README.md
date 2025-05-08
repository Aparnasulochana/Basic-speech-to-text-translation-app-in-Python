🗣️ Basic Speech-to-Text Translation App in Python

A simple Python-based translator app that uses your voice to recognize speech and translate it into another language. This project leverages the power of the speech_recognition library to convert speech to text and the deep_translator package to handle translations via the Google Translator API.

📌 Features

🎧 Speech Recognition: Converts spoken language into text using your microphone.

🌐 Multilingual Translation: Translates recognized text into your chosen target language using Google Translate.

💃 Voice-Activated Input: Speak both the target language code and the text to translate — no typing needed!

🔧 How It Works

Step 1 - Speak the Language Code

The app prompts you to say a valid language code like:

'es' for Spanish

'fr' for French

'hi' for Hindi

'de' for German(The full list of supported codes can be found in the code.)

Step 2 - Speak the Text to Translate

Once the language code is recognized, the app prompts you to say the sentence you want to translate.

Step 3 - Get the Translation

The app translates your sentence into the specified language using the Google Translator API and prints the result.

💬 Example Interaction

👤 You say: "es"

👤 Then you say: "Hello, how are you?"

📢 The app responds: "Hola, ¿como estas?"
