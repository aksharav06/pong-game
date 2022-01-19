#Name: Akshara Vaghela, ID: 709973
#Date: January 14, 2022
#Description: In this program, you will play the single-player pong game
#that has 3 versions (beginner, regular, challenging) to choose. Using the left
#and right arrow keys manuevering the paddle, keep the ball up in play.

#import libraries
from tkinter import*
from tkinter import messagebox
import random
import time
 
    
# Instructions for the game
user_name = input("Please enter your name: ")
def clicked():
    messagebox.showinfo('Pong Instructions', 'Hello ' + user_name + "! The rules "\
                        +"of this game are very simple. Keep the ball in the air "\
                        +"by using your left and right arrow keys to move and hit "\
                        +"the ball with the paddle. To replay game, close the tab "\
                        +"and press on the game button on the home screen. Enjoy!")
    
#Using Tkinter to create the homescreen/window for the pong game
window = Tk()
window.title("The Pong Game by AV 709973")
window.geometry('600x500')
window.configure(bg="light blue")

#button allows for the instruction(message box) to be accessible through home-
#-screen/main window
btn = Button(window,text='Instructions', command=clicked)
btn.grid(row=0, column = 0)

#Image is the title of the game
img1 = PhotoImage(file='C:/Users/foram/Downloads/Comp Sci Final - Pong Game - 709973/pong_title.png', width = 300, height=300)
lbl = Label(window, image = img1)
lbl.grid(row=2, column=2)
lbl.place(x=140,y=30)


#This section's code outputs the beginner-friendly version of the pong game where
# the ball is at a slightly slower then moderate speed.

def open():
    class ball: #blueprint for the object "ball"
        def __init__ (self, canvas, paddle,size):
            self.canvas = canvas
            self.paddle = paddle
            self.id = canvas.create_rectangle(11,11,size,size, fill="white")
            self.canvas.move(self.id, 230,230)
            self.x = random.randrange(-2,2)
            self.y = -1
            self.touch_bottom = False
            self.score = 0
            
        # creates the bouncing motion of the ball
        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 2
                
            elif pos[1] <= 0:
                self.y = 2
                
            elif pos [2] >= 500:
                self.x = -2
                
            elif pos [3] >= 500:
                self.touch_bottom = True
                canvas.create_text(250,200,text="GAME OVER",font=("Arial",30))
                go_label = canvas.create_text(250,290,text= user_name+ ", your score is " +str(ball.score))
                if ball.score >= 5:
                    canvas.create_text(250,330,text="YOU WIN :)", font=("Arial",15))
                else:
                    canvas.create_text(250,330,text="YOU LOSE :( Try Again", font=("Arial",15))
                #when the ball's y-position is equal to or beyond 500, the game
                #ends, hence the text "GAME OVER" and the player's score shows up
                #on the screen
                
            #everytime the ball comes in contact with the paddle, the score increases
            if self.touch_gamePaddle(pos) == True:
                self.x = random.randrange(-2,2)
                self.y = -2
                self.score += 1
        
        # defines when function "touch_paddle" is true using the posi
        #-tion of the paddle and the position of the ball
        def touch_gamePaddle(self, pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    return True
                
    #blueprint for the object "paddle"
    class Paddle:
        def __init__(self, canvas):
            self.canvas = canvas
            self.id = canvas.create_rectangle(0,0, 90, 20, fill="white")
            self.canvas.move(self.id, 230, 380)
            self.x = 0
            self.canvas.bind_all('<KeyPress-Left>', self.left)
            self.canvas.bind_all('<KeyPress-Right>', self.right)
            
        #creates the paddle's motion
        def draw(self):
            self.canvas.move(self.id, self.x, 0)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 0
            if pos[2] >= 500:
                self.x = 0
                
        #sets the speed of the paddle
        def left(self,evt):
            self.x = -2
        def right(self,evt):
            self.x = 2
                
    #code creates the pong-beginner version window + displays all the objects in
    #the window as well
    game = Toplevel()
    game.title("Level: Easy")
    game.geometry('500x500')
    game.configure(bg="black")
    canvas = Canvas(game, width=500, height=500, bg='light blue')
    canvas.pack()
    label = canvas.create_text(4, 4, anchor=NW, text="Score: 0")
    paddle = Paddle(canvas)
    ball = ball(canvas,paddle,30)
    
    #objects and functions continue updating as long as the game is still in play
    #(ball hasn't touched the ground)
    while ball.touch_bottom == False:
        ball.draw()
        paddle.draw()
        canvas.itemconfig(label, text="Score: "+str(ball.score))#everytime ball
        #makes contact with the paddle, score increases
        game.update()
        time.sleep(0.001)#suspends the game's exectution for 0.001 seconds

#attaches the homescreen to the beginner version pong screen
btn = Button(window, text="Easy", command=open)
btn.place(x=130,y=350)

#Outputs the regular version of pong. This code is exactly the same as the
#beginner version however the speed of the ball is increased by 1 to make the
#speed of the ball moderate and little challenging in comparison to the beginner
#version
def open():
    class ball: 
        def __init__ (self, canvas, paddle, size):
            self.canvas = canvas
            self.paddle = paddle
            self.id = canvas.create_rectangle(11,11,size,size, fill="white")
            self.canvas.move(self.id, 230,230)
            self.x = random.randrange(-3,3)
            self.y = -1
            self.touch_bottom = False
            self.score = 0
            
        #outputs the motion of the ball; speed of the ball increased from 2 to 3
        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 3
                
            elif pos[1] <= 0:
                self.y = 3
                
            elif pos [2] >= 500:
                self.x = -3
                
            elif pos [3] >= 500:
                self.touch_bottom = True
                canvas.create_text(250,250,text="GAME OVER",font=("Arial",25))
                go_label = canvas.create_text(250,300,text= user_name + ", your score is " +str(ball.score))
                if ball.score >= 10:
                    canvas.create_text(250,330,text="YOU WIN :)", font=("Arial",15))
                else:
                    canvas.create_text(250,330,text="YOU LOSE :( Try Again", font=("Arial",15))
                
            
            if self.touch_gamePaddle(pos) == True:
                self.x = random.randrange(-3,3)
                self.y = -3
                self.score += 1
                
        def touch_gamePaddle(self, pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    return True
                
            
    class Paddle:
        def __init__(self, canvas):
            self.canvas = canvas
            self.id = canvas.create_rectangle(0,0, 100, 10, fill="white")
            self.canvas.move(self.id, 230, 380)
            self.x = 0
            self.canvas.bind_all('<KeyPress-Left>', self.left)
            self.canvas.bind_all('<KeyPress-Right>', self.right)

        def draw(self):
            self.canvas.move(self.id, self.x, 0)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 0
            if pos[2] >= 500:
                self.x = 0

        def left(self, evt):
            self.x = -2
        def right(self, evt):
            self.x = 2
            
    #code creates the pong-regular version window + displays all the objects in
    #the window as well            
    game_med = Toplevel()
    game_med.title("Level: Medium")
    game_med.geometry('500x500')
    game_med.configure(bg="black")
    canvas = Canvas(game_med, width=500, height=500, bg='light blue')
    canvas.pack()
    label = canvas.create_text(4, 4, anchor=NW, text="Score: 0")
    paddle = Paddle(canvas)
    ball = ball(canvas, paddle, 30)
    
    
    
    while ball.touch_bottom == False:
        ball.draw()
        paddle.draw()
        canvas.itemconfig(label, text="Score: "+str(ball.score)) 
        game_med.update()
        time.sleep(0.001)

# button attaches the pong-regular version window to the homescreen window
btn = Button(window, text="Medium", command=open)
btn.place(x=225, y=350)

#Outputs a challenging version of the pong game. The code is exactly the same as
#the previous two however with one change. The speed of the ball in this version
#is increased by 2 when comparing to the beginner version, hence it's more
#challenging then the other two versions

def open():
    class ball:
        def __init__ (self, canvas, paddle, size):
            self.canvas = canvas
            self.paddle = paddle
            self.id = canvas.create_rectangle(11,11,size,size, fill="white")
            self.canvas.move(self.id, 230,230)
            self.x = random.randrange(-4,4)
            self.y = -1
            self.touch_bottom = False
            self.score = 0
        
        #outputs the motion of the ball; speed of the ball increased from 2 to 4
        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 4
                
            elif pos[1] <= 0:
                self.y = 4
                
            elif pos [2] >= 500:
                self.x = -4
                
            elif pos [3] >= 500:
                self.touch_bottom = True
                canvas.create_text(250,250,text="GAME OVER",font=("Arial",25))
                go_label = canvas.create_text(250,290,text = user_name + ", your score is " +str(ball.score))
                if ball.score >= 10:
                    canvas.create_text(250,330,text="YOU WIN :)", font=("Arial",15))
                else:
                    canvas.create_text(250,330,text="YOU LOSE :( Try Again", font=("Arial",15))
            
            if self.touch_gamePaddle(pos) == True:
                self.x = random.randrange(-4,4)
                self.y = -4
                self.score += 1
                
        def touch_gamePaddle(self, pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    return True
                
            
    class Paddle:
        def __init__(self, canvas):
            self.canvas = canvas           
            self.id = canvas.create_rectangle(0,0, 100, 10, fill="white")
            self.canvas.move(self.id, 230, 380)
            self.x = 0
            self.canvas.bind_all('<KeyPress-Left>', self.left)
            self.canvas.bind_all('<KeyPress-Right>', self.right)

        def draw(self):
            self.canvas.move(self.id, self.x, 0)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 0
            if pos[2] >= 500:
                self.x = 0

        def left(self, evt):
            self.x = -2
        def right(self, evt):
            self.x = 2
            
    #code creates the pong-challenging version window + displays all the objects 
    #in the window as well
    game_hard = Toplevel()
    game_hard.title("Level: Hard")
    game_hard.geometry('500x500')
    game_hard.configure()
    canvas = Canvas(game_hard, width=500, height=500, bg='light blue')
    canvas.pack()
    label = canvas.create_text(4, 4, anchor=NW, text="Score: 0")
    paddle = Paddle(canvas)    
    ball = ball(canvas, paddle, 30)

    while ball.touch_bottom == False:
        ball.draw()
        paddle.draw()
        canvas.itemconfig(label, text="Score: "+str(ball.score))
        game_hard.update()
        time.sleep(0.001)

#button attaches the pong-challenging version window to the homescreen window
btn = Button(window, text="Hard", command=open)
btn.place(x=350,y=350)

#displays all the windows and functions
window.mainloop()
