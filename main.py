from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from PIL import Image
import pytesseract
import time
import customtkinter as ctk 


root = ctk.CTk()
root.geometry("360x480")
root.title("")
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")
root.resizable(False, False)

basedir = os.path.dirname(__file__)
root.iconbitmap(os.path.join(basedir, "log-in (2).ico"))

def webpage(username, password, browser):

    address = __file__.replace("\\","/")
    for i in range(len(address)-1, 0, -1):
        if address[i] == '/':
            address = address[:i]
            break
    os.chdir(address)

    if browser=="Chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get("https://erp.mepcoeng.ac.in/")

    driver.find_element(By.ID, "txt_un").send_keys(username)
    driver.find_element(By.ID, "txt_pw").send_keys(password)

    img = driver.find_element(By.ID, "imgCaptcha")
    img.screenshot(os.path.join(address, 'captcha.png'))

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    cap = pytesseract.image_to_string(Image.open('captcha.png'))

    driver.find_element(By.ID, "txtCaptcha").send_keys(cap)
    
    button = driver.find_element(By.ID, "btn_login")
    button.click()

    time.sleep(20000)

frame1 = ctk.CTkFrame(root, width=360, height=480, fg_color="#594F4F")
frame1.grid(row=0, column=0)

frame = ctk.CTkFrame(frame1, width=320, height=440)
frame.grid(row=0, column=0, padx=20, pady=20)


label2 = ctk.CTkLabel(frame, text="\'Mepco Login\' \n _______", 
    font=ctk.CTkFont("font", size=26, weight="bold"), text_color="#706464")
label2.place(in_=frame, x=75, y=40)

optionmenu = ctk.CTkOptionMenu(frame, values=["FireFox", "Chrome"], width=150, height=30,
    fg_color="#594F4F", button_color="#594F4F", button_hover_color="#474242",
    font=ctk.CTkFont("font", size=18), dropdown_font=ctk.CTkFont("font", size=18))
optionmenu.place(in_=frame, x=95, y=140)

field1 = ctk.CTkEntry(frame, placeholder_text="Username", fg_color="#594F4F",
    width=200, height=36, font=("font", 18))
field1.place(in_=frame, x=65, y=200)

field2 = ctk.CTkEntry(frame, placeholder_text="Password", fg_color="#594F4F",
    width=200, height=36, font=("font", 18), show="*")
field2.place(in_=frame, x=65, y=260)

button = ctk.CTkButton(frame, text="Submit", width=140, height=36, border_width=1, border_color="#808080",
    font=ctk.CTkFont("font", size=20), fg_color="#524848", hover_color="#474242",
    command = lambda:webpage(field1.get(), field2.get(), optionmenu.get()))
button.place(in_=frame, x=95, y=340)

root.mainloop()

