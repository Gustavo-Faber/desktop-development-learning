from tkinter import *

contas = [["gustavo", "1234"]]

class Feats():
    def feat_btlogin(self):
        self.user = self.et_user.get()
        self.password = self.et_password.get()
        if [self.user, self.password] in contas:
            self.scr_login.forget()
            self.scr_main.pack(fill="both", expand=True)
        else:
            self.error_login.place(relx=0.5, rely=0.8, anchor="center")

    def clique(self, text):
        self.visor["text"] += text


class Application(Feats):
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.geometry("350x550")
        self.window.minsize(width=350, height=550)
        self.FUNDO = "#3B3B3B"
        self.window.configure(bg=self.FUNDO)
        self.screen_login()
        self.screen_main()

        self.window.mainloop()

    def screen_login(self):
        self.scr_login = Frame(self.window, bg=self.FUNDO)
        self.scr_login.pack(fill="both", expand=True)

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

        self.bt_login = Button(self.scr_login, text="LOGIN", bg="blue", font=("arial", 15), fg="white", command=self.feat_btlogin)
        self.bt_login.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.07, anchor="center")

        self.error_login = Label(self.scr_login, bg=self.FUNDO, text="Senha e/ou usuário incorretos!.", fg="red", font=("arial", 10))

    def screen_main(self):
        self.scr_main = Frame(self.window, bg=self.FUNDO)

        self.visor = Label(self.scr_main, bg="lightgray", text="")
        self.visor.place(relwidth=0.9, relheight=0.1, relx=0.5, rely=0.15, anchor="center")

        self.seven = Button(self.scr_main, text="7", bg="lightgray", command=lambda: self.clique("7"))
        self.seven.place(relx= 0.05, rely= 0.2, relwidth= 0.2, relheight= 0.1)

        self.eight = Button(self.scr_main, text="8", bg="lightgray", command=lambda: self.clique("8"))
        self.eight.place(relx= 0.25, rely= 0.2, relwidth= 0.2, relheight= 0.1)

        self.nine = Button(self.scr_main, text="9", bg="lightgray", command=lambda: self.clique("9"))
        self.nine.place(relx= 0.45, rely= 0.2, relwidth= 0.2, relheight= 0.1)

        self.four = Button(self.scr_main, text="4", bg="lightgray", command=lambda: self.clique("4"))
        self.four.place(relx= 0.05, rely= 0.3, relwidth= 0.2, relheight= 0.1)

        self.five = Button(self.scr_main, text="5", bg="lightgray", command=lambda: self.clique("5"))
        self.five.place(relx= 0.25, rely= 0.3, relwidth= 0.2, relheight= 0.1)

        self.six = Button(self.scr_main, text="6", bg="lightgray", command=lambda: self.clique("6"))
        self.six.place(relx= 0.45, rely= 0.3, relwidth= 0.2, relheight= 0.1)

        self.one = Button(self.scr_main, text="1", bg="lightgray", command=lambda: self.clique("1"))
        self.one.place(relx= 0.05, rely= 0.4, relwidth= 0.2, relheight= 0.1)

        self.two = Button(self.scr_main, text="2", bg="lightgray", command=lambda: self.clique("2"))
        self.two.place(relx= 0.25, rely= 0.4, relwidth= 0.2, relheight= 0.1)

        self.three = Button(self.scr_main, text="3", bg="lightgray", command=lambda: self.clique("3"))
        self.three.place(relx= 0.45, rely= 0.4, relwidth= 0.2, relheight= 0.1)

        self.soma = Button(self.scr_main, text="+", bg="lightgray", command=lambda: self.clique("+"))
        self.soma.place(relx= 0.65, rely= 0.5, relwidth= 0.2, relheight= 0.1)

        self.divisao = Button(self.scr_main, text="/", bg="lightgray", command=lambda: self.clique("/"))
        self.divisao.place(relx= 0.65, rely= 0.2, relwidth= 0.2, relheight= 0.1)

        self.subtracao = Button(self.scr_main, text="-", bg="lightgray", command=lambda: self.clique("-"))
        self.subtracao.place(relx= 0.65, rely= 0.4, relwidth= 0.2, relheight= 0.1)

        self.produto = Button(self.scr_main, text="x", bg="lightgray", command=lambda: self.clique("x"))
        self.produto.place(relx= 0.65, rely= 0.3, relwidth= 0.2, relheight= 0.1)



Application()
