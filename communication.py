import smtplib
import pywhatkit
import os
from dotenv import load_dotenv
from mtranslate import translate

load_dotenv()

class Communication:
    def __init__(self):
        self.EMAIL = os.getenv("EMAIL")
        self.PASSWORD = os.getenv("EMAIL_PASSWORD")
        self.SMTP_SERVER = "smtp.gmail.com"
        self.SMTP_PORT = 587

    def send_whatsapp(self, number, message, time_hour, time_min):
        try:
            pywhatkit.sendwhatmsg(number, message, time_hour, time_min)
            return f"Message scheduled for {time_hour}:{time_min}"
        except Exception as e:
            return f"Error scheduling WhatsApp message: {str(e)}"

    def send_email(self, to, subject, body):
        try:
            server = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
            server.starttls()
            server.login(self.EMAIL, self.PASSWORD)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(self.EMAIL, to, message)
            server.quit()
            return "Email sent successfully"
        except Exception as e:
            return f"Error sending email: {str(e)}"

    def translate_to_hindi(self, text):
        hindi_translation = translate(text, 'hi', 'en')
        return hindi_translation