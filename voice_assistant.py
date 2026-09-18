import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print("FIXORA:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("USER:", text)
        return text.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""


def diagnose(problem):

    if "led" in problem and ("not working" in problem or "not glowing" in problem):
        return "The LED may have a loose connection or may be damaged. Please switch off the power and check the connection."

    elif "bulb" in problem and ("not working" in problem or "not glowing" in problem):
        return "The bulb may be damaged or there may be a power connection problem. Switch off the power before checking it."

    elif "switch" in problem and ("not working" in problem or "not working" in problem):
        return "The switch may have a loose connection or may be faulty. Switch off the power and get the wiring checked safely."

    elif "fan" in problem and ("not working" in problem or "not running" in problem):
        return "The fan may have a power supply or wiring problem. Switch off the power before checking the circuit."

    elif "spark" in problem or "smoke" in problem:
        return "This may be dangerous. Switch off the main power immediately and do not touch the circuit. Contact a qualified electrician."

    else:
        return "I could not identify the exact fault. Please provide more details about the electrical problem."


def main():

    speak("Hello, I am FIXORA. Please describe your electrical problem.")

    while True:

        problem = listen()

        if not problem:
            continue

        if problem in ["exit", "quit", "stop"]:
            speak("Thank you. Goodbye.")
            break

        answer = diagnose(problem)
        speak(answer)


if __name__ == "__main__":
    main()