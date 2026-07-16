from tkinter import *

class Application():
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.geometry("350x550")
        self.window.configure(bg="#3B3B3B")
        self.login()

        self.window.mainloop()

    def login(self):
        self.screen_login = Frame(self.window).pack(anchor="center")

        self.user = Label(self.screen_login, bg="#3B3B3B", text="User", fg="white")
        self.user.place(relwidth=0.1, relheight=0.1, relx=0.45, rely=0.1)

Application()
