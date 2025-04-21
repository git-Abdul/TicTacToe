import os
import customtkinter
from PIL import Image

def centerWindow(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")

counter: int = 1

window = customtkinter.CTk()
window.geometry("300x300")
window.iconbitmap("icon.ico")
window.resizable(False, False)
window.title("")
centerWindow(window)

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

imagePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
window.logoImage = customtkinter.CTkImage(Image.open(os.path.join(imagePath, "logo.png")), size=(35, 35))
window.cross = customtkinter.CTkImage(Image.open(os.path.join(imagePath, "cross.png")), size=(35, 35))
window.circle = customtkinter.CTkImage(Image.open(os.path.join(imagePath, "circle.png")), size=(35, 35))
window.transparent = customtkinter.CTkImage(Image.open(os.path.join(imagePath, "transparent.png")), size=(35, 35))
window.dotPad = customtkinter.CTkImage(Image.open(os.path.join(imagePath, "dotPad.png")), size=(300, 300))

windowFrame = customtkinter.CTkFrame(master=window)
windowFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

gridFrame = customtkinter.CTkFrame(master=windowFrame, fg_color=("#fefefe", "#1f1f1f"), corner_radius=5)
gridFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

for i in range(3):
    gridFrame.grid_rowconfigure(i, weight=1)
    gridFrame.grid_columnconfigure(i, weight=1)
    
def checkWin():
    #ROWS:
    try:
        if(btn1.image == btn2.image == btn3.image):
            btn1.configure(border_color="#f14c4c")
            btn2.configure(border_color="#f14c4c")
            btn3.configure(border_color="#f14c4c")
            if(btn1.image == btn1.symbol):
                print("X won")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
            else:
                print("O won")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
    except AttributeError:
        print("AttributeError")
        
    try:    
        if(btn4.image == btn5.image == btn6.image):
            btn4.configure(border_color="#f14c4c")
            btn5.configure(border_color="#f14c4c")
            btn6.configure(border_color="#f14c4c")
            if(btn4.image == btn4.symbol):
                print("X won.")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
            else:
                print("O won.")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
    except AttributeError:
        print("AttributeError")
    
    try:    
        if(btn7.image == btn8.image == btn9.image):
            btn7.configure(border_color="#f14c4c")
            btn8.configure(border_color="#f14c4c")
            btn9.configure(border_color="#f14c4c")
            if(btn7.image == btn7.symbol):
                print("X won.")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
            else:
                print("O won.")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
    except AttributeError:
        print("AttributeError")
    
    #COLUMNS:
    try:
        if(btn1.image == btn4.image == btn7.image):
            btn1.configure(border_color="#f14c4c")
            btn4.configure(border_color="#f14c4c")
            btn7.configure(border_color="#f14c4c")
            if(btn1.image == btn1.symbol):
                print("X won.")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
            else:
                print("O won.")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
    except AttributeError:
        print("AttributeError")
    
    try:
        if(btn2.image == btn5.image == btn8.image):
            btn2.configure(border_color="#f14c4c")
            btn5.configure(border_color="#f14c4c")
            btn8.configure(border_color="#f14c4c")
            if(btn5.image == btn4.symbol):
                print("X won.")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
            else:
                print("O won.")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
    except AttributeError:
        print("AttributeError")
        
    try:
        if(btn3.image == btn6.image == btn9.image):
            btn3.configure(border_color="#f14c4c")
            btn6.configure(border_color="#f14c4c")
            btn9.configure(border_color="#f14c4c")
            if(btn6.image == btn7.symbol):
                print("X won.")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
            else:
                print("O won.")
                for widget in gridFrame.winfo_children():
                    widget.configure(state="disabled")
    except AttributeError:
        print("AttributeError")
      
    #DIAGONALS  
    try:
        if(btn1.image == btn5.image == btn9.image):
            btn1.configure(border_color="#f14c4c")
            btn5.configure(border_color="#f14c4c")
            btn9.configure(border_color="#f14c4c")

            if(btn5.image == btn1.symbol):
                print("X won.")
            else:
                print("O won.")
            
            for widget in gridFrame.winfo_children():
                widget.configure(state="disabled")
    except AttributeError:
        print("AttributeError")

    # Diagonal 2 → Top-right to Bottom-left
    try:
        if(btn3.image == btn5.image == btn7.image):
            btn3.configure(border_color="#f14c4c")
            btn5.configure(border_color="#f14c4c")
            btn7.configure(border_color="#f14c4c")

            if(btn5.image == btn1.symbol):  # Can also compare to btn3.symbol
                print("X won.")
            else:
                print("O won.")
            
            for widget in gridFrame.winfo_children():
                widget.configure(state="disabled")
    except AttributeError:
        print("AttributeError")

def btnClick(btn):
    global counter
    if counter % 2 == 0:
        btn.configure(image=window.cross, state="disabled")
        btn.image = "cross"
    else:
        btn.configure(image=window.circle, state="disabled")
        btn.image = "circle"
    
    btn.symbol = "cross"
    counter += 1
    checkWin()

btn1 = customtkinter.CTkButton(gridFrame, image=window.transparent, text="", fg_color=("#fefefe", "#2b2b2b"), hover_color=("#9c9c9c", "#181818"), border_color="#2cc985", border_width=3, compound="left", command=lambda: btnClick(btn1), width=45, height=45)
btn2 = customtkinter.CTkButton(gridFrame, image=window.transparent, text="", fg_color=("#fefefe", "#2b2b2b"), hover_color=("#9c9c9c", "#181818"), border_color="#2cc985", border_width=3, compound="left", command=lambda: btnClick(btn2), width=45, height=45)
btn3 = customtkinter.CTkButton(gridFrame, image=window.transparent, text="", fg_color=("#fefefe", "#2b2b2b"), hover_color=("#9c9c9c", "#181818"), border_color="#2cc985", border_width=3, compound="left", command=lambda: btnClick(btn3), width=45, height=45)
btn4 = customtkinter.CTkButton(gridFrame, image=window.transparent, text="", fg_color=("#fefefe", "#2b2b2b"), hover_color=("#9c9c9c", "#181818"), border_color="#2cc985", border_width=3, compound="left", command=lambda: btnClick(btn4), width=45, height=45)
btn5 = customtkinter.CTkButton(gridFrame, image=window.transparent, text="", fg_color=("#fefefe", "#2b2b2b"), hover_color=("#9c9c9c", "#181818"), border_color="#2cc985", border_width=3, compound="left", command=lambda: btnClick(btn5), width=45, height=45)
btn6 = customtkinter.CTkButton(gridFrame, image=window.transparent, text="", fg_color=("#fefefe", "#2b2b2b"), hover_color=("#9c9c9c", "#181818"), border_color="#2cc985", border_width=3, compound="left", command=lambda: btnClick(btn6), width=45, height=45)
btn7 = customtkinter.CTkButton(gridFrame, image=window.transparent, text="", fg_color=("#fefefe", "#2b2b2b"), hover_color=("#9c9c9c", "#181818"), border_color="#2cc985", border_width=3, compound="left", command=lambda: btnClick(btn7), width=45, height=45)
btn8 = customtkinter.CTkButton(gridFrame, image=window.transparent, text="", fg_color=("#fefefe", "#2b2b2b"), hover_color=("#9c9c9c", "#181818"), border_color="#2cc985", border_width=3, compound="left", command=lambda: btnClick(btn8), width=45, height=45)
btn9 = customtkinter.CTkButton(gridFrame, image=window.transparent, text="", fg_color=("#fefefe", "#2b2b2b"), hover_color=("#9c9c9c", "#181818"), border_color="#2cc985", border_width=3, compound="left", command=lambda: btnClick(btn9), width=45, height=45)

btn1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
btn2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
btn3.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
btn4.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
btn5.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
btn6.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
btn7.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
btn8.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
btn9.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

window.mainloop()
