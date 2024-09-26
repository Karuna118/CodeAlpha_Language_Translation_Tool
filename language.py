from googletrans import Translator

# Initialize the translator
translator = Translator()

# Get input from user
text = input("Enter text to translate: ")

# Translate text to a specific language (e.g., 'es' for Spanish)
translated_text = translator.translate(text, dest='es')

# Output the translated text
print(f"Translated text: {translated_text.text}")
