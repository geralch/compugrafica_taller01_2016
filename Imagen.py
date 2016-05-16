#Importar librerias
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy 
import random
from PIL import Image
import os


def InitGL(Width, Height):
	
	glClearColor(0.53,0.53,0.53,0.0)
	glMatrixMode(GL_PROJECTION)
	
	
def mostrarEscena():
	glClear(GL_COLOR_BUFFER_BIT)
	img = Image.open('logo.jpg')
	#img.show()
	os.system('/home/segus/Documentos/Grafica/compugrafica_taller01_2016/logo.jpg')
	img_data =numpy.array(list(img.getdata()), numpy.uint8)
	id = glGenTextures(1)
	glPixelStorei(GL_UNPACK_ALIGNMENT,1)
	glBindTexture(GL_TEXTURE_2D, id)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)	
	
	glutSwapBuffers();


	
def main():
	global window

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)

	window = glutCreateWindow('Imagen')

	glutDisplayFunc(mostrarEscena)
	glutIdleFunc(mostrarEscena)
	InitGL(500,500)
	glutMainLoop()


if __name__ == "__main__":
	main()
