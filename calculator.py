from tkinter import *

class Application():
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.geometry("350x550")
        self.window.minsize(width=350, height=550)
        self.FUNDO = "#3B3B3B"
        self.window.configure(bg=self.FUNDO)
        self.screen_login()

        self.window.mainloop()

    def screen_login(self):
        self.scr_login = Frame(self.window, bg=self.FUNDO).pack(fill="both", expand=True)

        self.lb_login = Label(self.scr_login, bg=self.FUNDO, text="LOGIN", fg="white", font=("Arial", 25))
        self.lb_login.place(relx=0.5, rely=0.05, anchor="center")

        self.lb_user = Label(self.scr_login, bg=self.FUNDO, text="User", fg="white")
        self.lb_user.place(relx=0.5, rely=0.1, anchor="center")

        self.et_user = Entry(self.scr_login)
        self.et_user.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.12)

        self.lb_password = Label(self.scr_login, bg=self.FUNDO, text="Password", fg="white")
        self.lb_password.place(relx=0.5, rely=0.25, anchor="center")

        self.et_password = Entry(self.scr_login)
        self.et_password.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.27)

Application()
