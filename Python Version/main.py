import os
import threading
import subprocess
import customtkinter
from PIL import Image

def centerWindow(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")
    
def openClassic():
    def Classic():
        subprocess.run(["python", "classic.py"])
    thread = threading.Thread(target=Classic)
    thread.start()
    
def openBot():
    def Bot():
        subprocess.run(["python", "bot.py"])
    thread = threading.Thread(target=Bot)
    thread.start()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.geometry("500x310")
window.title("")
window.resizable(False, False)
window.iconbitmap("icon.ico")

imagePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
window.logoImage = customtkinter.CTkImage(Image.open(os.path.join(imagePath, "logo.png")), size=(120, 120))

logoLabel = customtkinter.CTkLabel(window, text="", image=window.logoImage)
logoLabel.grid(column=1, row=0, columnspan=10, padx=190, pady=40)

btn1 = customtkinter.CTkButton(window, text="Classic", text_color="#181818", command=openClassic, height=40)
btn1.grid(row=1, column=1, padx=55, pady=30)

btn2 = customtkinter.CTkButton(window, text="Vs Bot", text_color="#181818", command=openBot, height=40)
btn2.grid(row=1, column=2, padx=60, pady=30)

centerWindow(window)
window.mainloop()