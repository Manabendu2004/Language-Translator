A simple Language Translator GUI built in Python. It uses the Google Translator engine via the translators library to translate text between languages.

🚀 Features:

Translate text between multiple languages

Uses Google Translate in the backend

No dataset required

Simple function-based implementation (Translate())

🛠️ Technologies Used:

Python 3

translators library (pip install translators)

(Optional) tkinter for GUI

📌 Installation:

Clone the repository:

git clone https://github.com/your-username/language-translator.git
cd language-translator


Install dependencies:

pip install translators


If using GUI:

pip install tk

▶️ Usage:
import translators as ts  

def Translate():
    translat = ts.translate_text(
        "Hello, how are you?",
        translator="google",
        from_language="en",
        to_language="fr"
    )
    print(translat)  # Bonjour, comment ça va ?

Translate()


For GUI (with tkinter):

def Translate():
   translat = ts.translate_text(
       TextVar.get(),
       translator="google",
       from_language=InputLanguage.get()[:2],
       to_language=TranslatedLanguage.get()[:2]
   )
   OutputVar.set(translat)
