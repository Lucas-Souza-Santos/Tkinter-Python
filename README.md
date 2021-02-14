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

## podemos modificar o tamanho mínimo e máximo da janela

```janela.resizable(True, True)
janela.minsize(400, 400)
janela.maxsize(800, 500)
```

- o primeiro argumento é o comprimento ou width
- o segundo argumento é a altura ou height

```janela.resizable(True, True)
janela.minsize(width=400, height=400)
janela.maxsize(width=800, height=500)
```

As duas formas acimas dão certo

```janela.state("zoomed")```

inicia a janela nas larguras máximas

```janela.state("iconic")```

inicia a janela nas larguras mínimas

também pode ser mudado o icone da janela, usando:

```janela.iconbitmap("img/icone.ico")```

o caminho passado é local do icone
