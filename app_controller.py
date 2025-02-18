import subprocess
import webbrowser

class AppController:
    def open_app(self, app_name):
        apps = {
            "youtube": "https://youtube.com",
            "google": "https://google.com",
            "whatsapp": "https://web.whatsapp.com",
            "gmail": "https://mail.google.com",
            "chatgpt": "https://chatgpt.com/",
            "github": "https://github.com/"
        }
        
        if app_name.lower() in apps:
            webbrowser.open(apps[app_name.lower()])
            return f"Opening {app_name}"
        return "App not supported"

    def open_windows_app(self, app_name):
        app_mappings = {
            "notepad": "notepad",
            "calculator": "calc",
            "word": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk",
            "excel": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk",
            "powerpoint": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk",
            "chrome": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk",
            "vs code": r"C:\Users\Divya\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk",
            "vs": r"C:\Users\Divya\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk",
            "code": r"C:\Users\Divya\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"
        }

        try:
            app_command = app_mappings.get(app_name.lower(), app_name)
            subprocess.Popen([app_command], shell=True)
            return f"Opening {app_name}"
        except Exception as e:
            return f"Failed to open {app_name}: {str(e)}"
            
    def search_google(self, query):
        webbrowser.open(f"https://google.com/search?q={query}")
        return f"Searching Google for {query}"
