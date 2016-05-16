# Geraldine Caicedo Hidalgo - 1527691
# Sebastian Salazar - 0938596
# Computacion Grafica
# Practica 01 - Mayo 2016
# Figuras - Cubo | Esfera

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import os
import threading
import random

caraA = [ 1.0, 1.0, -1.0, -1.0, 1.0,-1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
caraB = [ 1.0, -1.0, 1.0, -1.0,-1.0, 1.0, -1.0,-1.0,-1.0,1.0,-1.0, -1.0]
caraC = [ 1.0, 1.0, 1.0, -1.0, 1.0, 1.0, -1.0,-1.0, 1.0, 1.0,-1.0,  1.0]
caraD = [ 1.0,-1.0,-1.0, -1.0,-1.0,-1.0,-1.0, 1.0,-1.0, 1.0, 1.0,-1.0]
caraE = [-1.0, 1.0, 1.0, -1.0, 1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0, 1.0]
caraF = [1.0, 1.0,-1.0,1.0, 1.0, 1.0,1.0,-1.0, 1.0,1.0,-1.0,-1.0]
window = 0

#rotation
XCuadro = -0.5
YCuadro = -0.5
ZCuadro = -0.5
XEsfera = -0.5
YEsfera = -0.5
ZEsfera = -0.5

XScaCuadro = -1
YScaCuadro = -1
ZScaCuadro = -1
XScaEsfera = -1
YScaEsfera = -1
ZScaEsfera = -1

colorRE = 1
colorGE = 1
colorBE = 1

DIRECTION = 1


def InitGL(Width, Height):

    glClearColor(0.53,0.53,0.53,0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def mostrarEscena():
    global XCuadro,YCuadro,ZCuadro,XEsfera,YEsfera,ZEsfera
    global  XScaCuadro, YScaCuadro, ZScaCuadro, XScaEsfera, YScaEsfera, ZScaEsfera
    global colorRE, colorGE, colorBE
    global DIRECTION
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Cubo
    glLoadIdentity()
    xc = -0.3/2
    yc = -0.3/2
    glTranslatef(xc,yc,-6)
    glRotatef(XCuadro,0.5,0.0,0.0)
    glRotatef(YCuadro,0.0,0.5,0.0)
    glRotatef(ZCuadro,0.0,0.0,0.5)

	# Abajo
    glBegin(GL_QUADS)
    glVertex3f(caraA[0], caraA[1],  caraA[2])
    glVertex3f(caraA[3], caraA[4],  caraA[5])
    glVertex3f(caraA[6], caraA[7],  caraA[8])
    glVertex3f(caraA[9], caraA[10], caraA[11])
    glColor3f(0, 0, 0) # Azul
    glEnd()

	# Frente
    glBegin(GL_QUADS)
    glVertex3f(caraB[0], caraB[1],  caraB[2])
    glVertex3f(caraB[3], caraB[4],  caraB[5])
    glVertex3f(caraB[6], caraB[7],  caraB[8])
    glVertex3f(caraB[9], caraB[10], caraB[11])
    glColor3f(0, 1, 0) # Verde
    glEnd()

	# Atras
    glBegin(GL_QUADS)
    glVertex3f(caraC[0], caraC[1],  caraC[2])
    glVertex3f(caraC[3], caraC[4],  caraC[5])
    glVertex3f(caraC[6], caraC[7],  caraC[8])
    glVertex3f(caraC[9], caraC[10], caraC[11])
    glColor3f(0, 1, 1) # Cyan
    glEnd()

	# Izquierdo
    glBegin(GL_QUADS)
    glVertex3f(caraD[0], caraD[1],  caraD[2])
    glVertex3f(caraD[3], caraD[4],  caraD[5])
    glVertex3f(caraD[6], caraD[7],  caraD[8])
    glVertex3f(caraD[9], caraD[10], caraD[11])
    glColor3f(1, 0, 0) # Rojo
    glEnd()
    
	#  Derecha
    glBegin(GL_QUADS)
    glVertex3f(caraE[0], caraE[1],  caraE[2])
    glVertex3f(caraE[3], caraE[4],  caraE[5])
    glVertex3f(caraE[6], caraE[7],  caraE[8])
    glVertex3f(caraE[9], caraE[10], caraE[11])
    glColor3f(1,0, 1) #Rosado
    glEnd()

	# Arriba
    glBegin(GL_QUADS)
    glVertex3f(caraF[0], caraF[1],  caraF[2])
    glVertex3f(caraF[3], caraF[4],  caraF[5])
    glVertex3f(caraF[6], caraF[7],  caraF[8])
    glVertex3f(caraF[9], caraF[10], caraF[11])
    glColor3f(0, 0, 1) # 
    glEnd()

    # Esfera

    glLoadIdentity()
    xe = -0.4/2
    ye = -0.4/2
    glTranslatef(xe,ye,-2)
    glRotatef(XEsfera,0.5,0.0,0.0)
    glRotatef(YEsfera,0.0,0.5,0.0)
    glRotatef(ZEsfera,0.0,0.0,0.5)
    glScalef(XScaEsfera,YScaEsfera,ZScaEsfera)
    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, .7)
    XEsfera = XEsfera + 0.30
    ZEsfera = ZEsfera - 0.30
    glEnd()
    glutWireSphere(0.4,32,32);

    glutSwapBuffers()

def keyPressed(key,x,y):
	global XCuadro,YCuadro,ZCuadro
	global XScaEsfera, YScaEsfera, ZScaEsfera
	
	if(key[0]==114):
		XCuadro = XCuadro + 0.30
		YCuadro = YCuadro - 0.30
	if(key[0]==115):
		XScaEsfera = 0.8
		YScaEsfera = 0.8
		ZScaEsfera = 0.8
	if(key[0]==122):
		XScaEsfera = 1.2
		YScaEsfera = 1.2
		ZScaEsfera = 1.2

	glLoadIdentity()

def click(button,state,x,y):
	global colorRE, colorGE, colorBE
	global XCuadro,YCuadro,ZCuadro
	if (button==GLUT_LEFT_BUTTON and state==GLUT_UP):
		XCuadro = XCuadro + 0.30
		ZCuadro = ZCuadro - 0.30
	if (button==GLUT_RIGHT_BUTTON and state==GLUT_UP):
		print("click izq")


def main():

		global window

		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
		glutInitWindowSize(500,500)
		glutInitWindowPosition(200,200)

		window = glutCreateWindow('Cubo y Esfera')

		glutDisplayFunc(mostrarEscena)
		glutIdleFunc(mostrarEscena)
		glutKeyboardFunc(keyPressed)
		glutMouseFunc(click)
		print(
		"CaraA :" + str(caraA)+"\n"+
		"CaraB :" + str(caraB)+"\n"+
		"CaraC :" + str(caraC)+"\n"+
		"CaraD :" + str(caraD)+"\n"+
		"CaraE :" + str(caraE)+"\n"+
		"CaraF :" + str(caraF)+"\n"
		)
		InitGL(500,500)
		glutMainLoop()

if __name__ == "__main__":
        main()
