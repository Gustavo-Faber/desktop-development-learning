from tkinter import *

class Feats():
    def feat_btlogin(self):
        self.user = 

class Application(Feats):
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

        self.lb_login = Label(self.scr_login, bg=self.FUNDO, text="Login", fg="white", font=("Arial", 25))
        self.lb_login.place(relx=0.5, rely=0.2, anchor="center")

        self.lb_user = Label(self.scr_login, bg=self.FUNDO, text="User", fg="white")
        self.lb_user.place(relx=0.5, rely=0.3, anchor="center")

        self.et_user = Entry(self.scr_login, font=("Arial", 15), bg="gray", fg="white")
        self.et_user.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.33)

        self.lb_password = Label(self.scr_login, bg=self.FUNDO, text="Password", fg="white")
        self.lb_password.place(relx=0.5, rely=0.5, anchor="center")

        self.et_password = Entry(self.scr_login, font=("Arial", 15), bg="gray", fg="white")
        self.et_password.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.53)

        self.bt_login = Button(self.scr_login, text="LOGIN", bg="blue", font=("arial", 15), fg="white")
        self.bt_login.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.07, anchor="center")

Application()
