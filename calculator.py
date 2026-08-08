from tkinter import *
import sqlite3

class Feats():
    def feat_btlogin(self):
        self.conecta_bd()
        self.user = self.et_user.get()
        self.password = self.et_password.get()
        self.cursor.execute("""SELECT * FROM users""")
        self.contas = self.cursor.fetchall()
        if any(self.user == conta[1] and self.password == conta[2] for conta in self.contas):
            self.scr_login.forget()
            self.scr_main.pack(fill="both", expand=True)
        else:
            self.error_login.place(relx=0.5, rely=0.8, anchor="center")
        self.desconecta_bd()
    def clique(self, text):
        self.operadores = ["+", "-", "x", "/"]
        self.textvisor = self.visor["text"]

        if text == "=":
             self.visor["text"] = str(eval(self.visor["text"]))
        elif text == "C":
            if self.visor["text"] == " ":
                return
            self.visor["text"] = self.visor["text"][:-1]
        elif text == "AC":
            self.visor["text"] = " "
        elif self.visor == " " and text in self.operadores:
            return
        elif not (self.textvisor[-1] in self.operadores and text in self.operadores):
            self.visor["text"] += text
        else:
            return
    def conecta_bd(self):
        self.conn = sqlite3.connect("banco.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando do banco de dados")
    def monta_tabelas(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL UNIQUE,
            pass TEXT NOT NULL
            )""")

        self.cursor.execute("""
        INSERT OR IGNORE INTO users (user, pass)
        VALUES ('admin', '1234')
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def switch_mode(self):
        if self.w_mode:
            self.black_mode()
            self.modo.configure(text="☀️")
            self.w_mode = False
        else:
            self.white_mode()
            self.modo.configure(text="🌙")
            self.w_mode = True
        self.aplicar_tema()

    def aplicar_tema(self):
        self.window.configure(bg=self.FUNDO)
        self.scr_main.configure(bg=self.FUNDO)
        self.scr_login.configure(bg=self.FUNDO)
        self.visor.configure(bg=self.FUNDOB, fg=self.FUNDOL)
        self.lb_login.configure(bg=self.FUNDO, fg=self.FUNDOL)
        self.lb_user.configure(bg=self.FUNDO, fg=self.FUNDOL)
        self.lb_password.configure(bg=self.FUNDO, fg=self.FUNDOL)
        self.et_user.configure(bg=self.FUNDOB, fg=self.FUNDOL)
        self.et_password.configure(bg=self.FUNDOB, fg=self.FUNDOL)
        self.error_login.configure(bg=self.FUNDO)

        botoes = [self.seven, self.eight, self.nine,
              self.four, self.five, self.six,
              self.one, self.two, self.three,
              self.zero, self.soma, self.subtracao,
              self.produto, self.divisao, self.resolver,
              self.delete, self.delall, self.parl,
              self.parr, self.point, self.modo]
    
        for bt in botoes:
            bt.configure(bg=self.FUNDOB, fg=self.FUNDOL)

class Application(Feats):
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.geometry("350x550")
        self.window.minsize(width=350, height=550)
        self.white_mode()
        self.w_mode = True
        self.monta_tabelas()
        self.screen_login()
        self.screen_main()

        self.window.mainloop()

    def screen_login(self):
        self.scr_login = Frame(self.window, bg=self.FUNDO)
        self.scr_login.pack(fill="both", expand=True)

        self.lb_login = Label(self.scr_login, bg=self.FUNDO, text="Login", fg=self.FUNDOL, font=("Arial", 25))
        self.lb_login.place(relx=0.5, rely=0.2, anchor="center")

        self.lb_user = Label(self.scr_login, bg=self.FUNDO, text="User", fg=self.FUNDOL)
        self.lb_user.place(relx=0.5, rely=0.3, anchor="center")

        self.et_user = Entry(self.scr_login, font=("Arial", 15), bg="gray", fg=self.FUNDOL)
        self.et_user.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.33)

        self.lb_password = Label(self.scr_login, bg=self.FUNDO, text="Password", fg=self.FUNDOL)
        self.lb_password.place(relx=0.5, rely=0.5, anchor="center")

        self.et_password = Entry(self.scr_login, font=("Arial", 15), bg="gray", fg=self.FUNDOL)
        self.et_password.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.53)

        self.bt_login = Button(self.scr_login, text="LOGIN", bg="blue", font=("arial", 15), fg=self.FUNDOL, command=self.feat_btlogin)
        self.bt_login.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.07, anchor="center")

        self.error_login = Label(self.scr_login, bg=self.FUNDO, text="Incorrect password and/or username!", fg="red", font=("arial", 10))

    def screen_main(self):
        self.scr_main = Frame(self.window, bg=self.FUNDO)

        self.visor = Label(self.scr_main, bg=self.FUNDOB, text=" ", font=("Arial", 20))
        self.visor.place(relwidth=1, relheight=0.1, relx=0.5, rely=0.15, anchor="center")

        self.seven = Button(self.scr_main, text="7", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("7"))
        self.seven.place(relx= 0.0, rely= 0.3, relwidth= 0.25, relheight= 0.1)

        self.eight = Button(self.scr_main, text="8", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("8"))
        self.eight.place(relx= 0.25, rely= 0.3, relwidth= 0.25, relheight= 0.1)

        self.nine = Button(self.scr_main, text="9", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("9"))
        self.nine.place(relx= 0.50, rely= 0.3, relwidth= 0.25, relheight= 0.1)

        self.four = Button(self.scr_main, text="4", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("4"))
        self.four.place(relx= 0.0, rely= 0.4, relwidth= 0.25, relheight= 0.1)

        self.five = Button(self.scr_main, text="5", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("5"))
        self.five.place(relx= 0.25, rely= 0.4, relwidth= 0.25, relheight= 0.1)

        self.six = Button(self.scr_main, text="6", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("6"))
        self.six.place(relx= 0.50, rely= 0.4, relwidth= 0.25, relheight= 0.1)

        self.one = Button(self.scr_main, text="1", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("1"))
        self.one.place(relx= 0.0, rely= 0.5, relwidth= 0.25, relheight= 0.1)

        self.two = Button(self.scr_main, text="2", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("2"))
        self.two.place(relx= 0.25, rely= 0.5, relwidth= 0.25, relheight= 0.1)

        self.three = Button(self.scr_main, text="3", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("3"))
        self.three.place(relx= 0.50, rely= 0.5, relwidth= 0.25, relheight= 0.1)

        self.zero = Button(self.scr_main, text="0", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("0"))
        self.zero.place(relx= 0.25, rely= 0.6, relwidth= 0.25, relheight= 0.1)

        self.soma = Button(self.scr_main, text="+", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("+"))
        self.soma.place(relx= 0.75, rely= 0.5, relwidth= 0.25, relheight= 0.1)

        self.divisao = Button(self.scr_main, text="/", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("/"))
        self.divisao.place(relx= 0.75, rely= 0.2, relwidth= 0.25, relheight= 0.1)

        self.subtracao = Button(self.scr_main, text="-", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("-"))
        self.subtracao.place(relx= 0.75, rely= 0.4, relwidth= 0.25, relheight= 0.1)

        self.produto = Button(self.scr_main, text="x", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("*"))
        self.produto.place(relx= 0.75, rely= 0.3, relwidth= 0.25, relheight= 0.1)

        self.resolver = Button(self.scr_main, text="=", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("="))
        self.resolver.place(relx= 0.75, rely= 0.6, relwidth= 0.25, relheight= 0.1)

        self.delete = Button(self.scr_main, text="C", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("C"))
        self.delete.place(relx= 0.0, rely= 0.2, relwidth= 0.25, relheight= 0.1)

        self.parl = Button(self.scr_main, text="(", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("("))
        self.parl.place(relx= 0.25, rely= 0.2, relwidth= 0.25, relheight= 0.1)

        self.parr = Button(self.scr_main, text=")", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique(")"))
        self.parr.place(relx= 0.50, rely= 0.2, relwidth= 0.25, relheight= 0.1)

        self.delall = Button(self.scr_main, text="AC", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("AC"))
        self.delall.place(relx= 0.50, rely= 0.6, relwidth= 0.25, relheight= 0.1)

        self.point = Button(self.scr_main, text=".", bg=self.FUNDOB, fg=self.FUNDOL, font=("Arial", 15), command=lambda: self.clique("."))
        self.point.place(relx= 0, rely= 0.6, relwidth= 0.25, relheight= 0.1)

        self.modo = Button(self.window, text="🌙", bg=self.FUNDOB, command=self.switch_mode)
        self.modo.place(relx=0, rely=0, relwidth=0.25, relheight=0.1)


    def white_mode(self):
        self.FUNDO = "white"
        self.FUNDOB = "gray"
        self.FUNDOL = "black"

    def black_mode(self):
        self.FUNDO = "#242424"
        self.FUNDOB = "#3B3B3B"
        self.FUNDOL = "white"

Application()
