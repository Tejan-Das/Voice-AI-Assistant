import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import os
import wikipedia
import requests
import pywhatkit
import pyautogui



def speak(text):
    print("Assistant:", text)

    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 200)

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text

    except Exception as e:
        print(e)
        return ""


speak("Assistant is ready")

while True:
    text = listen()

    if text == "":
        continue

    text_lower = text.lower()

    if "bye" in text_lower:
        speak("Goodbye")
        break
    
    elif "hello" in text_lower:
        speak("Hi,How can i help you")

    elif "jarvis" in text_lower:
        speak("Yes Boss")

    elif "how r u" in text_lower:
        speak("I'm fine ,what about you")
    
    elif "made you" in text_lower:
        speak("I was created by Tejan")

    elif "hu r u" in text_lower:
        speak("I'm your assistant")
    
    elif "thanks" in text_lower:
        speak("No thanks, it's my pleasure!")
    
    elif "thank u" in text_lower:
        speak("No problem!")

    elif "can you do" in text_lower:
        speak("I can help with daily tasks, music, time, weather and questions.")

    elif "time" in text_lower:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + current_time)

    elif "date" in text_lower:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    elif "open" in text_lower:
        site = text_lower.replace("open", "").strip()

        if site:
            speak("Opening " + site)
            webbrowser.open(f"https://www.{site}.com")

    elif "search" in text_lower:
        query = text_lower.replace("search", "").strip()
        speak("Searching Google for " + query)

        webbrowser.open(
        "https://www.google.com/search?q="
        + query.replace(" ", "+")
    )

    elif "play song" in text_lower:
        song = text_lower.replace("play song", "").strip()

        if song:
            speak("Playing " + song)
            pywhatkit.playonyt(song)
        else:
            speak("Please tell me the song name")

    elif "pause" in text_lower:
        speak("Pausing")
        pyautogui.press("space")

    elif "resume" in text_lower:
        speak("Resuming")
        pyautogui.press("space")

    elif "mute" in text_lower:
        speak("Muting")
        pyautogui.press("m")             

    elif "full screen" in text_lower:
        speak("Full screen")
        pyautogui.press("f")  

    elif "joke" in text_lower:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "notepad" in text_lower:
        speak("Opening Notepad")
        os.system("notepad")

    elif "calculator" in text_lower:
        speak("Opening Calculator")
        os.system("calc")
    
    elif "weather in" in text_lower:
        city = text_lower.replace("weather in", "").strip()

        if city:
            speak("Checking weather in " + city)

            try:
                response = requests.get(
                f"https://wttr.in/{city}?format=Temperature:%20%t,%20Feels%20like:%20%f,%20Humidity:%20%h,%20Wind:%20%w"
            )

                weather = response.text
                print(weather)
                speak(weather)

            except:
                speak("Unable to get weather right now")

        else:
         speak("Please tell me the city name")

    elif "who is" in text_lower or "what is" in text_lower or "where is" in text_lower or "what are" in text_lower:

        query = text_lower.replace("who is", "")
        query = query.replace("what is", "")
        query = query.replace("where is", "")
        query = query.replace("what are","")
        query = query.strip()

        try:
            speak("Searching Wikipedia for " + query)

            wikipedia.set_lang("en")
            info = wikipedia.summary(query, sentences=2)

            print(info)
            speak(info)

        except wikipedia.exceptions.DisambiguationError:
            speak("Multiple results found. Please be more specific.")

        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find that.")

        except requests.exceptions.JSONDecodeError:
            speak("Wikipedia is not responding right now.")

        except Exception as e:
            print(e)
            speak("Some error occurred.")
    

    else:
        speak(text)
 

