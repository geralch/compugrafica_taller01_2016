# Taller 01 | Computacion Grafica
* AUTORES : geralch - segus3088
* ARCHIVOS : Figuras.py - Imagen.py - Modelos.py
* Semestre 01 de 2016

1. FIGURAS A GENERAR 
  En el misma ventana genere las siguiente figuras
  1. Genere un cubo con L = 0,3 centrado en el punto (−0,5, −0,5, −0,5). Los colores de las caras deben ser diferentes.
  2. Genere una esfera con r = 0,4 centrada en el punto (0,4, 0,4, 0,4). La esfera debe tener un color de su elección (Excepto azul (0,0,1))
  
  1.1. Operaciones sobre las figuras
  Sobre las figuras generadas en el punto anterior crear la siguientes operaciones:
    1. Cada vez que se presiona la tecla r el cubo rota 30 con respecto al vector (1, 1, 0).
    2. Cada vez que se presiona la tecla s la esfera se escala en un factor en x,y y z de 0,8.
    3. Cada vez que se presiona la tecla z la esfera es escala en un factor en x,y y z de 1,2.
    4. Usando la función glutMouseFunc 1 genere los siguientes eventos:
      1. Cada vez que hace clic izquierdo en el área inicial del cubo, este debe escalar en x,y y z con un factor de 1,3
      2. Cada vez que hace clic derecho en el área inicial del cubo, este debe escalar en x,y y z con un factor de 0,7
      3. Cada vez que hace clic izquierdo en el área de la esfera, esta cambia a color azul (0,0,1)
      4. Cada vez que hace clic derecho en el área de la esfera, esta recupera el color que usted especificó.
      
2.  CARGAR UNA IMAGEN Y OBJETOS 3D

  1. Busque una imagen en la Internet, carguela utilizando la librerı́a en OpenGL y muestre en la pantalla. Pista: Texturas.
  2. Investigue como cargar modelos 3D en OpenGL,cargue al menos 3 de ellos y aplique las operaciones de proyección y transformación que considere pertinentes para una correcta visualización. Existen varias paginas donde puede descargar modelos 3D, como es el caso de Turbosquid, página con modelos 3D de imágenes, existen imágenes gratuitas y de pago: TurboSquid: 3D MODELS FOR PROFESSIONALS. Los archivos recomendados a buscar son los .OBJ que se pueden cargar openGL.
