# IMPORTES
import tkinter as tk
from tkinter import *
from openpyxl import *

from BancoSQLITE import *
import pandas as pd


def voltar():
    import LOGIN

# Relação com o Banco De dados
def cadastrar_tecnico():
    conexao = sqlite3.connect('Tecnicos.db')
    ck = conexao.cursor()

    ck.execute("INSERT INTO Tecnico VALUES (:cpf,:nome,:telefone,:turno,:equipe)",
              {
                  'cpf': cpfEntrada.get(),
                  'nome': nomeEntrada.get(),
                  'telefone' : telefoneNumero.get(),
                  'turno' : turnoEntrada.get(),
                  'equipe' : nomeEquipeEntrada.get()

              })
    # Commit as mudanças:

    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    cpfEntrada.delete(0,"end")
    nomeEntrada.delete(0,"end")
    telefonePrefixo.delete(0,"end")
    telefoneNumero.delete(0,"end")
    turnoEntrada.delete(0,"end")
    nomeEquipeEntrada.delete(0,"end")
    topLevel.destroy()
    return voltar()

# Configuração Janela
topLevel = Tk()
topLevel.minsize(670, 500)
topLevel.config(background="#E0DFDA")
topLevel.title("Cadastro de Técnico")

# Configuração Frame e Label
topLevel.Label = Label(master=topLevel, text="CADASTRO DE TÉCNICO",
                                    font="Arial 18 bold", background="#E0DFDA", fg="#2B42A6")
topLevel.Label.place(x=20, y=20)

topLevel.frameMoldura = Frame(
    master=topLevel, bg="white", width=600, height=315)
topLevel.frameMoldura.place(x=25, y=60)

# Configuração CPF
topLevel.cpf = Label(master=topLevel.frameMoldura,
                                  text="CPF", bg="white", font="Arial 13", fg="#1B2866")
topLevel.cpf.place(x=20, y=20)

cpfEntrada = Entry(master=topLevel.frameMoldura, bg="#DCE0E6",
                                         font="Arial 13", fg="black", width=50, highlightbackground="#1B2866")
cpfEntrada.place(x=130, y=20)

topLevel.cpfRequisito = Label(
            master=topLevel.frameMoldura, text="Inserir apenas dígitos numéricos.Não inserir '.' e '-'.", bg="white", font="Arial 12 italic", fg="#1B2866")
topLevel.cpfRequisito.place(x=130, y=50)

# Configuração NOME
topLevel.nome = Label(master=topLevel.frameMoldura,
                                   text="Nome", bg="white", font="Arial 13", fg="#1B2866")
topLevel.nome.place(x=20, y=90)

nomeEntrada = Entry(master=topLevel.frameMoldura, bg="#DCE0E6",
                                          font="Arial 13", fg="black", width=50, highlightbackground="#1B2866")
nomeEntrada.place(x=130, y=90)

# Configuração TELEFONE
topLevel.telefone = Label(
            master=topLevel.frameMoldura, text="Telefone", bg="white", font="Arial 13", fg="#1B2866")
topLevel.telefone.place(x=20, y=140)

telefonePrefixo = Entry(
            master=topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=2, highlightbackground="#1B2866")
telefonePrefixo.place(x=130, y=140)

telefoneNumero = Entry(
            master=topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=45, highlightbackground="#1B2866")
telefoneNumero.place(x=170, y=140)

# Configuração TURNO
topLevel.turno = Label(
            master=topLevel.frameMoldura, text="Turno", bg="white", font="Arial 13", fg="#1B2866")
topLevel.turno.place(x=20, y=190)

turnoEntrada = Entry(master=topLevel.frameMoldura, bg="#DCE0E6",
                                           font="Arial 13", fg="black", width=50, highlightbackground="#1B2866")
turnoEntrada.place(x=130, y=190)

topLevel.turnoRequisito = Label(
            master=topLevel.frameMoldura, text="Opções válidas: Matutino / Vespetirno / Noturno", bg="white", font="Arial 12 italic", fg="#1B2866")
topLevel.turnoRequisito.place(x=130, y=220)

# Configuração NOME EQUIPE
topLevel.nomeEquipe = Label(
            master=topLevel.frameMoldura, text="Nome da Equipe", bg="white", font="Arial 13", fg="#1B2866")
topLevel.nomeEquipe.place(x=20, y=260)

nomeEquipeEntrada = Entry(
            master=topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=50, highlightbackground="#1B2866")
nomeEquipeEntrada.place(x=148, y=260,width=435)

# Botão Cadastrar
topLevel.botaoCancelar = Button(master=topLevel, text="CANCELAR", bd=0,
                                             width=20, height=2, fg="#E80523", font="Arial 13 bold",command=topLevel.destroy)
topLevel.botaoCancelar.place(x=100, y=390)

topLevel.botaoCadastro = Button(master=topLevel, text="CADASTRAR", bd=0,
                                             width=20, height=2, fg="#2C6928", font="Arial 13 bold",command=cadastrar_tecnico)
topLevel.botaoCadastro.place(x=350, y=390)

topLevel.mainloop()