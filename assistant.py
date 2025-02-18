import pyttsx3
import speech_recognition as sr
from datetime import datetime , timedelta
from task_manager import TaskManager
from media_controller import MediaController
from app_controller import AppController
from communication import Communication
from wiki_searcher import WikiSearcher
from ai_helper import AIHelper

class JarvisAssistant:
    def __init__(self):
        self.chat_history = []
        self.todo_manager = TaskManager()
        self.media_controller = MediaController()
        self.app_controller = AppController()
        self.communication = Communication()
        self.wiki_searcher = WikiSearcher()
        self.ai_helper = AIHelper()
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

        # Configure voice engine
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 180)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("\nListening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=7)

            try:
                print("Recognizing...")
                query = self.recognizer.recognize_google(audio, language='en-in')
                print(f"User: {query}")
                return query.lower()
            except sr.UnknownValueError:
                self.speak("Sorry sir, I didn't catch that. Could you repeat?")
                return ""
            except Exception as e:
                self.speak("There was an error with the microphone. Please check your audio settings.")
                return ""

    def greet(self):
        hour = datetime.now().hour
        if 5 <= hour < 12:
            return "Good morning sir!"
        elif 12 <= hour < 18:
            return "Good afternoon sir!"
        else:
            return "Good evening sir!"

    def get_time(self):
        return datetime.now().strftime("%I:%M %p")

    def get_date(self):
        return datetime.now().strftime("%A, %B %d, %Y")

    def route_command(self, user_input):
        response = ""
        if "time" in user_input:
            response = self.get_time()
        elif "date" in user_input:
            response = self.get_date()
        elif "play" in user_input or "music" in user_input:
            query = user_input.replace("play", "").replace("music", "").strip()
            response = self.media_controller.play_music(query)
        elif "add task" in user_input:
            task = user_input.split("add task")[1].strip()
            response = self.todo_manager.add_todo(task)
        elif "read tasks" in user_input or "read to do" in user_input:
            response = self.todo_manager.read_todo()
        elif "clear tasks" in user_input or "clear" in user_input:
            response = self.todo_manager.clear_todo()
        elif "open" in user_input:
            app = user_input.split("open")[1].strip()
            response = self.app_controller.open_app(app)
            if "not supported" in response.lower():
                response = self.app_controller.open_windows_app(app)
        elif "wikipedia" in user_input:
            query = user_input.split("wikipedia")[1].strip()
            response = self.wiki_searcher.search_wikipedia(query)
        elif "search" in user_input:
            query = user_input.split("search")[1].strip()
            response = self.app_controller.search_google(query)
        elif "send email" in user_input:
            print("\nEmail Details:")
            to = input("Recipient email: ")
            subject = input("Subject: ")
            body = input("Message: ")
            response = self.communication.send_email(to, subject, body)
        elif "whatsapp" in user_input:
            print("\nWhatsApp Details:")
            number = input("Phone number with country code: ")
            message = input("Message: ")
            current_time = datetime.now()
            future_time = current_time + timedelta(minutes=1)
            time_hour = future_time.hour
            time_min = future_time.minute
            print("Hour : ",time_hour)
            print("Minute : ",time_min)
            response = self.communication.send_whatsapp(number, message, time_hour, time_min)
        elif "translate" in user_input:
            query = user_input.split("translate")[1].strip()
            response = self.communication.translate_to_hindi(query)
        else:
            response = self.ai_helper.ask_ai(user_input)

        return response
