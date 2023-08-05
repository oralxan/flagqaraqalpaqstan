from turtle import *

title('Qaraqalpaqstan')
my_screen = Screen()
my_screen.setup(1000,600)


qq=Turtle()
qq.speed(15)
def center_mark():
    qq.pu()
    qq.left(180)
    qq.forward(500)
    


center_mark()
qq.right(90)
qq.forward(100)
qq.right(90)

qq.pd()
qq.fillcolor('#0077be')
qq.begin_fill()
qq.forward(1000)
qq.left(90)
qq.forward(200)
qq.left(90)
qq.forward(1000)
qq.left(90)
qq.forward(200)
qq.end_fill()

qq1 = Turtle()

qq1.pu()
qq1.left(180)
qq1.forward(500)
qq1.right(90)
qq1.forward(95)
qq1.right(90)

#sdfghjkl
qq1.pd()
qq1.fillcolor('#f9c00c')
qq1.begin_fill()
qq1.forward(1000)
qq1.right(90)
qq1.forward(200)
qq1.right(90)
qq1.forward(1000)
qq1.right(90)
qq1.forward(200)
qq1.end_fill()





qq1.pd()
qq1.fillcolor('#e60000')
qq1.right(90)
qq1.begin_fill()
qq1.width(10)
qq1.color('#e60000')
qq1.forward(1000)
qq1.end_fill()



qq3 = Turtle()
def center_mark():
    qq3.pu()
    qq3.left(180)
    qq3.forward(500)


center_mark()
qq3.left(90)
qq3.forward(100)
qq3.left(90)

qq3.pd()
qq3.fillcolor('#66ff33')
qq3.begin_fill()
qq3.forward(1000)
qq3.right(90)
qq3.forward(200)
qq3.right(90)
qq3.forward(1000)
qq3.right(90)
qq3.forward(200)
qq3.end_fill()


qq2 = Turtle()
qq2.pu()

qq2.left(180)
qq2.forward(500)
qq2.left(90)
qq2.forward(100)
qq2.left(90)

qq2.pd()
qq2.fillcolor('#e60000')
qq2.begin_fill()
qq2.width(10)
qq2.color('#e60000')
qq2.forward(1000)
qq2.end_fill()


qq.color('white')
qq.write(f"\n☾",align='left',font=('white',150,'normal'))
qq.color('white')
qq.write(f"""                             ☆ ☆\n\n\n
""", font=("White",20, "bold"))
qq.write(f"""\n
                          ☆ ☆ ☆\n\n
""", font=("White",20, "bold"))


qq4 = Turtle()
qq4.begin_fill()
qq4.end_fill()
my_screen.exitonclick()

