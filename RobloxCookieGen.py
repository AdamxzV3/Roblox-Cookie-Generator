from tkinter import *
from random import randint
import customtkinter
def GenerateCookie():
    randomNum = randint(10000000, 99999999)
    randomStr = ''.join(chr(randint(65, 90)) for _ in range(802))
    cookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + str(randomNum) + randomStr
    cookieTextBox.delete(1.0, END)  # Clear the current text
    cookieTextBox.insert(END, cookie)

    with open("cookie.txt", "w") as file:
        file.write(cookie)

root = Tk()
cookieTextBox = Text()
cookieTextBox.pack()

GenerateCooki3 = customtkinter.CTkButton(root, text="Generate Cookie", command=GenerateCookie)
GenerateCooki3.pack()

GenerateShit = customtkinter.CTkLabel(root, text="JOIN : https://discord.gg/Q2Vx75J4")
GenerateShit.pack()

root.title("CodePulse Cookie Generator PAID ")
root.configure(bg="#292929")
root.geometry("800x450")

root.mainloop()
