#TORTUGA-VERSÃO MAIS REDENTE
#BIBLIOTEDAS
import turtle
from random import randint 
import winsound
import os
from tkinter import *
from time import sleep
ui=True
bk=False
def fase2():
    #DOLODANDO O TEMPO
    os.chdir("D:\\")
    global ui
    global bk
    global wn
    global abi
    global tempo
    global time
    global resposta
    global scor
    global ac
    global ag
    global al
    global aco
    global asa
    global ja
    global bc
    global bm
    global scor
    global bb
    for i in inimigos:
        i.hideturtle()
    time=60
    cane= turtle.Turtle()
    cane.speed(0)
    cane.shape('turtle')
    cane.color('black')
    cane.penup()
    cane.hideturtle()
    cane.goto(-450,130)
    def tempo():
        global time
        global music
        if time>=0:
            cane.clear()
            cane.write(('Tempo:',time), align= 'center', font=('Dourier',24, 'normal'))
            time-=1
        if scor==100:
            return
        wn.ontimer(tempo,800)
        
    #MÚSIDA
    winsound.PlaySound("D:/Lógica e Linguagem de Pgm/Projeto de Conclusão/Músicas/Música de fundoa.wav", winsound.SND_ASYNC)
        
    #SDORE E RESPOSTA
    scor=0
    resposta=""

    #DRIANDO TARTARUDA PRINDIPAL
    b = turtle.Turtle()

    #DRIANDO A TELA
    wn = turtle.Screen() 
    wn.bgcolor('Light Goldenrod')
    wn.title('Save the ocean!')
    b.pu() 
    b.goto(-250,250)
    b.pd()
    for i in range(4):
        b.fd(500)
        b.right(90)
    b.pu()
    b.goto(0,0)
    b.shape("turtle")
    b.color('dark green')
    b.shapesize(1)
    b.hideturtle()

    #DRIANDO O DENÁRIO
    cena=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/teste.gif")
    cena.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/teste.gif")
        
    #REGISTRO DE SDORE 
    pen= turtle.Turtle()
    pen.speed(0)
    pen.shape('turtle')
    pen.color('black')
    pen.penup()
    pen.hideturtle()
    pen.goto(-450,170)
    pen.write(('Score:',scor), align= 'center', font=('Courier',24, 'normal'))

    def escrever():
        if scor<110:
            pen.write(('Score:',scor), align= 'center', font=('Courier',24, 'normal'))
        else:
            pen.write(('Score:',100), align= 'center', font=('Courier',24, 'normal'))
                        
    #DRIANDO AS LATAS DE LIXO
    bk=False
    def metal():
        global resposta, scor, bk
        if resposta=='lata' and bk==False:
            m.goto(-186,190)
            m.hideturtle()
            scor+=10
            bk=True
            pen.clear()
            escrever()
    bt = Button(width=10, text='Metal', command=metal)
    bt.place(x=460, y=200)
    amare= turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixoamarelo.gif")
    amare.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixoamarelo.gif")
    amare.pu()
    amare.goto(-185,190)

    ac= True
    ag= True
    al= True
    aco= True
    asa= True
    def plastico():
        global resposta
        global scor
        global ac
        global ag
        global al
        global aco
        global asa
        if resposta=='canudo' or resposta=='garrafa' or resposta=='lixos' or resposta=='copo' or resposta=='sacola':
            if resposta=='canudo' and ac==True:
                n.goto(-95,190)
                n.hideturtle()
                scor+=10
                ac=False
            elif resposta=='garrafa' and ag==True:
                j.goto(-95,190)
                j.hideturtle()
                scor+=10
                ag=False 
            elif resposta=='lixos' and al==True:
                r.goto(-95,190)
                r.hideturtle()
                scor+=10
                al=False
            elif resposta=='copo' and aco==True:
                p.goto(-95,190)
                p.hideturtle()
                scor+=10
                aco=False
            elif resposta=='sacola' and asa==True:
                t.goto(-95,190)
                t.hideturtle()
                scor+=10
                asa=False
            pen.clear()
            escrever()
        
    bt = Button(width=10, text='Plástico', command=plastico)
    bt.place(x=550, y=200)
    plas=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixovermelho.gif")
    plas.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixovermelho.gif")
    plas.pu()
    plas.goto(-95,190)
    
    ja= True
    def vidro():
        global resposta
        global scor
        global ja
        if resposta=='caco' and ja== True:
            l.goto(-5,190)
            l.hideturtle()
            scor+=10
            pen.clear()
            escrever()
            ja= False

    bt = Button(width=10, text='Vidro', command=vidro)
    bt.place(x=640, y=200)
    vidro=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixoverde.gif")
    vidro.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixoverde.gif")
    vidro.pu()
    vidro.goto(-5,190)


    def papel():
        print('bt_click')
    bt = Button(width=10, text='Papel', command=papel)
    bt.place(x=730, y=200)
    papel=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixoazul.gif")
    papel.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixoazul.gif")
    papel.pu()
    papel.goto(85,189)

    bc= True
    bm= True
    def organico():
        global resposta
        global scor
        global bc
        global bm
        if resposta=='casca' or resposta=='maca':
            if resposta=='casca' and bc== True:
                o.goto(175,188)
                o.hideturtle()
                bc=False
                scor+=10
            elif resposta=='maca' and bm==True:
                s.goto(175,188)
                s.hideturtle()
                bm=False
                scor+=10
            pen.clear()
            escrever()
    bt = Button(width=10, text='Orgânico', command=organico)
    bt.place(x=820, y=200)
    organico=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixomarrom.gif")
    organico.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixomarrom.gif")
    organico.pu()
    organico.goto(175,188)

    bb=True
    def nreciclavel():
        global resposta
        global scor
        global bb
        if resposta=='bota' and bb==True:
            k.goto(-5,86)
            k.hideturtle()
            scor+=10
            pen.clear()
            escrever()
            bb=False
    bt = Button(width=10, text='Não Reciclável', command=nreciclavel)
    bt.place(x=640, y=300)
    reci=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixocinza.gif")
    reci.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario/lixocinza.gif")
    reci.pu()
    reci.goto(-5,86)

    #DRIANDO OS LIXOS
    def garrafa():
        global resposta
        resposta='garrafa'
    bt = Button(width=5, text='Garrafa', command=garrafa)
    bt.place(x=763, y=480)
    j=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/garrafa.gif")
    j.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/garrafa.gif")
    j.pu()
    j.goto(100,-100)

    def bota():
        global resposta
        resposta='bota'
    bt = Button(width=5, text='Bota', command=bota)
    bt.place(x=843, y=400)
    k=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/bota.gif")
    k.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/bota.gif")
    k.pu()
    k.goto(180,-20)

    def caco():
        global resposta
        resposta='caco'
    bt = Button(width=5, text='Daco', command=caco)
    bt.place(x=683, y=420)
    l=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/caco.gif")
    l.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/caco.gif")
    l.pu()
    l.goto(20,-50)

    def lata():
        global resposta
        resposta='lata'
    bt = Button(width=5, text='Lata', command=lata)
    bt.place(x=561, y=478)
    m=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/lata.gif")
    m.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/lata.gif")
    m.pu()
    m.goto(-100,-100)

    def canudo():
        global resposta
        resposta='canudo'
    bt = Button(width=5, text='Danudo', command=canudo)
    bt.place(x=500, y=441)
    n=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/canudo.gif")
    n.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/canudo.gif")
    n.pu()
    n.goto(-170,-70)

    def casca():
        global resposta
        resposta='casca'
    bt = Button(width=5, text='Dasca', command=casca)
    bt.place(x=460, y=489)
    o=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/casca.gif")
    o.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/casca.gif")
    o.pu()
    o.goto(-205,-120)

    def copo():
        global resposta
        resposta='copo'
    bt = Button(width=5, text='Dopo', command=copo)
    bt.place(x=512, y=535)
    p=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/copo.gif")
    p.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/copo.gif")
    p.pu()
    p.goto(-150,-220)

    def lixos():
        global resposta
        resposta='lixos'
    bt = Button(width=5, text='Saco', command=lixos)
    bt.place(x=863, y=560)
    r=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/lixo.gif")
    r.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/lixo.gif")
    r.pu()
    r.goto(200,-180)

    def maca():
        global resposta
        resposta='maca'
    bt = Button(width=5, text='Maça', command=maca)
    bt.place(x=665, y=498)
    s=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/maça.gif")
    s.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/maça.gif")
    s.pu()
    s.goto(0,-120)

    def sacola():
        global resposta
        resposta='sacola'
    bt = Button(width=5, text='Sacola', command=sacola)
    bt.place(x=685, y=565)
    t=turtle.Turtle()
    wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/saco.gif")
    t.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/saco.gif")
    t.pu()
    t.goto(20,-190)
    def gamefase3():
        global music
        global ac
        global ag
        global al
        global aco
        global asa
        global ja
        global bc
        global bm
        global scor
        global bb
        global tempo
        global ui
        if scor==100 and ui==True:
            ui== False
            pen.clear()
            pen.write(('Parabéns!'), align= 'center', font=('Courier',24, 'normal'))
            cane.clear()
            cane.write(('Você ganhou',answer,'!'), align= 'center', font=('Courier',24, 'normal'))
            return winsound.PlaySound("D:/Lógica e Linguagem de Pgm/Projeto de Conclusão/Músicas/Música de ganhar.wav", winsound.SND_ASYNC)
        if time<=0:
            pen.clear()
            pen.write('Seu tempo acabou!', align= 'center', font=('Courier',24, 'normal'))
            cane.clear()
            cane.write('Tente novamente!', align= 'center', font=('Courier',24, 'normal'))
            already=True
            ac=False
            ag=False
            al=False
            aco=False
            asa=False
            ja=False
            bc=False
            bm=False
            bb=False
            winsound.PlaySound("D:/Lógica e Linguagem de Pgm/Projeto de Conclusão/Músicas/Música de perder.wav", winsound.SND_ASYNC)
            return 
    gamefase3()
    tempo()
#SDORE
score= 0

#DRIANDO TARTARUDA PRINDIPAL
b = turtle.Turtle()

#DRIANDO A TELA
wn = turtle.Screen() 
wn.bgcolor('light blue')
wn.title('Save the ocean!')
b.pu() 
b.goto(-250,250)
b.pd()
for i in range(4):
    b.fd(500)
    b.right(90)
b.pu()
b.goto(0,0)
b.shape("turtle")
b.color('dark green')
b.shapesize(1)
ji=True
#MÚSIDA
def music():
     return winsound.PlaySound("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Músicas\Música de fundo.wav", winsound.SND_ASYNC)
music()

#DUNÇÃO DE POSIDIONAR
def posicionar(coisa):
    x = randint(-240,240)
    y = randint(-240,240)
    coisa.goto(x,y)

#REDISTRO DE SDORE 
pen= turtle.Turtle()
pen.speed(0)
pen.shape('turtle')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,-290)
pen.write(('Score:',score), align= 'center', font=('Courier',24, 'normal'))

#DRIANDO INIMIDOS
inimigos=[]
c=turtle.Turtle()
c.pu()
posicionar(c)
a=turtle.Turtle()
a.pu()
posicionar(a)
e=turtle.Turtle()
e.pu()
posicionar(e)
o=turtle.Turtle()
o.pu()
posicionar(o)
r=turtle.Turtle()
r.pu()
posicionar(r)
os.chdir("D:\\")
wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Inimigos/navio.gif")
c.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Inimigos/navio.gif")
wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Inimigos/rede.gif")
a.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Inimigos/rede.gif")
wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Inimigos/arpão.gif")
e.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Inimigos/arpão.gif")
wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Inimigos/pescador.gif")
o.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Inimigos/pescador.gif")
wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Inimigos/anzol.gif")
r.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Inimigos/anzol.gif")
inimigos.append(c)
inimigos.append(a)
inimigos.append(e)
inimigos.append(o)
inimigos.append(r)

#MOVIMENTANDO OS INIMIDOS 
def move():
    c.setheading(c.towards(b))
    c.speed(100)
    c.forward(5)
    if c.distance(b)<=25 and ji==True:
        b.hideturtle()
        c.goto(-400,400)
        c.hideturtle()
        pen.clear()
        pen.write('GAME OVER', align= 'center', font=('Courier',24, 'normal'))
        winsound.PlaySound("D:/Lógica e Linguagem de Pgm/Projeto de Conclusão/Músicas/Música de perder.wav", winsound.SND_ASYNC)
        return
    a.setheading(a.towards(b))
    a.forward(5)
    a.speed(100)
    if a.distance(b)<=25 and ji==True :
        b.hideturtle()
        a.goto(-400,400)
        a.hideturtle()
        pen.clear()
        pen.write('GAME OVER', align= 'center', font=('Courier',24, 'normal'))
        winsound.PlaySound("D:/Lógica e Linguagem de Pgm/Projeto de Conclusão/Músicas/Música de perder.wav", winsound.SND_ASYNC)
        return
    e.setheading(e.towards(b))
    e.forward(5)
    e.speed(100)
    if e.distance(b)<=25 and ji==True :
        b.hideturtle()
        e.goto(-400,400)
        e.hideturtle()
        pen.clear()
        pen.write('GAME OVER', align= 'center', font=('Courier',24, 'normal'))
        winsound.PlaySound("D:/Lógica e Linguagem de Pgm/Projeto de Conclusão/Músicas/Música de perder.wav", winsound.SND_ASYNC)
        return
    o.setheading(o.towards(b))
    o.forward(5)
    o.speed(100)
    if o.distance(b)<=25 and ji==True :
        b.hideturtle()
        o.goto(-400,400)
        o.hideturtle()
        pen.clear()
        pen.write('GAME OVER', align= 'center', font=('Courier',24, 'normal'))
        winsound.PlaySound("D:/Lógica e Linguagem de Pgm/Projeto de Conclusão/Músicas/Música de perder.wav", winsound.SND_ASYNC)
        
        return
    r.setheading(r.towards(b))
    r.forward(5)
    r.speed(100)
    if r.distance(b)<=25 and ji==True:
        b.hideturtle()
        r.goto(-400,400)
        r.hideturtle()
        pen.clear()
        pen.write('GAME OVER', align= 'center', font=('Courier',24, 'normal'))
        winsound.PlaySound("D:/Lógica e Linguagem de Pgm/Projeto de Conclusão/Músicas/Música de perder.wav", winsound.SND_ASYNC)
        return
    wn.ontimer(move,10)

#DRIANDO LIXOS
os.chdir("D:\\")
lixao=[]
x1={'register':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/garrafa.gif",'shape':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/garrafa.gif"}
lixao.append(x1)
x2={'register':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/bota.gif",'shape':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/bota.gif"}
lixao.append(x2)
x3={'register':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/caco.gif",'shape':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/caco.gif"}
lixao.append(x3)
x4={'register':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/canudo.gif",'shape':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/canudo.gif"}
lixao.append(x4)
x5={'register':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/casca.gif",'shape':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/casca.gif"}
lixao.append(x5)
x6={'register':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/copo.gif",'shape':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/copo.gif"}
lixao.append(x6)
x7={'register':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/lata.gif",'shape':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/lata.gif"}
lixao.append(x7)
x8= {'register':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/lixo.gif",'shape':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/lixo.gif"}
lixao.append(x8)
x9={'register':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/maça.gif",'shape':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/maça.gif"}
lixao.append(x9)
x10={'register':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/saco.gif",'shape':"D:\Lógica e Linguagem de Pgm\Projeto de Conclusão/Lixos/saco.gif"}
lixao.append(x10)
lixos = []
for i in range(10):
    t = turtle.Turtle()
    wn.register_shape(lixao[i]['register'])
    t.shape(lixao[i]['shape'])
    t.pu()
    posicionar(t)
    lixos.append(t)
    
def escrever():
    pen.write(('Score:',score), align= 'center', font=('Courier',24, 'normal'))
    
def fd():
    global score
    global ji
    b.forward(4)
    x,y = b.position()
    for i in lixos:
        if b.distance(i) <= 20.0:
            lixos.remove(i) 
            i.hideturtle()
            i.goto(-400,400)
            score+=10
            pen.clear()
            escrever()
        if score==100 and ji==True:
            ji=False
            pen.clear()
            pen.write(('Parabéns',answer,'você ganhou!'), align= 'center', font=('Courier',18, 'bold'))
            pen.clear()
            ce.hideturtle()
            b.hideturtle()
            fase2()
    for i in inimigos:
        if b.distance(i) <= 20.0 and ji==True:
            b.hideturtle()
            i.goto(-400,400)
            i.hideturtle()
            pen.clear()
            pen.write('GAME OVER', align= 'center', font=('Courier',24, 'normal'))
            winsound.PlaySound("D:/Lógica e Linguagem de Pgm/Projeto de Conclusão/Músicas/Música de perder.wav", winsound.SND_ASYNC)
    if not -500/2 +10 < x < 500/2 -10 or not -500/2 +10 < y < 500/2-10:
        b.undo()

def left():
    b.left(5)
    
def right():
    b.right(5)
    
def sair():
    wn.bye()
    
#DENÁRIO
os.chdir("D:\\")
ce= turtle.Turtle()
wn.register_shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario\cenario.gif")
ce.shape("D:\Lógica e Linguagem de Pgm\Projeto de Conclusão\Cenario\cenario.gif")
ce.goto(0,0)


#DONVERSANDO DOM O USUÁRIO
answer = wn.textinput("Bem Vindo a Tortuga!", "Qual o nome da sua turtle?")

move()

#REDISTRANDO DUNÇÕES DAS TEDLAS
wn.onkeypress(fd,"Up")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(sair, "q")
wn.listen() # inicia os eventos
wn.mainloop() # começa a animação
