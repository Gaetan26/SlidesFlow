
import customtkinter as ctk
from PIL import Image
from threading import Thread

from utils import get_ip
from mqtt import run, vibrate_devices

running = True
def on_window_closing():
    global running
    running = False
    window.destroy()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

window = ctk.CTk()
window.title("Slide Flow")
window.geometry("300x250")
window.resizable(width=0, height=0)
#

window.columnconfigure(0, weight=1)
window.rowconfigure([0,1,2], weight=1)

image = Image.open("img/joystick.png")
image = ctk.CTkImage(dark_image=image, size=(100,100))

image_label = ctk.CTkLabel(window, text="", image=image)
image_label.grid(row=0, column=0, pady=(5, 0))

ip = get_ip()

ip_label = ctk.CTkLabel(window, text=ip, font=("JetBrains Mono", 20))
ip_label.grid(row=1, column=0)

vibrate_button = ctk.CTkButton(window, text="Vibrate Devices", font=("JetBrains Mono", 15), corner_radius=64, command=vibrate_devices)
vibrate_button.grid(row=2, column=0, sticky="we", padx=20, ipady=6, pady=(0, 20))

Thread(target=run).start()

#
window.protocol("WM_DELETE_WINDOW", on_window_closing)
window.mainloop()