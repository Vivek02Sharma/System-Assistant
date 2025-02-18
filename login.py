import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import hashlib
import os

class LoginSystem:
    def __init__(self, app):
        self.app = app
        self.cred_file = "user_credentials.txt"
        self.login_successful = False  # Start with login as False
        self.create_widgets()
        
    def create_widgets(self):
        self.frame = ctk.CTkFrame(master=self.app)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text="Modern Login System UI")
        self.label.pack(pady=12, padx=10)

        self.username_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=12, padx=10)

        self.password_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=12, padx=10)

        self.login_button = ctk.CTkButton(master=self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=12, padx=10)

        self.register_button = ctk.CTkButton(master=self.frame, text="Register", command=self.register)
        self.register_button.pack(pady=12, padx=10)

        self.checkbox = ctk.CTkCheckBox(master=self.frame, text="Remember Me")
        self.checkbox.pack(pady=12, padx=10)
        
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def validate_credentials(self, username, password):
        if not os.path.exists(self.cred_file):
            return False
        with open(self.cred_file, "r") as f:
            for line in f:
                stored_user, stored_pass = line.strip().split(":")
                if stored_user == username and stored_pass == self.hash_password(password):
                    return True
        return False
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            tkmb.showerror("Error", "Please fill all fields")
            return
        
        if self.validate_credentials(username, password):
            tkmb.showinfo("Login Successful", "You have logged in Successfully")
            self.login_successful = True
            self.app.destroy()  # Close the window if login is successful
        else:
            tkmb.showerror("Error", "Invalid credentials")
    
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            tkmb.showerror("Error", "Please fill all fields")
            return
            
        if os.path.exists(self.cred_file):
            with open(self.cred_file, "r") as f:
                for line in f:
                    if line.startswith(username + ":"):
                        tkmb.showerror("Error", "Username already exists")
                        return
                        
        with open(self.cred_file, "a") as f:
            f.write(f"{username}:{self.hash_password(password)}\n")
            tkmb.showinfo("Success", "Registration successful")

    def close_window(self):
        self.login_successful = False
        self.app.quit()

def start_login():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("400x400")
    app.title("JARVIS Login System")
    login_system = LoginSystem(app)

    app.protocol("WM_DELETE_WINDOW", login_system.close_window)
    app.mainloop()  
    
    return login_system.login_successful  
