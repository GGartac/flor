from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0, -40)

# Dibujar la flor en espiral con pétalos
for i in range(16):
    for j in range(18):
        color('#FFA216')  # Color de los pétalos
        right(90)
        circle(150 - j * 6, 90)
    
        left(90)
        circle(150 - j * 6, 90)
        right(180)
    circle(40, 24)

# Dibujar centro de la flor con "sellos" en espiral dorada
color('black')
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')  # Color del centro (marrón)

golden_ang = 137.508  # Ángulo de espiral dorada
phi = golden_ang * (pi / 180)

for i in range(140):
    r = 4 * sqrt(i)  # Radio para la espiral
    theta = i * phi  # Ángulo en espiral
    x = r * cos(theta)  # Coordenada X
    y = r * sin(theta)  # Coordenada Y
    penup()
    goto(x, y)
    setheading(i * golden_ang)  # Dirección de la tortuga
    pendown()
    stamp()  # Estampa el centro


penup()

# Crear la sombra del texto para efecto 3D
goto(3, -23)  # Desplazamiento para la sombra
color('gray')
write(" ", align="center", font=("Arial", 24, "bold"))

# Escribir el texto principal encima de la sombra
goto(0, -20)
color('white')
write("  ", align="center", font=("Arial", 24, "bold"))

hideturtle()
done()
