import speech_recognition as sr
from deep_translator import GoogleTranslator

def recognize_and_translate():
    # Initialize recognizer
    r = sr.Recognizer()

    # Prompt user to input the language code (speech recognition)
    with sr.Microphone() as source:
        print("Say the language code (e.g., 'es' for Spanish, 'fr' for French)...")
        audio = r.listen(source)

    try:
        # Recognize the language code
        language_code = r.recognize_google(audio).lower()
        print(f"Language code recognized: {language_code}")

        # Ensure that the recognized language code is valid
        valid_codes = ['es', 'fr', 'de', 'it', 'ja', 'hi', 'en', 'pt']
        if language_code not in valid_codes:
            print("Invalid language code. Please say a valid code (e.g., 'es' for Spanish).")
            return

        # Now, listen for the text to translate
        with sr.Microphone() as source:
            print("Now, say the text to translate...")
            audio = r.listen(source)

        # Recognize the speech to text
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        # Translate the text to the specified language
        translated = GoogleTranslator(source='auto', target=language_code).translate(text)
        print(f"Translated ({language_code}): {translated}")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error with speech recognition service: {e}")
    except Exception as e:
        print(f"Translation error: {e}")

# Run the function
recognize_and_translate()
