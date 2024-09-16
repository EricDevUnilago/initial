#Bibliotecas (customtkinter $ pyperclip)

import customtkinter as custom
import random
import pyperclip


custom.set_appearance_mode("dark")
custom.set_default_color_theme("dark-blue")


window = custom.CTk()
window.geometry("800x300")

def generate(size):
    values = []

    if cbx1.get():
        values += alph
    if cbx2.get():
        values += nums
    if cbx3.get():
        values += char

    password = "".join(random.choice(values) for _ in range(size))

    if size < 4:
        color = "#FF6F6F"
    elif size < 6:
        color = "#FFA07A"
    elif size < 8:
        color = "#FFD700"
    elif size < 10:
        color = "#90EE90"
    else:
        color = "#32CD32"

    return password, color

def update_password(value):
    size = int(value)
    new_password, color = generate(size)
    showPassword.configure(text=new_password, text_color=color)
    slider_label.configure(text=f"Tamanho da Senha: {size}")

def copy_password():
    pyperclip.copy(showPassword.cget("text"))

def check_checkboxes():
    checked_count = sum([cbx1.get(), cbx2.get(), cbx3.get()])
    checkboxes = [checkbox1, checkbox2, checkbox3]

    if checked_count == 1:
        for checkbox in checkboxes:
            if checkbox.get():
                checkbox.configure(state=custom.DISABLED)
    elif checked_count == 2:
        for checkbox in checkboxes:
            if checkbox.cget('state') == custom.DISABLED:
                checkbox.configure(state=custom.NORMAL)

    update_password(slider.get())

def increment_slider():
    current_value = slider.get()
    if current_value < slider.cget("to"):
        slider.set(current_value + 1)
        update_password(slider.get())

def decrement_slider():
    current_value = slider.get()
    if current_value > slider.cget("from_"):
        slider.set(current_value - 1)
        update_password(slider.get())


alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
char = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~\\"

cbx1 = custom.BooleanVar(value=True)
cbx2 = custom.BooleanVar(value=True)
cbx3 = custom.BooleanVar(value=True)

size = 15
button_size = 35


title = custom.CTkLabel(window, text="Gerador de Senhas", font=("Arial", 30, "bold"))
showPassword = custom.CTkLabel(window, text="", font=("Arial", 16, "bold"), corner_radius=32)
copyPasswordButton = custom.CTkButton(window, text="Copiar", command=copy_password, fg_color="#0070F6", hover_color="#0040D6", corner_radius=32, width=100, height=40, font=("Arial", 16))


slider_frame = custom.CTkFrame(window, fg_color="transparent")
slider = custom.CTkSlider(slider_frame, from_=1, to=50, progress_color="#0070F6", button_color="#0070F6", button_hover_color="#0040D6", command=update_password)
slider.set(size)
slider_label = custom.CTkLabel(slider_frame, text=f"Tamanho da Senha: {slider.get()}", font=("Arial", 14))
increment_button = custom.CTkButton(slider_frame, text="+", command=increment_slider, border_color="#0070F6", border_width=2, width=button_size, height=button_size, corner_radius=button_size // 2, fg_color="#0070F6")
decrement_button = custom.CTkButton(slider_frame, text="-", command=decrement_slider, border_color="#0070F6", border_width=2, width=button_size, height=button_size, corner_radius=button_size // 2, fg_color="#0070F6")


checkbox_frame = custom.CTkFrame(window, fg_color="transparent")
checkbox1 = custom.CTkCheckBox(checkbox_frame, text="abc", variable=cbx1, command=check_checkboxes, fg_color="#0070D6", corner_radius=20)
checkbox2 = custom.CTkCheckBox(checkbox_frame, text="123", variable=cbx2, command=check_checkboxes, fg_color="#0070D6", corner_radius=20)
checkbox3 = custom.CTkCheckBox(checkbox_frame, text="#$&", variable=cbx3, command=check_checkboxes, fg_color="#0070D6", corner_radius=20)


title.pack(pady=10)
showPassword.pack(pady=15)
copyPasswordButton.pack(pady=5)
slider_frame.pack(pady=10)
slider_label.pack(padx=10)
decrement_button.pack(side="left", padx=5)
slider.pack(side="left", padx=10)
increment_button.pack(side="left", padx=5)
checkbox_frame.pack(pady=5)
checkbox1.pack(side="right")
checkbox2.pack(side="right")
checkbox3.pack(side="right")


initial_password, initial_color = generate(size)
showPassword.configure(text=initial_password, text_color=initial_color)

window.mainloop()
