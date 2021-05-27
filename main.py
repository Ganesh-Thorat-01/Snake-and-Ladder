'''
env python3
Created on Thu May 27 2021
@author: Ganesh Thorat
-*-coding: utf-8 -*-

*Tip - To execute this program you should install pygame and pillow module in your machine.
        You can install it by following command in terminal "pip install pygame","pip install pillow" resp.
'''


import tkinter as tk
import random
from PIL import Image,ImageTk
from tkinter import messagebox
import pygame

player1_pos=0
player2_pos=0
play_round=0
pygame.init()
def main():
    global player1_pos,player2_pos,play_round

    board_frame=tk.Frame(screen,bd=2,width=505,height=505)
    board_frame.rowconfigure(10, {'minsize': 50})
    board_frame.columnconfigure(10, {'minsize': 50})
    board_frame.place(x=0,y=0)

    board_lab=tk.Label(board_frame,image=board_img)
    board_lab.place(x=0,y=0)

    player1_lab=tk.Label(board_frame,image=player[0])
    player1_lab.place(x=board_pos[player1_pos][0],y=board_pos[player1_pos][1])

    player2_lab=tk.Label(board_frame,image=player[1])
    player2_lab.place(x=board_pos[player2_pos][0],y=board_pos[player2_pos][1])

    extra_frame=tk.Frame(screen,bd=2,width=200,height=505,bg="white")
    extra_frame.place(x=505,y=0)


    player_lab=tk.Label(extra_frame,text="Player 1\n VS\nPlayer 2",bg="white",fg="red",font=("arial bold",25))
    player_lab.place(x=10,y=70)

    play1_lab=tk.Label(extra_frame,image=player[0],bg="white")
    play1_lab.place(x=150,y=74)

    play2_lab=tk.Label(extra_frame,image=player[1],bg="white")
    play2_lab.place(x=150,y=153)

    roll_dice_but=tk.Button(extra_frame,image=DiceImage,bd=1,activebackground="white",bg="white",relief="solid",command=lambda:move())
    roll_dice_but.place(x=55,y=250)

    restart_but=tk.Button(extra_frame,text="Restart",font=("arial bold",18),width=12,bd=1,fg="blue",activebackground="white",bg="white",relief="solid",command=lambda:restart())
    restart_but.place(x=1,y=400)

    exit_but=tk.Button(extra_frame,text="Exit",font=("arial bold",18),width=12,bd=1,fg="blue",activebackground="white",bg="white",relief="solid",command=lambda:exit())
    exit_but.place(x=1,y=450)


    def move():
        global play_round,player1_pos,player2_pos
        if play_round==0:
            count=random.choice([1,2,3,4,5,6])
            DiceImage=dice_arr[count-1]
            dice_sound.play()
            roll_dice_but.config(image=DiceImage)
            play_round=1   
            if player1_pos<=99:
                if board_pos[player1_pos][2]==-1 :
                    player1_pos=player1_pos+count
                    if player1_pos<=99:
                        player1_lab.place(x=board_pos[player1_pos][0],y=board_pos[player1_pos][1])
                    else:
                        player1_pos-=count

            if player1_pos<=99 :
                if board_pos[player1_pos][2]>=0 :
                    player1_pos=board_pos[player1_pos][2]
                      

                    if player1_pos<=99:
                        player1_lab.place(x=board_pos[player1_pos][0],y=board_pos[player1_pos][1])

                if player1_pos==99:
                    victory_sound.play()
                    messagebox.showinfo("Win"+"🥂","Congratulations!! Player 1 win the match")
                    restart()
                return     
        
        elif play_round==1:
            count=random.choice([1,2,3,4,5,6])
            DiceImage=dice_arr[count-1] 
            dice_sound.play()
            roll_dice_but.config(image=DiceImage)
            play_round=0
            if player2_pos<=99:
                if board_pos[player2_pos][2]==-1 :
                    player2_pos+=count
                    if player2_pos<=99:
                        player2_lab.place(x=board_pos[player2_pos][0],y=board_pos[player2_pos][1])
                    else:
                        player2_pos-=count
            if player2_pos<=99:
                if board_pos[player2_pos][2]>=0 :
                    player2_pos=board_pos[player2_pos][2]
                    if player2_pos<=99:
                        player2_lab.place(x=board_pos[player2_pos][0],y=board_pos[player2_pos][1])
                if player2_pos==99:
                    victory_sound.play()
                    messagebox.showinfo("Win"+"🥂","Congratulations!! Player 2 win the match")
                    restart()
        else:
            pass

def restart():
    msg=messagebox.askokcancel("Restart","Do you want to restart?")
    if msg==True:
        global player1_pos,player2_pos,play_round
        player1_pos=0
        player2_pos=0
        play_round=0
        main()


def exit():
    msg=messagebox.askokcancel("Exit","Do you really want to Exit?")
    if msg==True:
        screen.destroy()

if __name__=="__main__":
    screen=tk.Tk()
    screen.geometry("700x505")
    screen.minsize(700,505)
    screen.maxsize(700,505)
    screen.title("Snake and Ladder")
    screen.config(bg="white")
    screen.iconbitmap("Resources\Images\snake.ico")

    board_img=Image.open("Resources\Images\Board.jpg")
    board_img=board_img.resize((500,500))
    board_img=ImageTk.PhotoImage(board_img)

    dice1=Image.open("Resources\Images\dice1.png")
    dice1=dice1.resize((80,80))
    dice1=ImageTk.PhotoImage(dice1)

    dice2=Image.open("Resources\Images\dice2.png")
    dice2=dice2.resize((80,80))
    dice2=ImageTk.PhotoImage(dice2)

    dice3=Image.open("Resources\Images\dice3.png")
    dice3=dice3.resize((80,80))
    dice3=ImageTk.PhotoImage(dice3)

    dice4=Image.open("Resources\Images\dice4.png")
    dice4=dice4.resize((80,80))
    dice4=ImageTk.PhotoImage(dice4)

    dice5=Image.open("Resources\Images\dice5.png")
    dice5=dice5.resize((80,80))
    dice5=ImageTk.PhotoImage(dice5)

    dice6=Image.open("Resources\Images\dice6.png")
    dice6=dice6.resize((80,80))
    dice6=ImageTk.PhotoImage(dice6)

    player1=Image.open("Resources\Images\player1.png")
    player1=player1.resize((30,30))
    player1=ImageTk.PhotoImage(player1)

    player2=Image.open("Resources\Images\player2.png")
    player2=player2.resize((30,30))
    player2=ImageTk.PhotoImage(player2)

    dice_sound=pygame.mixer.Sound("Resources\Sound\dice_roll.mp3")
    victory_sound=pygame.mixer.Sound("Resources\Sound\\victory.mp3")

    dice_arr=[dice1,dice2,dice3,dice4,dice5,dice6]
    player=[player1,player2]

    board_pos=[[10,460,-1],[62,460,-1],[110,460,50],[160,460,-1],[210,460,-1],[260,460,26],[310,460,-1],[360,460,-1],[410,460,-1],[460,460,-1],
                [10,410,-1],[62,410,-1],[110,410,-1],[160,410,-1],[210,410,-1],[260,410,-1],[310,410,-1],[360,410,-1],[410,410,-1],[460,410,69],
                [10,360,-1],[62,360,-1],[110,360,-1],[160,360,-1],[210,360,4],[260,360,-1],[310,360,-1],[360,360,-1],[410,360,-1],[460,360,-1],
                [10,310,-1],[62,310,-1],[110,310,-1],[160,310,1],[210,310,-1],[260,310,54],[310,310,-1],[360,310,-1],[410,310,-1],[460,310,-1],
                [10,260,-1],[62,260,-1],[110,260,-1],[160,260,-1],[210,260,-1],[260,260,-1],[310,260,18],[360,260,-1],[410,260,-1],[460,260,-1],
                [10,210,-1],[62,210,-1],[110,210,-1],[160,210,-1],[210,210,-1],[260,210,-1],[310,210,-1],[360,210,-1],[410,210,-1],[460,210,-1],
                [10,160,-1],[62,160,-1],[110,160,94],[160,160,-1],[210,160,51],[260,160,-1],[310,160,-1],[360,160,97],[410,160,-1],[460,160,-1],
                [10,110,-1],[62,110,-1],[110,110,-1],[160,110,-1],[210,110,-1],[260,110,-1],[310,110,-1],[360,110,-1],[410,110,-1],[460,110,-1],
                [10,60,-1],[62,60,-1],[110,60,-1],[160,60,-1],[210,60,-1],[260,60,-1],[310,60,56],[360,60,-1],[410,60,-1],[460,60,60],
                [10,10,60],[62,10,-1],[110,10,-1],[160,10,-1],[210,10,-1],[260,10,-1],[310,10,-1],[360,10,-1],[410,10,68],[460,10,-1]]

    DiceImage=random.choice(dice_arr)


    main()
    screen.mainloop()