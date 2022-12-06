from tkinter import *
from tkinter import ttk
from BancoSQLITE import *


def nv_feramenta():
    import cadastroFerramenta

def cadstro_reserva():
    import reserva2



menu = Tk()
# Configurações de janela

menu.title('Menu')
menu.geometry("1200x550")
menu.resizable(False, False)
menu.configure(background='#708090')
style = ttk.Style(menu)
style.theme_use("clam")

# configuraçoes Header
Central_Ferramenta = Label(menu, text="Central de Feramentas",fg="white",
                           font="verdana 18 bold", background="#708090"
                           )
Central_Ferramenta.place(relx=0.20,rely=0.01)

entry_buscar = Entry(menu)
entry_buscar.place(relx=0.1,rely=0.1,height=30)


botao_buscar = Button(text= "Buscar",background="#1E90FF", font="verdana",fg="white")
botao_buscar.place(relx=0.33,rely=0.1,height=30)

botao_buscar = Button(text= "Nova Feramenta",background="#1E90FF", font="verdana", fg="white",command=nv_feramenta)
botao_buscar.place(relx=0.6,rely=0.1,height=30)
# Main Atalhos
frame = Frame(menu, bd=4, bg='#dfe3ee',
                            highlightbackground='#759fe6', highlightthickness=6, width=1200)
frame.place(relx=0.02, rely=0.30, relwidth=0.96, relheight=0.46)

    # Adicionando vertical scrollbar na tabela de dados
vertical_scroll = ttk.Scrollbar(master=frame)
vertical_scroll.pack(side=RIGHT, fill=Y)

    # Criando a tabela de dados 
lista_itens = []
global tabela_dados
itens_head = ["codigo", "fabricante", "voltagem", "partnumber", "descrição", "tamanho", "unidademed", "tipo", "material"]

tabela_dados = ttk.Treeview(master=frame, 
columns=itens_head, show="headings", height=5, yscrollcommand=vertical_scroll.set, selectmode="extended")
style.configure("Treeview", rowheight=31)

    # Configurando o tamanho das colunas
tabela_dados.column("codigo", minwidth=1, width=50)
tabela_dados.column("fabricante", minwidth=1, width=150)
tabela_dados.column("voltagem", minwidth=1, width=140)
tabela_dados.column("partnumber", minwidth=1, width=135)
tabela_dados.column("descrição", minwidth=1, width=150)
tabela_dados.column("tamanho", minwidth=1, width=120)
tabela_dados.column("unidademed", minwidth=1, width=120)
tabela_dados.column("tipo", minwidth=1, width=120)
tabela_dados.column("material", minwidth=1, width=120)


    # Configurando o heading das colunas
tabela_dados.heading("codigo", text="CÓDIGO")
tabela_dados.heading("fabricante", text="Fabricante")
tabela_dados.heading("voltagem", text="Voltagem")
tabela_dados.heading("partnumber", text="Part Number")
tabela_dados.heading("descrição", text="Descrição")
tabela_dados.heading("tamanho", text="Tamanho")
tabela_dados.heading("unidademed", text="Unid. Medida")
tabela_dados.heading("tipo", text="Tipo")
tabela_dados.heading("material", text="Material")

    # Inserindo dados do banco no Treeview
msg.execute("""SELECT * FROM Feramenta""")
resultado = msg.fetchall()
for row in resultado:
        tabela_dados.insert("", "end", values=row)
tabela_dados.pack(padx=10)

    # Configurando o vertical scrollbar 
vertical_scroll.config(command=tabela_dados.yview)

# Configurando o vertical scrollbar --------------------------------------------------------------------------------------------------------------------------------
vertical_scroll.config(command=tabela_dados.yview)




botao_exportar = Button(text="Exportar base de Ferramentas",font="verdana 8",background="#1E90FF",fg="white",command=exportar_ferramentas)
botao_exportar.place(relx=0.6,rely=0.9,height=30)

botao_reserva= Button(text="Solicitar Reservsa",font="verdana 8 ",background="#1E90FF", fg="white",command=cadstro_reserva)
botao_reserva.place(rely=0.9,relx=0.32,height=30)
consultar_reserva = Button(text="Consultar reserva",font="verdana 8 ",background="#1E90FF", fg="white")
consultar_reserva.place(relx=0.05,rely=0.9,height=30)


menu.mainloop()