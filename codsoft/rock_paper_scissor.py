from tkinter import *
import random
from PIL import Image,ImageTk
game_window=Tk()
game_window.title("rock paper scissor")
game_window.configure(background="orange")


#images left
rock_image=ImageTk.PhotoImage(Image.open("stone1.jpg"))
paper_image=ImageTk.PhotoImage(Image.open("paper1.jpg"))
scissor_image=ImageTk.PhotoImage(Image.open("scissor1.jpg"))
#right image
rock_image2=ImageTk.PhotoImage(Image.open("stone2.jpg"))
paper_image2=ImageTk.PhotoImage(Image.open("paper2.jpg"))
scissor_image2=ImageTk.PhotoImage(Image.open("scissor2.jpg"))

player_label= Label(game_window,image=scissor_image )
computer_label=Label(game_window,image=scissor_image)
player_label.grid(row=2,column=6)
computer_label.grid(row=2,column=0)

player_score=Label(game_window,text=0,font=("bold",40),fg="black")
computer_score=Label(game_window,text=0,font=("bold",40),fg="black")
player_score.grid(row=1,column=0)
computer_score.grid(row=1,column=6)

player_text=Label(game_window,text="player",font=("bold",40),fg="black")
computer_text=Label(game_window,text="computer",font=("bold",40),fg="black")
player_text.grid(row=0,column=0)
computer_text.grid(row=0,column=6)

message=Label(game_window,font=("bold",60))
message.grid(row=6,column=3)


def update_message(a):
    message["text"]=a  

def update_player():
    final=int(player_score["text"])
    final+=1
    player_score["text"]=(final)    

def update_computer():
    final=int(computer_score["text"])
    final+=1
    computer_score["text"]=(final) 

def winner(c,p):
    if c==p:
        update_message("tie")
    elif c=="rock":
        if p=="paper":
            update_message("player won")
            update_player()
        else:
            update_message("computer won")
            update_computer()
    elif c=="paper":
        if p=="scissor":
            update_message("player wins")
            update_player()
        else:
            update_message("computer wins")
            update_computer()
    elif c=="scissor":
        if p=="rock":
            update_message("player wins")
            update_player()
        else:
            update_message("computer win")
            update_computer()          
    else:
        pass

to_select=["rock","paper","scissor"]   
    
def choice_update(a):
    computer_choice= to_select[random.randint(0,2)] 

    if computer_choice=="rock":
        player_label.configure(image=rock_image2)
    elif computer_choice== "paper":
        player_label.configure(image=paper_image2)
    else:
        player_label.configure(image=scissor_image2)

    if a=="rock":
        computer_label.configure(image=rock_image)
        
    elif a=="paper":
        computer_label.configure(image=paper_image)
    else:
        computer_label.configure(image=scissor_image)  

    winner(computer_choice,a)                      

rock_button= Button(game_window,width=12,height=2,text="ROCK",font=("bold",18),bg="yellow",
                       fg="red",command=lambda:choice_update("rock")).grid(row=1,column=3)

paper_button= Button(game_window,width=12,height=2,text="paper",font=("bold",18),bg="yellow",
                       fg="red",command=lambda:choice_update("paper")).grid(row=2,column=3)

scissor_button= Button(game_window,width=12,height=2,text="scissor",font=("bold",18),bg="yellow",
                       fg="red",command=lambda:choice_update("scissor")).grid(row=3,column=3)



game_window.mainloop()