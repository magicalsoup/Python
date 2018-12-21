from graphics import *
import time
import random

win = GraphWin("Mushroom", 800, 600)

#colors
deepSkyBlue = color_rgb(0, 191, 255)
lawnGreen = color_rgb(124, 252, 0)
springGreen = color_rgb(0, 255, 127)
darkGreen = color_rgb(0, 100, 0)
fireBrick = color_rgb(178, 34, 34)
blueViolet = color_rgb(138, 43, 226)
darkGoldenrod = color_rgb(184, 134, 11)
darkSlateGray = color_rgb(49, 79, 79)
cyan = color_rgb(0, 255, 255)
tomato = color_rgb(255, 99, 71)
lightGoldenrod = color_rgb(238, 221, 130)
#ground
def build_ground(color):
        ground = Rectangle(Point(0, 400), Point(800, 600))
        ground.setFill(color)
        ground.draw(win)

#sky
def build_sky(color):
        sky = Rectangle(Point(0 , 0), Point(800, 400))
        sky.setFill(color)
        sky.draw(win)
def build_sun(color):
        sun = Circle(Point(750, 0), 100)
        sun.setFill(color)
        sun.draw(win)

#clouds
cloudpart1 = Circle(Point(50, 100), 30)
cloudpart2 = Circle(Point(80, 80), 30)
cloudpart3 = Circle(Point(110, 95), 30)
cloudpart4 = Circle(Point(80, 100), 30)
###
cloudpart5 = Circle(Point(750, 100), 30)
cloudpart6 = Circle(Point(720, 80), 30)
cloudpart7 = Circle(Point(690, 95), 30)
cloudpart8 = Circle(Point(720, 100), 30)

# clouds that move right
def draw_right_clouds(color):
        cloudpart1.setFill(color)
        cloudpart1.setOutline(color)
        cloudpart1.draw(win)
        
        cloudpart2.setFill(color)
        cloudpart2.setOutline(color)
        cloudpart2.draw(win)
        
        cloudpart3.setFill(color)
        cloudpart3.setOutline(color)
        cloudpart3.draw(win)
        
        cloudpart4.setFill(color)
        cloudpart4.setOutline(color)
        cloudpart4.draw(win)

# clouds that move left
def draw_left_clouds(color):
        cloudpart5.setFill(color)
        cloudpart5.setOutline(color)
        cloudpart5.draw(win)
        
        cloudpart6.setFill(color)
        cloudpart6.setOutline(color)
        cloudpart6.draw(win)
        
        cloudpart7.setFill(color)
        cloudpart7.setOutline(color)
        cloudpart7.draw(win)
        
        cloudpart8.setFill(color)
        cloudpart8.setOutline(color)
        cloudpart8.draw(win)

def move_clouds_right():
        cloudpart1.move(20, 0)
        cloudpart2.move(20, 0)
        cloudpart3.move(20, 0)
        cloudpart4.move(20, 0)

def move_clouds_left():
        cloudpart5.move(-20, 0)
        cloudpart6.move(-20, 0)
        cloudpart7.move(-20, 0)
        cloudpart8.move(-20, 0) 
#trees
def build_trees(color1, color2):
    tree1 = Polygon(Point(0, 400),Point(100, 400), Point(50, 250))
    tree2 = Polygon(Point(100, 400), Point(200, 400), Point(150, 250))
    tree3 = Polygon(Point(200, 400), Point(300, 400), Point(250, 250))
    tree4 = Polygon(Point(300, 400), Point(400, 400), Point(350, 250))
    tree5 = Polygon(Point(400, 400), Point(500, 400), Point(450, 250))
    tree6 = Polygon(Point(500, 400), Point(600, 400), Point(550, 250))
    tree7 = Polygon(Point(600, 400), Point(700, 400), Point(650, 250))
    tree8 = Polygon(Point(700, 400), Point(800, 400), Point(750, 250))
    
    for i in range(30):
        move_clouds_right()
        move_clouds_left()
        tree1.undraw()
        tree2.undraw()
        tree3.undraw()
        tree4.undraw()
        tree5.undraw()
        tree6.undraw()
        tree7.undraw()
        tree8.undraw()
        if i %2 == 1:
            tree1.setFill(color1)
            tree2.setFill(color2)   
            
            tree3.setFill(color1)
            tree4.setFill(color2)
            
            tree5.setFill(color1)
            tree6.setFill(color2)
            
            tree7.setFill(color1)
            tree8.setFill(color2)
        else:
            tree1.setFill(color2)
            tree2.setFill(color1)
            
            tree3.setFill(color2)
            tree4.setFill(color1)
            
            tree5.setFill(color2)
            tree6.setFill(color1)
            
            tree7.setFill(color2)
            tree8.setFill(color1)
            
        tree1.draw(win)
        tree2.draw(win)
        tree3.draw(win)
        tree4.draw(win)
        tree5.draw(win)
        tree6.draw(win)
        tree7.draw(win)
        tree8.draw(win)
        time.sleep(0.2)


def build_tall_trees(color):
        tallTree1 = Polygon(Point(50, 400), Point(150, 400), Point(100,200))
        temp = tallTree1.clone()
        moveX = 0
        for i in range(8):
                temp.setFill(color)
                temp.draw(win)
                temp = tallTree1.clone()
                temp.move(moveX,0)
                moveX += 100
        
        
#head
def build_head(color):     
    head = Oval(Point(225, 180), Point(575, 425))
    head.setFill(color)
    head.draw(win)

#spots
def add_spots(color):
    spot1 = Circle(Point(400, 300), 60)
    spot2 = Circle(Point(265, 300), 40)
    spot3 = Circle(Point(535, 300), 40)

    spot1.setFill(color)
    spot1.setOutline(color)
    spot1.draw(win)
    spot2.setFill(color)
    spot2.setOutline(color)
    spot2.draw(win)
    spot3.setFill(color)
    spot3.setOutline(color)
    spot3.draw(win)

#bottom
def build_bottom(color):
    bottom = Rectangle(Point(300, 370), Point(500, 470))
    bottom.setFill(color)
    bottom.draw(win)

#eyes
def add_eyes(color):
    rightEye = Oval(Point(340,395), Point(360, 430))
    rightEye.setFill(color)
    rightEye.draw(win)

    leftEye = Oval(Point(440, 395), Point(460, 430))
    leftEye.setFill(color)
    leftEye.draw(win)

#Text
def add_text(x, y, text):
    message = Text(Point(x, y), text)
    message.draw(win)

#add crown
def add_crown(color1):
        crownbase = Rectangle(Point(370, 20), Point(430, 60))
        crownbase.setFill(color1)
        crownbase.draw(win)
        crownhead = Polygon(Point(370, 20), Point(430, 20), Point(400, 0))
        crownhead.setFill(color1)
        crownhead.draw(win)
        for i in range(15):
                time.sleep(0.02)
                crownbase.move(0, 10)
                crownhead.move(0, 10)
#build grass
def build_grass(color1, color2):
        for i in range (20):
                randx = random.randint(0, 795) 
                randy = random.randint(385, 595)
                grass = Circle(Point(randx, randy), 5)
                randcolor = random.randint(1, 2)
                if randcolor == 1:
                        grass.setFill(color1)
                        grass.setOutline(color1)
                else:
                        grass.setFill(color2)
                        grass.setOutline(color2)
                grass.draw(win)
#build fireworks
def build_fireworks(startx, starty, color):
        firework_start = Circle(Point(startx, starty), 10)
        firework_start.setOutline(color)
        firework_start.setFill(color)
        firework_start.draw(win)
        for i in range(70):
                time.sleep(0.015)
                firework_start.move(0, -5)

        a2 = firework_start.clone()
        a3 = firework_start.clone()
        a4 = firework_start.clone()

        a2.draw(win)
        a3.draw(win)
        a4.draw(win)
        for i in range(60):
                time.sleep(0.015)
                firework_start.move(0, -5)
                a2.move(5, 0)
                a3.move(0, 5)
                a4.move(-5, 0)
        firework_start.undraw()
        a2.undraw()
        a3.undraw()
        a4.undraw()

def build_castle(color1, color2, color3):
        background = Rectangle(Point(0, 400), Point(800, 200))
        background.setFill(darkGreen)
        background.draw(win)
        castlepart1 = Rectangle(Point(200, 275), Point(600, 400))
        castlepart1.setFill(color1)
        castlepart1.draw(win)
        castlepart2 = Rectangle(Point(275, 200), Point(525, 275))
        castlepart2.setFill(color2)
        castlepart2.draw(win)
        castlepart3 = Rectangle(Point(325, 150), Point(475, 275))
        castlepart3.setFill(color1)
        castlepart3.draw(win)
        castletop1 = Polygon(Point(325, 150), Point(475, 150), Point(400, 50))
        castletop1.setFill(color2)
        castletop1.draw(win)
        castleside1 = Polygon(Point(100, 400), Point(200, 400), Point(200, 275))
        castleside1.setFill(color2)
        castleside1.draw(win)
        castleside2 = Polygon(Point(700, 400), Point(600, 400), Point(600, 275))
        castleside2.setFill(color2)
        castleside2.draw(win)
        castledoor = Rectangle(Point(380, 325), Point(430, 400))
        castledoor.setFill('black')
        castledoor.draw(win)
        
        
def build_window1():
        build_ground(lawnGreen)
        build_sky(deepSkyBlue)
        build_sun('yellow')
        build_grass('red', 'white')
        draw_right_clouds('white')
        draw_left_clouds('white')
        build_tall_trees('black')
        build_trees(springGreen, darkGreen)
        build_head('red')
        add_spots('white')
        build_bottom('white')
        add_eyes('black')
        add_text(380, 440, "Hi, my names Bob")
def build_window2():
        build_ground(fireBrick)
        build_sky(blueViolet)
        build_sun('red')
        draw_right_clouds(tomato)
        draw_left_clouds(tomato)
        build_trees(darkSlateGray,darkGoldenrod)
        build_head(cyan)
        build_bottom('white')
        add_spots('black')
        add_eyes('red')
        add_text(380, 440, "I WILL KILL YOU!")


def build_window3():
        build_ground(lawnGreen)
        build_sky(deepSkyBlue)
        build_sun('yellow')
        build_castle('gold','lightGoldenrod','white')
        build_fireworks(200, 400, 'red')
        build_fireworks(600, 400, 'yellow')
        build_fireworks(300, 400, 'pink')
        build_fireworks(400, 400, blueViolet)
        draw_right_clouds('white')
        draw_left_clouds('white')
        build_head('gold')
        build_bottom('white')
        add_spots('yellow')
        add_eyes('black')
        add_crown(lightGoldenrod)
        add_text(380, 440, "Hello, Im king Bob")

def setup():

        window1 = Rectangle(Point(0, 0), Point(100, 100))
        windowtext = add_text(50, 50, "Button 1")
        window1.draw(win)
        window2 = Rectangle(Point(100, 0), Point(200, 100))
        windowtext2 = add_text(150, 50, "Button 2")
        window2.draw(win)
        window3 = Rectangle(Point(200, 0), Point(300, 100))
        windowtext3 = add_text(250, 50, "Button 3")
        window3.draw(win)
        

def main():
        setup()
        mousex = win.getMouse().getX()
        mousey = win.getMouse().getY()
        if mousex <= 100 and mousey <= 100:
                build_window1()
        elif mousex <= 200 and mousey <= 100: 
                build_window2()
        elif mousex <= 300 and mousey <= 100:
                build_window3()
        else:
                add_text(400, 400, "Please Click A Button")

                
        while True:
                print("running")
                mousex = win.getMouse().getX()
                mousey = win.getMouse().getY()

                if mousex <= 100 and mousey <= 100:
                        build_window1()
                        break
                elif mousex <= 200 and mousey <= 100: 
                        build_window2()
                        break
                elif mousex <= 300 and mousey <= 100:
                        build_window3()
                        break
                else:
                        add_text(400, 400, "Please Click A Button")
                        break;

main()
