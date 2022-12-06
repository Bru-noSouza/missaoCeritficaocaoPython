# IMPORTES
import tkinter as tk
from tkinter import *
import sqlite3
# Banco para feramentas
def cadastrar_ferramenta():
    conexao = sqlite3.connect('Feramentas.db')
    cc = conexao.cursor()

    cc.execute("INSERT INTO Feramenta VALUES (:codigo,:fabricante,:voltagem,:partnumber,:descrição,:tamanho,:unidademed,:tipo,:material)",
              {
                'codigo':codigoEntrada.get(),
                'fabricante':fabricanteEntrada.get(),
                'voltagem':voltagemEntrada.get(),
                'partnumber':partNumberEntrada.get(),
                'descrição':descricaoEntrada.get(),
                'tamanho':tamanhoEntrada.get(),
                'unidademed':unidadeMedidaEntrada.get(),
                'tipo':tipoEntrada.get(),
                'material':materialEntrada.get(),


              })
    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada



# Configuração Janela
topLevel = Tk()
topLevel.minsize(950, 400)
topLevel.config(background="#E0DFDA")
topLevel.title("Cadastro de Ferramenta")

# Configuração Frame e Label
topLevel.Label = Label(topLevel, text="CADASTRO DE FERRAMENTAS", font="Arial 18 bold", background="#E0DFDA", fg="#2B42A6")
topLevel.Label.place(x=20, y=20)

topLevel.frameMoldura = Frame(topLevel, bg="white", width=850, height=275)
topLevel.frameMoldura.place(x=25, y=60)

# Configuração CÓDIGO
topLevel.codigo = Label(topLevel.frameMoldura, text="Código", bg="white", font="Arial 13", fg="#1B2866" )
topLevel.codigo.place(x=20, y=20)
        
codigoEntrada = Entry(topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=30, highlightbackground = "#1B2866")
codigoEntrada.place(x=110, y=20)

# Configuração TAMANHO
tamanho = Label(topLevel.frameMoldura, text="Tamanho", bg="white", font="Arial 13", fg="#1B2866")
tamanho.place(x=470, y=20)
        
tamanhoEntrada = Entry(topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=30, highlightbackground = "#1B2866")
tamanhoEntrada.place(x=540, y=20)

# Configuração FABRICANTE
topLevel.fabricante = Label(topLevel.frameMoldura, text="Fabricante", bg="white", font="Arial 13", fg="#1B2866" )
topLevel.fabricante.place(x=20, y=70)
        
fabricanteEntrada = Entry(topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=30, highlightbackground = "#1B2866")
fabricanteEntrada.place(x=110, y=70)

# Configuração UNIDADE DE MEDIDA
topLevel.unidadeMedida = Label(topLevel.frameMoldura, text="Unidade de Medida", bg="white", font="Arial 13", fg="#1B2866")
topLevel.unidadeMedida.place(x=470, y=70)
        
unidadeMedidaEntrada = Entry(topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=23, highlightbackground = "#1B2866")
unidadeMedidaEntrada.place(x=595, y=70)

# Configuração VOLTAGEM
topLevel.voltagem = Label(topLevel.frameMoldura, text="Voltagem", bg="white", font="Arial 13", fg="#1B2866" )
topLevel.voltagem.place(x=20, y=120)
        
voltagemEntrada = Entry(topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=24, highlightbackground = "#1B2866")
voltagemEntrada.place(x=110, y=120)

topLevel.volts = Label(topLevel.frameMoldura, text="Volts", bg="white", font="Arial 13", fg="#1B2866" )
topLevel.volts.place(x=322, y=120)

# Configuração TIPO
topLevel.tipo = Label(topLevel.frameMoldura, text="Tipo", bg="white", font="Arial 13", fg="#1B2866" )
topLevel.tipo.place(x=470, y=120)
        
tipoEntrada = Entry(topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=30, highlightbackground = "#1B2866")
tipoEntrada.place(x=540, y=120)

# Configuração PART NUMBER
topLevel.partNumber = Label(topLevel.frameMoldura, text="Part Number", bg="white", font="Arial 13", fg="#1B2866" )
topLevel.partNumber.place(x=20, y=170)
        
partNumberEntrada = Entry(topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=30, highlightbackground = "#1B2866")
partNumberEntrada.place(x=110, y=170)

# Configuração MATERIAL
topLevel.material = Label(topLevel.frameMoldura, text="Material", bg="white", font="Arial 13", fg="#1B2866" )
topLevel.material.place(x=470, y=170)

materialEntrada = Entry(topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=30, highlightbackground = "#1B2866")
materialEntrada.place(x=540, y=170)

# Configuração DESCRIÇÃO
topLevel.descricao = Label(topLevel.frameMoldura, text="Descrição", bg="white", font="Arial 13", fg="#1B2866" )
topLevel.descricao.place(x=20, y=220)
        
descricaoEntrada = Entry(topLevel.frameMoldura, bg="#DCE0E6", font="Arial 13", fg="black", width=84, highlightbackground = "#1B2866")
descricaoEntrada.place(x=110, y=220)

# Botão Cadastrar
topLevel.botaoCadastro = Button(topLevel, text="CADASTRAR", bd=0,
        width=20, height=2, fg="#2C6928", font="Arial 13 bold",command=cadastrar_ferramenta)
topLevel.botaoCadastro.place(x=525, y=350)

topLevel.botaoCancelar = Button(topLevel,text="CANCELAR", bd=0,
        width=20, height=2, fg="#E80523", font="Arial 13 bold")
topLevel.botaoCancelar.place(x=235, y=350)

# FUNÇÃO PARA ABRIR TELA CADASTRO DE FERRAMENTAS  

topLevel.mainloop()





