# Basic-speech-to-text-translation-app-in-Python
 Building a basic speech-to-text translation app in Python using the speech_recognition library and the deep_translator package for translating speech into another language.
**Speech Recognition:**
The speech_recognition library listens to the microphone and converts spoken words into text.
**Translation:**
The deep_translator library uses the Google Translator API to translate the recognized text into the specified language.
# How It Works:
**Step 1 - Speak the Language Code:**
The user is prompted to speak the language code (e.g., 'es', 'fr') which the program will recognize using speech-to-text.
**Step 2 - Speak the Text to Translate:**
After recognizing the language code, the program will prompt the user to speak the text to be translated.
**Step 3 - Translation:**
The recognized text is then sent to the deep_translator API to translate into the language specified in the first step.

# Example Interaction:
Step 1: You say "es" (for Spanish).
Step 2: Then, you say "Hello, how are you?"
Step 3: The app will translate "Hello, how are you?" into Spanish and print the translated text.
