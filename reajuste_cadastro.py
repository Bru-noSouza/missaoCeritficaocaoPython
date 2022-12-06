
from tkinter import *
from BancoSQLITE import *

def voltar():
    import LOGIN

def cadastrar_clente():
    conexao = sqlite3.connect('Users.db')
    cc = conexao.cursor()

    cc.execute("INSERT INTO Usuarios VALUES (:email,:usuario,:senha)",
              {
                  'email': entry_email.get(),
                  'usuario': entry_nome.get(),
                  'senha' : entry_senha.get(),

              })
    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0,"end")
    entry_senha.delete(0,"end")
    entry_email.delete(0,"end")
    window.destroy()
    return voltar()





window = Tk()
window.geometry('300x300')
window.resizable(False,False)
window.config(background="#E0DFDA")
# Title
window.title('Registre-se')



window.frameMoldura = Frame(
    master=window, bg="#E0DFDA", width=300, height=300)
window.frameMoldura.place(x=2, y=3)

window.Label = Label(master=window, text="CADASTRO",
                                  font="Arial 18 bold", background="#E0DFDA", fg="#2B42A6")
window.Label.place(x=75, y=2)

window.lb_email = Label(master=window.frameMoldura, text='Email',bg='#E0DFDA',fg='#5d46e2',font="Arial 16 bold")
window.lb_email.place(relx=0.01,rely=0.2)
# entry Nome :
entry_email = Entry(master=window.frameMoldura)
entry_email.place(relx=0.29, rely=0.22, relheight=0.06, relwidth=0.5)


window.lb_nome = Label(master=window.frameMoldura, text='Usuário',bg='#E0DFDA',fg='#5d46e2',font="Arial 16 bold")
window.lb_nome.place(relx=0.01,rely=0.3)
# entry Nome :
entry_nome = Entry(master=window.frameMoldura)
entry_nome.place(relx=0.29, rely=0.33, relheight=0.06, relwidth=0.5)
        

window.lb_senha = Label(master=window.frameMoldura, text='Senha',bg='#E0DFDA', fg='#5d46e2', font="Arial 16 bold")
window.lb_senha.place(relx=0.01, rely=0.42)

# entry senha:
entry_senha = Entry(master=window.frameMoldura)
entry_senha.place(relx=0.29, rely=0.44, relheight=0.06, relwidth=0.5)

window.ceck = Checkbutton(master=window.frameMoldura,text='Concordo com todos os termos',bg='#E0DFDA',fg='#5d46e2', font="Arial 9 italic")
window.ceck.place(relx=0.01,rely=0.62)

window.bt_login = Button(master=window.frameMoldura,text="Continuar", background='#5d46e2', bd=2, fg='white',
                               font=('verdana', 8),pady=5,command=cadastrar_clente)
window.bt_login.place(relx=0.74, rely=0.8)

window.bt_login = Button(master=window.frameMoldura,text="Cancelar", background='tomato', bd=2, fg='white',
                               font=('verdana', 8),command=window.destroy,pady=5)
window.bt_login.place(relx=0.47, rely=0.8)

window.mainloop()














