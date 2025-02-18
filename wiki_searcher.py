import wikipedia

class WikiSearcher:
    def __init__(self):
        wikipedia.set_lang("en")

    def search_wikipedia(self, query):
        try:
            summary = wikipedia.summary(query, sentences=2)
            return f"According to Wikipedia:\n{summary}"
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Sorry, the query is too ambiguous. Here are some options:\n{e.options}"
        except wikipedia.exceptions.HTTPTimeoutError:
            return "Sorry, the request timed out. Please try again later."
        except wikipedia.exceptions.RedirectError:
            return "Sorry, there was a redirect on the Wikipedia page."
        except wikipedia.exceptions.PageError:
            return "Sorry, I couldn't find any information on that."
        except Exception as e:
            return f"Server is busy..."