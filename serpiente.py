import turtle
import time
import random

retraso=0.01
marcador=0
marcador_alto=0

#Creando la pantalla

s = turtle.Screen()
s.setup(650,650) #Configurar #pixeles de la pantalla
s.bgcolor("lightgray")
s.title("Juego de la serpiente")

#Creando la serpiente

serpiente=turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction="stop"
serpiente.color("green")

cuerpo=[]

#Creando la comida
comida=turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0,100)
comida.speed(0)

texto=turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,-260)
texto.write("Marcador: 0 \t Marcador más alto: 0 ", align="center", font=("verdana",24,"normal"))

#Agregando movimiento a la serpiente

def arriba():
    serpiente.direction ="up"

def abajo():
    serpiente.direction ="down"

def izquierda():
    serpiente.direction ="left"
    
def derecha():
    serpiente.direction ="right"

def movimiento():
    if serpiente.direction== "up":
        y=serpiente.ycor()
        serpiente.sety(y+20)
    if serpiente.direction== "down":
        y=serpiente.ycor()
        serpiente.sety(y-20)
    if serpiente.direction== "right":
        x=serpiente.xcor()
        serpiente.setx(x+20)
    if serpiente.direction== "left":
        x=serpiente.xcor()
        serpiente.setx(x-20)

s.listen() # pone en escucha la pantalla (reaccionando a las teclas)
s.onkeypress(arriba,"Up")
s.onkeypress(abajo,"Down")
s.onkeypress(izquierda,"Left")
s.onkeypress(derecha,"Right")



while True:
    s.update() #Actualizar la pantalla
    
    if serpiente.xcor()>300 or serpiente.xcor()<-300 or serpiente.ycor()>300 or serpiente.ycor()<-300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction="stop"
        cuerpo.clear()
        marcador=0
        texto.clear()
        texto.write("Marcador: {} \t Marcador más alto: {} ".format(marcador, marcador_alto), align="center", font=("verdana",24,"normal"))
        
    
    
    if serpiente.distance(comida)<=20:
        x=random.randint(-250,250)
        y=random.randint(-250,250)
        comida.goto(x,y)
        
        #crear nuevo cuerpo al llegar a tocar la comida
        nuevo_cuerpo=turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)
        
        marcador+=10
        if marcador>=marcador_alto:
            marcador_alto=marcador
        texto.clear()
        texto.write("Marcador: {} \t Marcador más alto: {} ".format(marcador, marcador_alto), align="center", font=("verdana",24,"normal"))
        
    total=len(cuerpo)
    for i in range(total-1,0,-1):
        x=cuerpo[i-1].xcor()
        y=cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)
    if total>0:
        x=serpiente.xcor()
        y=serpiente.ycor()
        cuerpo[0].goto(x,y)
        
    movimiento()
    
    for i in cuerpo:
        if i.distance(serpiente)<20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            serpiente.direction="stop"
            cuerpo.clear()
            marcador=0
            texto.clear()
            texto.write("Marcador: {} \t Marcador más alto: {} ".format(marcador, marcador_alto), align="center", font=("verdana",24,"normal"))
        
    
    
    time.sleep(retraso)


turtle.done()
