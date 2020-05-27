try:
  from OpenGL.GL import *
  from OpenGL.GLU import *
  from OpenGL.GLUT import *
except Exception as e:
  raise Exception("Missing glut.dll as error was {}'.format(e))
