import tkinter.messagebox
from tkinter import *
from BancoSQLITE import *

def cadastro():
    root.destroy()
    import reajuste_cadastro

def tecnico():
    root.destroy()
    import cadastroTecnico



root = Tk()
root.title('Login')
root.geometry('400x400')
root.resizable(False,False)


title = Label(root,text='Faça login ou cadastre-se', fg='#5d46e2',font="Arial 18 bold")
title.place(relx=0.14,rely=0.1)
cpfa = Label(root,text="Email",fg="#5d46e2",font="Arial 16 bold")
cpfa.place(relx=0.05,rely=0.25)
entry_email = Entry()

entry_email.place(relx=0.26, rely=0.25, relheight=0.06, relwidth=0.5)
lb_nome = Label(root, text='Usuário', fg='#5d46e2', font="Arial 16 bold")
lb_nome.place(relx=0.05, rely=0.35)

# entry Nome :-----------------
ent_nome = Entry()
ent_nome.place(relx=0.26,rely=0.35,relheight=0.06,relwidth=0.5)


lb_senha = Label(root, text='Senha',fg='#5d46e2', font="Arial 16 bold")
lb_senha.place(relx=0.05, rely=0.45)

# entry senha:-------------------
senha = Entry(root)
senha.place(relx=0.26, rely=0.45, relheight=0.06, relwidth=0.5)

# Buttons ------------------------
bt_cadastrar = Button(root, text="Cadastrar", background='#5d46e2', bd=2, fg='white',
                              font=('verdana', 8),command=cadastro)
bt_cadastrar.place(relx=0.30, rely=0.7,relheight=0.13)
## tecnico -----------------------
bt_cadastrar_tecnico = Button(root, text="Cadastrar"
                                         " Tecnico", background='#2E8B57', bd=2, fg='white',
                                   font=('verdana', 8),command=tecnico)
bt_cadastrar_tecnico.place(relx=0.49, rely=0.7, relheight=0.13)

# Comando de login ----------------


def fazer_login():

    for item in usuarios_cadastrados:
        print(item)
        

        if (entry_email.get() in item or ent_nome.get() in item) and senha.get() in item:
            root.destroy()
            import Novo_menu
         

        elif (entry_email.get() in item or ent_nome.get() in item) and senha.get() not in item: 
            tkinter.messagebox.showinfo(title="Login não validado", message="Senha inexistente")

        elif entry_email.get() not in item and ent_nome.get() not in item:
            tkinter.messagebox.showinfo(title="Login não validado", message="E-mail ou usuário inexistente")
            

    

       
    
   


# login


bt_login = Button(root, text="Login", background='#5d46e2', bd=2, fg='white',
                          font=('verdana', 8), command=fazer_login)
bt_login.place(relx=0.80, rely=0.7, relwidth=0.15, relheight=0.13)

root.mainloop()


# janela.withdraw()