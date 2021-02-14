from  tkinter import *

# criando a janela de aplicação

janela = Tk()

# Mudando o nome da janela 
janela.title('Janela Python')

# Modificando as dimensões da janela
janela.geometry('300x300+0+0')

janela.resizable(True, True)
janela.minsize(400, 400)
janela.maxsize(800, 500)

janela.iconbitmap("img/icone.ico")

janela.mainloop()
