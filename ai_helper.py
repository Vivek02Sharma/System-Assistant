from groq import Groq
import os

class AIHelper:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.chat_history = []

    def ask_ai(self, prompt):
        self.chat_history.append({"role": "user", "content": prompt})
        
        completion = self.client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {
                    "role": "system",
                    "content": """You are JARVIS, an advanced AI assistant. 
                    Respond formally but helpfully. Be concise. Also understand the user context."""
                },
                *self.chat_history
            ],
            temperature=0.5,
            max_tokens=1024,
        )
        
        response = completion.choices[0].message.content
        self.chat_history.append({"role": "assistant", "content": response})
        return response
