from assistant import JarvisAssistant
from login import start_login

def main():
    jarvis = JarvisAssistant()
    greeting = jarvis.greet()
    print(greeting)
    jarvis.speak(greeting)
    
    while True:
        jarvis.speak("How can I assist you?")
        user_input = jarvis.listen()
        
        if not user_input:
            continue
            
        if any(word in user_input for word in ["exit", "bye", "goodbye"]):
            farewell = "Goodbye sir!"
            print(farewell)
            jarvis.speak(farewell)
            break

        response = ""
        try:
            response = jarvis.route_command(user_input)
            print(f"\nJarvis: {response}")
            jarvis.speak(response)

        except Exception as e:
            error_msg = f"Sorry sir, I encountered an error: {str(e)}"
            print(error_msg)
            jarvis.speak(error_msg)

if __name__ == "__main__":
    if start_login():
        main()  
    else:
        print("Login failed or cancelled. Exiting.")
