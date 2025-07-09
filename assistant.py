import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import time
import threading
import tkinter as tk
from PIL import Image, ImageTk

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1: female, 0: male

# GUI popup for Ani's visual response
class AniPopup:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ani is Listening")
        self.root.geometry("220x170+20+20")
        self.root.configure(bg='white')
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        self.frames = []
        try:
            gif_path = "assets/ani_icon.gif"
            img = Image.open(gif_path)

            while True:
                frame = ImageTk.PhotoImage(img.copy().resize((200, 150)))
                self.frames.append(frame)
                img.seek(len(self.frames))  # Next frame
        except EOFError:
            pass  # End of frames

        self.label = tk.Label(self.root, bg='white')
        self.label.pack()
        self.frame_index = 0
        self.animate()

    def animate(self):
        if self.frames:
            self.label.config(image=self.frames[self.frame_index])
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.root.after(100, self.animate)

    def show(self):
        self.root.after(4000, self.root.destroy)
        self.root.mainloop()

def ani_speak(text):
    print(f"\033[95m✨ Ani:\033[0m {text}")
    engine.say(text)
    engine.runAndWait()

def show_popup():
    popup = AniPopup()
    popup.show()

def listen(timeout=5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        r.energy_threshold = 4000
        try:
            print("\033[93m🔍 Listening...\033[0m")
            audio = r.listen(source, timeout=timeout)
            command = r.recognize_google(audio).lower()
            print(f"\033[94m👤 You:\033[0m {command}")
            return command
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            ani_speak("Sorry, I didn't catch that")
            return ""
        except sr.RequestError:
            ani_speak("Speech service is down")
            return ""

def handle_command(command):
    if 'your name' in command:
        ani_speak("I'm Ani, your personal assistant!")

    elif 'play' in command:
        song = command.replace('play', '').strip()
        ani_speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
        time.sleep(2)

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        ani_speak(f"It's {current_time}")

    elif 'date' in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        ani_speak(f"Today is {current_date}")

    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        try:
            info = wikipedia.summary(person, sentences=2)
            ani_speak(info)
        except:
            ani_speak("I couldn't find info about that")

    elif 'joke' in command:
        ani_speak(pyjokes.get_joke())

    elif 'open' in command:
        if 'chrome' in command:
            ani_speak("Opening Chrome")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'code' in command:
            ani_speak("Launching VS Code")
            os.system("code")

    elif any(word in command for word in ['sleep', 'exit', 'bye']):
        ani_speak("Going to sleep. Say 'Hey Ani' when you need me!")
        return False

    else:
        ani_speak("I didn't understand. Try again!")
    return True

def wake_loop():
    ani_speak("Ani is in testing mode. Speak now.")
    threading.Thread(target=show_popup).start()
    ani_speak("How can I help?")
    active_loop()


def active_loop():
    while True:
        command = listen()
        if not command:
            continue
        if not handle_command(command):
            break

if __name__ == "__main__":
    try:
        wake_loop()
    except KeyboardInterrupt:
        ani_speak("Shutting down... Goodbye!")
        sys.exit()
