from BancoSQLITE import *
# Função para fechar a janela ---------------------------------
def cancelar():
    finalCadReserva.destroy()

# Importes --------------------------------------------------------------
import tkinter as tk
from tkinter import *
import tkinter.messagebox

def reserva_aceita():
    for tecnicos in tecnicos_cadstrados:
        print(tecnicos)

        if e_nome.get() in tecnicos:
            finalCadReserva.destroy()
            tkinter.messagebox.Mensage.showinfo(title='None',message='Reserva Efetuada com Sucesso')

        

            

# Criando finalização cadastro reserva ----------------------------------
finalCadReserva = Tk()
finalCadReserva.minsize(800, 280) 
finalCadReserva.config(background="#E0DFDA")
finalCadReserva.title("Cadastro de Reserva")

# Frame title -----------------------------------------------------------
LabelDisponibilidade = Label(master=finalCadReserva, text="FERRAMENTA DISPONÍVEL PARA RESERVA", font="Arial 20 italic bold", background="#E0DFDA", fg="#2C6928")
LabelDisponibilidade.place(relx=0.12)

textDisponibilidade = Label(master=finalCadReserva, text="FINALIZAÇÃO DO CADASTRO DA RESERVA", font="Arial 14 bold", background="#E0DFDA", fg="#2B42A6")
textDisponibilidade.place(x=20, y=80)

# 2º Frame --------------------------------------------------------------
frameMoldura = Frame(master=finalCadReserva, bg="white", width=750, height=70)
frameMoldura.place(x=20, y=115)

# Nome do técnico -------------------------------------------------------
l_nome = Label(master=frameMoldura, text="Técnico Responsável", bg="white", font="Arial 13", fg="#1B2866")
l_nome.place(x=10, y=21)

e_nome = Entry(frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=60, highlightbackground="#1B2866")
e_nome.place(x=180, y=21)

# Botão Cancelar e Cadastrar
botaoCancelar = Button(master=finalCadReserva, text="CANCELAR", bd=0, width=20, height=2, fg="#E80523", font="Arial 13 bold", command=cancelar)
botaoCancelar.place(x=175, y=210)

botaoCadastro = Button(master=finalCadReserva, text="CADASTRAR", bd=0, width=20, height=2, fg="#2C6928", font="Arial 13 bold",command=reserva_aceita)
botaoCadastro.place(x=450, y=210)


finalCadReserva.mainloop()