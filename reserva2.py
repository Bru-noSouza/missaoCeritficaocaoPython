# Função para fechar a janela ---------------------------------
def cancelar():
    janelaReserva.destroy()

# Importes ---------------------------------------------------------------
import tkinter as tk
from tkinter import *

from tkcalendar import Calendar, DateEntry
def abrir():
    janelaReserva.destroy()
    import cadastroReserva2
    


from datetime import date

# Criando janela ---------------------------------------------------------------
janelaReserva = Tk()
janelaReserva.minsize(650, 500)
janelaReserva.maxsize(650, 500)
janelaReserva.config(background="#E0DFDA")
janelaReserva.title("Reserva")

# Criando Frame Title ---------------------------------------------------------------
frameBemVindo = Frame(master=janelaReserva, bg="#2B42A6", width=700, height=60)
frameBemVindo.place(x=0, y=0)

textBemVindo = Label(master=janelaReserva, text="BEM VINDO À RESERVA", font="Arial 20 bold", foreground="white", bg="#2B42A6")
textBemVindo.place(x=210, y=14)

# Criando Frame Verificação ---------------------------------------------------------------
textVerificacao = Label(master=janelaReserva, text="CONSULTAR DISPONIBILIDADE", font="Arial 18 bold", background="#E0DFDA", fg="#2B42A6")
textVerificacao.place(x=20, y=90)

frameVerificacao = Frame(master=janelaReserva, bg="white", width=600, height=225)
frameVerificacao.place(x=25, y=130)

# Código Ferramenta ---------------------------------------------------------------
l_codigo = Label(master=frameVerificacao, text="Código da Ferramenta", bg="white", font="Arial 13", fg="#1B2866" )
l_codigo.place(x=20, y=20)
        
e_codigo = Entry(master=frameVerificacao, bg="#DCE0E6", font="Arial 13", fg="black", width=20, highlightbackground = "#1B2866")
e_codigo.place(x=180, y=20)

# Data Retirada ---------------------------------------------------------------
l_data = Label(master=frameVerificacao, text="Data de Retirada", bg="white", font="Arial 13", fg="#1B2866" )
l_data.place(x=20, y=60)

e_data = DateEntry(master=frameVerificacao, width= 10, font=("Verdana 10"), borderwidth=0)
e_data.place(x=180, y=60)

# Hora Retirada ---------------------------------------------------------------
l_hora = Label(master=frameVerificacao, text="Hora de Retirada", bg="white", font="Arial 13", fg="#1B2866" )
l_hora.place(x=20, y=100)
        
optionsHora = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30",]

valorEscolhidoHora = StringVar()
valorEscolhidoHora.set(optionsHora[0])
horaDrop = OptionMenu(frameVerificacao, valorEscolhidoHora, *optionsHora)
horaDrop.config(bg="#DCE0E6", font="Arial 13", fg="black", width=7)
horaDrop.place(x=180, y=100)

# Data Devolução ---------------------------------------------------------------
l_dev = Label(master=frameVerificacao, text="Data de Retirada", bg="white", font="Arial 13", fg="#1B2866" )
l_dev.place(x=20, y=140)

e_dev = DateEntry(master=frameVerificacao, width= 10, font=("Verdana 10"), borderwidth=0)
e_dev.place(x=180, y=140)

# Hora Devolução ---------------------------------------------------------------
l_horaDev = Label(master=frameVerificacao, text="Hora de Retirada", bg="white", font="Arial 13", fg="#1B2866" )
l_horaDev.place(x=20, y=180)
        
optionsHoraDev = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30",]

valorEscolhidoHoraDev = StringVar()
valorEscolhidoHoraDev.set(optionsHora[0])
horaDevDrop = OptionMenu(frameVerificacao, valorEscolhidoHoraDev, *optionsHoraDev)
horaDevDrop.config(bg="#DCE0E6", font="Arial 13", fg="black", width=7)
horaDevDrop.place(x=180, y=180)

# Botões ---------------------------------------------------------------
botaoDisp = Button(master=janelaReserva, text="VERIFICAR DISPONIBILIDADE", bd=0, width=30, height=2, fg="#2C6928", font="Arial 13 bold",command=abrir)
botaoDisp.place(x=40, y=380)

botaoCancel = Button(master=janelaReserva, text="CANCELAR", bd=0, width=30, height=2, fg="#E80523", font="Arial 13 bold", command=cancelar)
botaoCancel.place(x=330, y=380)




janelaReserva.mainloop()

