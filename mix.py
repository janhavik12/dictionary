import spacy
import speech_recognition as sr
import requests
from translate import Translator

nlp = spacy.load('en_core_web_sm')

# Your dictionary and search_word function remain unchanged

# Replace 'YOUR_API_KEY' with your actual API key from Merriam-Webster
API_KEY = '6969e035-fe34-42a8-9ade-eb7a194bc1f9'
BASE_URL = 'https://dictionaryapi.com/api/v3/references/learners/json/'


dictionary = {
    'love': {
        'english': 'A strong affection or deep feeling of affection',
        'hindi': 'प्यार (Pyar)',
        'marathi': 'प्रेम (Prem)',
        'sanskrit': 'प्रेम (Prema)'
    },
    'home': {
        'english': 'A place where one lives or feels comfortable',
        'hindi': 'घर (Ghar)',
        'marathi': 'घर (Ghar)',
        'sanskrit': 'गृह (Griha)'
    },
    'water': {
        'english': 'A transparent, tasteless, and odorless liquid',
        'hindi': 'पानी (Pani)',
        'marathi': 'पाणी (Pani)',
        'sanskrit': 'जल (Jala)'
    },
    'knowledge': {
        'english': 'Information, understanding, or skills gained through experience',
        'hindi': 'ज्ञान (Gyaan)',
        'marathi': 'ज्ञान (Gyaan)',
        'sanskrit': 'ज्ञान (Jnana)'
    },
    'happiness': {
        'english': 'A state of well-being and contentment',
        'hindi': 'ख़ुशी (Khushi)',
        'marathi': 'सुख (Sukh)',
        'sanskrit': 'सुख (Sukha)'
    },
    'sun': {
        'english': 'The star at the center of our solar system',
        'hindi': 'सूरज (Suraj)',
        'marathi': 'सूर्य (Surya)',
        'sanskrit': 'सूर्य (Surya)'
    },
    'moon': {
        'english': 'The natural satellite of the Earth',
        'hindi': 'चांद (Chand)',
        'marathi': 'चंद्र (Chandra)',
        'sanskrit': 'चंद्र (Chandra)'
    },
    'friend': {
        'english': 'A person you enjoy being with and trust',
        'hindi': 'दोस्त (Dost)',
        'marathi': 'मित्र (Mitra)',
        'sanskrit': 'मित्र (Mitram)'
    },
    'peace': {
        'english': 'A state of tranquility and freedom from conflict',
        'hindi': 'शांति (Shanti)',
        'marathi': 'शांतता (Shantata)',
        'sanskrit': 'शान्ति (Shanti)'
    },
    'mother': {
        'english': 'A female parent',
        'hindi': 'माँ (Maa)',
        'marathi': 'आई (Aai)',
        'sanskrit': 'मातृ (Matr)'
    },
    'father': {
        'english': 'A male parent',
        'hindi': 'पिता (Pita)',
        'marathi': 'वडील (Vadil)',
        'sanskrit': 'पितृ (Pitr)'
    },

    'food': {
        'english': 'Any nutritious substance consumed for nourishment',
        'hindi': 'भोजन (Bhojan)',
        'marathi': 'जेवण (Jevan)',
        'sanskrit': 'आहार (Aahar)'
    },
    'courage': {
        'english': 'The ability to face difficulties without fear',
        'hindi': 'साहस (Sahas)',
        'marathi': 'साहस (Sahas)',
        'sanskrit': 'सौहार्द (Sauharda)'
    },
    'dream': {
        'english': 'A series of thoughts and images experienced during sleep',
        'hindi': 'सपना (Sapna)',
        'marathi': 'स्वप्न (Swapna)',
        'sanskrit': 'स्वप्न (Swapna)'
    },
    'rain': {
        'english': 'Water falling from the sky in drops',
        'hindi': 'बारिश (Barish)',
        'marathi': 'पाऊस (Paus)',
        'sanskrit': 'वर्षा (Varsha)'
    },
    'freedom': {
        'english': 'The power or right to act, speak, or think as one wants',
        'hindi': 'स्वतंत्रता (Swatantrata)',
        'marathi': 'स्वातंत्र्य (Swatantrya)',
        'sanskrit': 'स्वतंत्रता (Swatantrata)'
    },
    'book': {
        'english': 'A written or printed work consisting of pages',
        'hindi': 'किताब (Kitab)',
        'marathi': 'पुस्तक (Pustak)',
        'sanskrit': 'पुस्तकम् (Pustakam)'
    },
   'flower': {
        'english': 'The reproductive structure of flowering plants',
        'hindi': 'फूल (Phool)',
        'marathi': 'फूल (Phool)',
        'sanskrit': 'पुष्प (Pushpa)'
    },
   'time': {
        'english': 'The indefinite continued progress of existence',
        'hindi': 'समय (Samay)',
        'marathi': 'वेळ (Vel)',
        'sanskrit': 'काल (Kala)'
    },
   'hope': {
        'english': 'A feeling of expectation and desire for a certain thing to happen',
        'hindi': 'आशा (Asha)',
        'marathi': 'आशा (Asha)',
        'sanskrit': 'आशा (Ashā)'
    },
    'kindness': {
        'english': 'The quality of being friendly, generous, and considerate',
        'hindi': 'दया (Daya)',
        'marathi': 'करुणा (Karuna)',
        'sanskrit': 'कृपा (Kripā)'
    },


    # Add more words and their meanings in different languages
}


def search_word(word):
    search_tokens = [token.lemma_.lower() for token in nlp(word)]

    found_words = []
    for dict_word in dictionary:
        dict_word_tokens = [token.lemma_.lower() for token in nlp(dict_word)]
        if all(token in dict_word_tokens for token in search_tokens):
            found_words.append(dict_word)

    if found_words:
        results = []
        for found_word in found_words:
            meanings = dictionary[found_word]
            result = (
                "Word: " + found_word + "\n" +
                "English: " + meanings['english'] + "\n" +
                "Hindi: " + meanings['hindi'] + "\n" +
                "Marathi: " + meanings['marathi'] + "\n" +
                "Sanskrit: " + meanings['sanskrit'] + "\n"
            )
            results.append(result)
        return results
    else:
        result = "Word not found in dictionary"
        return result


# Language code mapping

def text_input():
    while True:
        user_input = input("Enter a word (or type 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            break

        result = search_word(user_input)
        print(result)

def voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

        try:
            recognized_text = recognizer.recognize_google(audio)
            print("You said:", recognized_text)

            # Make the API request to Merriam-Webster
            url = BASE_URL + recognized_text.lower() + '?key=' + API_KEY
            response = requests.get(url)

            if response.status_code == 200:
                meanings = response.json()
                if isinstance(meanings, list) and len(meanings) > 0:
                    # If the API returns a list of meanings, get the first one
                    english_meaning = meanings[0].get('shortdef', [''])[0]
                    print("English Meaning of '{}': {}".format(recognized_text, english_meaning))

                    # Translate the English meaning into other languages
                    for language, code in language_codes.items():
                        if code != 'en':
                            translator = Translator(from_lang='en', to_lang=code)
                            translated_meaning = translator.translate(english_meaning)
                            print("{} Meaning: {}".format(language, translated_meaning))

                else:
                    print("No meaning found for '{}'".format(recognized_text))
            else:
                print("Error while fetching the meaning. Status Code:", response.status_code)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except Exception as e:
            print("not found:", e)
# Prompt user to choose text or voice input
while True:
    user_choice = input("Enter 'T' for text input or 'V' for voice input (or 'exit' to quit): ").strip().lower()

    if user_choice == 'exit':
        break
    elif user_choice == 't':
        text_input()
    elif user_choice == 'v':
        voice_input()
    else:
        print("Invalid input. Please enter 'T', 'V', or 'exit'.")
