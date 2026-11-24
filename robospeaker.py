# import os
# print("Welcome to Robo-Speaker 1.1 created by Dolly")
# x=input("Enter what do you want me to speak ")
# command =f"say {x}"
# os.system(command)
# # these function can run automatically commands
import pyttsx3

def speak(text: str) -> None:
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("Welcome to Robo‑Speaker 1.1 (created by Dolly)")
    while True:
        msg = input("Enter what you want me to speak: ")
        if msg=='q':
            speak("bye bye friend")
            break
        speak(msg)
