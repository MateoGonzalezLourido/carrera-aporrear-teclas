import turtle
import time

#variables globales
WINDOW_WIDTH=600#tamaño pantalla x
WINDOWS_HEIGHT=700#tamaño pantalla y
COLOR_FONDO='#fedaa1'
lista_jugadores=[]
lista_texto_posiciones_jugadores=[]
posicionesFinales=[]
DESPLAZAMIENTO=11#11
POSICION_META=WINDOWS_HEIGHT/2-50
COLORES_JUGADORES=['#C70039','#2471a3','#229954','#f39c12','#7d3c98']
TECLAS_JUGADORES=["q","h","p","z","Up"]
NOMBRES_JUGADORES=['Rojo','Azul','Verde','Naranja','Morado']
empezarCarrera=False
poderMoverse=False
#ventana
window = turtle.Screen()
window.title("Carrera Aporrear Teclas Python-By Mateo González")
window.setup(width=WINDOW_WIDTH, height=WINDOWS_HEIGHT)
window.bgcolor(COLOR_FONDO)

#meta
meta=turtle.Turtle()
meta.hideturtle()
meta.penup()
meta.color('white')
meta.pensize(4)
meta.goto(-WINDOW_WIDTH/2,POSICION_META)
meta.pendown()
meta.goto(WINDOW_WIDTH/2,POSICION_META)
#salida
salida=turtle.Turtle()
salida.hideturtle()
salida.penup()
salida.color('white')
salida.pensize(4)
salida.goto(-WINDOW_WIDTH/2,-POSICION_META)
salida.pendown()
salida.goto(WINDOW_WIDTH/2,-POSICION_META)

#texto meta
textMeta=turtle.Turtle()
textMeta.hideturtle()
textMeta.penup()
textMeta.color('black')
textMeta.goto(0,WINDOWS_HEIGHT/2-40)
textMeta.write('¡META!',align='center',font=('Impact',22))

#numero jugadores
numeroJugadores=int(turtle.textinput('Número de jugadores:','Rango 2-5'))
if numeroJugadores<2:
    numeroJugadores=2
elif numeroJugadores>5:
    numeroJugadores=5

#jugadores
for jugador in range(0,numeroJugadores):
    #jugador
    nuevo_jugador=turtle.Turtle()
    textMeta.hideturtle()
    nuevo_jugador.shape("square")
    nuevo_jugador.color(COLORES_JUGADORES[jugador])
    nuevo_jugador.pensize(3)
    nuevo_jugador.penup()
    width=((WINDOW_WIDTH/numeroJugadores)*(jugador)-((WINDOW_WIDTH/2)-40))
    nuevo_jugador.goto(width,-POSICION_META)
    nuevo_jugador.pendown()
    lista_jugadores.append(nuevo_jugador)
    #texto posicion
    nuevo_texto=turtle.Turtle()
    nuevo_texto.hideturtle()
    nuevo_texto.penup()
    nuevo_texto.color('black')
    lista_texto_posiciones_jugadores.append(nuevo_texto)

#HUD opciones
textOpciones=turtle.Turtle()
textOpciones.hideturtle()
textOpciones.penup()
textOpciones.color('black')
textOpciones.goto(0,0)
textOpciones.write('EMPEZAR (S) / AYUDA (J)',align='center',font=('Impact',23))
#HUD ayuda
textoAyuda=turtle.Turtle()
textoAyuda.hideturtle()
textoAyuda.penup()
textoAyuda.color(COLOR_FONDO)
textoAyuda.goto(0,-100)


#mostrar informacion
def mostrar_informacion():
    if not empezarCarrera:
        pencolorFondoComparar=(0.996078431372549, 0.8549019607843137, 0.6313725490196078)
        if textOpciones.pencolor()==pencolorFondoComparar:
            textOpciones.color('black')
            textoAyuda.color(COLOR_FONDO)
            textoAyuda.clear()
            textOpciones.write('EMPEZAR (S) / AYUDA (J)',align='center',font=('Impact',23))
        else:
            textOpciones.color(COLOR_FONDO)
            textoAyuda.color('black')
            textOpciones.clear()

            textoEscribir="Aporrea las teclas indicadas \npara mover el coche hasta la meta\ny ganar.\n\nTECLAS-JUGADORES:\n"
            for jugador in range(0,numeroJugadores):
                textoEscribir+=f"   {TECLAS_JUGADORES[jugador]} - {jugador+1}\n"
            textoAyuda.write(f'{textoEscribir}\n\nSALIR (j)',align='center',font=('Arial',16))
        
#empezar carrera
def empezar_carrera():
    global empezarCarrera
    if empezarCarrera==False:
        empezarCarrera=True
        textOpciones.clear()
        textoAyuda.clear()
        #temporizador
        textTemporizador=turtle.Turtle()
        textTemporizador.hideturtle()
        textTemporizador.penup()
        textTemporizador.color('black')
        textTemporizador.goto(0,0)
        textTemporizador.clear()
        textTemporizador.write(f'Empieza en\n3s',align='center',font=('Impact',22))
        time.sleep(1)
        textTemporizador.clear()
        textTemporizador.write(f'Empieza en\n2s',align='center',font=('Impact',22))
        time.sleep(1)
        textTemporizador.clear()
        textTemporizador.write(f'Empieza en\n1s',align='center',font=('Impact',22))
        time.sleep(1)
        textTemporizador.clear()
        textTemporizador.write(f'¡CORRER!',align='center',font=('Impact',25))
        time.sleep(1)
        textTemporizador.clear()
        global poderMoverse
        poderMoverse=True

#funciones movimientos
def mover_jugador(jugador):
    if poderMoverse:
        if jugador<=numeroJugadores-1:
            ox=lista_jugadores[jugador].xcor()
            oy=lista_jugadores[jugador].ycor()
            if oy<POSICION_META:
                oy+=DESPLAZAMIENTO
                lista_jugadores[jugador].goto(ox,oy)
                if oy>=POSICION_META:
                    posicionesFinales.append(jugador+1)
                    if len(posicionesFinales)>=numeroJugadores-1:
                        fin_carrera()

def fin_carrera():
    global poderMoverse
    poderMoverse=False
    #añadir a la clasificacion el jugador que no cruzo la meta
    if len(posicionesFinales)!=numeroJugadores:
        for i in range(1,numeroJugadores+1):
            try:
                posicionesFinales.index(i)
            except:
                posicionesFinales.append(i)
    for i in range(len(lista_jugadores)):
        lista_jugadores[i].speed(0)
        lista_jugadores[i].penup()
        lista_jugadores[i].goto(WINDOW_WIDTH+100,WINDOWS_HEIGHT+100)
    lista_jugadores.clear()
    lista_texto_posiciones_jugadores.clear()
    textMeta.clear()
    #mostrar clasificacion
    textClasic=turtle.Turtle()
    textClasic.hideturtle()
    textClasic.penup()
    textClasic.color('black')
    textClasic.goto(0,0)
    escribirTexto=""
    for pos in range(1,len(posicionesFinales)+1):
        escribirTexto+=f'   {pos}º- {NOMBRES_JUGADORES[posicionesFinales[pos-1]-1]}\n'
    textClasic.write(f'Clasificacion:\n{escribirTexto}',align='center',font=('Arial',16))
    
def actualizarPosicionesPantalla():
    #mostrar posicion encima del jugador oy+30
    oy=[]
    for jugador in range(len(lista_jugadores)):
        oy.append([jugador,POSICION_META-lista_jugadores[jugador].ycor()])
    oy=sorted(oy,key=lambda x:x[1])
    for i in range(len(oy)):
        if oy[i][1]>0:
            try:
                lista_texto_posiciones_jugadores[oy[i][0]].goto(lista_jugadores[oy[i][0]].xcor(),lista_jugadores[oy[i][0]].ycor()+25)
                lista_texto_posiciones_jugadores[oy[i][0]].clear()
                if oy!=POSICION_META:
                    lista_texto_posiciones_jugadores[oy[i][0]].write(i+1,align='center',font=('Impact',14))
                else:
                    lista_texto_posiciones_jugadores[oy[i][0]].write(posicionesFinales[oy[i][0]],align='center',font=('Impact',14))
            except:
                return 0

#movimientos teclado
window.listen()
window.onkeypress(None,"q")
window.onkeypress(None,"h")
window.onkeypress(None,"p")
window.onkeypress(None,"z")
window.onkeypress(None,"Up")
window.onkeyrelease(lambda:mover_jugador(0),"q")
window.onkeyrelease(lambda:mover_jugador(1),"h")
window.onkeyrelease(lambda:mover_jugador(2),"p")
window.onkeyrelease(lambda:mover_jugador(3),"z")
window.onkeyrelease(lambda:mover_jugador(4),"Up")
window.onkeypress(empezar_carrera,"s")
window.onkeypress(mostrar_informacion,"j")

#controlador/ejecutador programa
while True:
    window.update()#actualizar pantalla 
    if poderMoverse==True:
        actualizarPosicionesPantalla()
