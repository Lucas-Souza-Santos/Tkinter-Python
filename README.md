# Curso de Tkinter-Python

## Crindo a primeira Janela com o modulo tkinter

```from  tkinter import *

janela = Tk()

janela.title('Janela Python')

janela.mainloop()
```

Os comandos acima são:

- importando o tudo do modulo tkinter através de *
- criando uma instância de Tk, com o nome janela
- Trocando o nome da janela
- rodando a aplicação usando o comando janela.mainloop(), que ficará rodando até a janela for fechada.

## modificando o tamanho da janela

```janela.geometry('widthxheight+posição_x+posição_y')```

- width largura da janela
- height altura da janela
- posição_x aonde a janela será aberta da tela do computador
- posição_y altura da tela da janela que será aberta a janela
