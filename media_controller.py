import webbrowser

class MediaController:
    def play_music(self, query):
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"Playing {query} on YouTube"
