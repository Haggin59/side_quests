import cv2
from turtle import Turtle,Screen
import numpy

img = cv2.imread("rdj.jpeg")            #Reading the image
img = cv2.resize(img,(50,50))        #Resizing to 50x50 Px

size = img.shape

t1 = Turtle()                        
scr = Screen()                       
scr.colormode(255)

x = 0
y = 0
arr = numpy.asarray(img)             #Converting image to numpy array
t1.speed(0)

for i in range(size[0]):             
    t1.penup()
    t1.setpos(x,y)                   #shifting to new row
    t1.pendown()
    for j in range(size[1]):         
    
        t1.dot(5,arr[i][j])          #Completing i-th row
        t1.penup()
        t1.forward(5)
        t1.pendown()
    
    y = y-5                          #decrementing y-cordinate


scr.exitonclick()