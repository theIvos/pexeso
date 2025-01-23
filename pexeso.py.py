from tkinter import *
from PIL import Image, ImageTk
from time import sleep
from random import randint

# FUNCTIONS

# quit game
def quit_game():
    sleep(0.2)
    exit()

# click on button
def click(clicked_button,image_on):

    clicked_button.config(image=image_on)
    
    if clicked_button not in chosen_buttons:
        chosen_pics.append(image_on)
        chosen_buttons.append(clicked_button)
    else:
        pass

    print(chosen_buttons)
    print(chosen_pics)

# game events checker
def remove_or_not():
    change = "YES"
    global on_turn
    global off_turn
    sleep(0.3)

    if len(chosen_pics) == 2:
        if chosen_pics[0] == chosen_pics[1]:
            success_label['text'] = "MATCH!"
            if on_turn == player1:
                player1_score_label['text'] += 1
            else:
                player2_score_label['text'] += 1
        
            for i in chosen_buttons:
                i.destroy()
            change = "NO"

        
        else:
            
            success_label['text'] = "NOPE."
            for i in chosen_buttons:
                sleep(0.2)
                i.config(image=defualt_new)
            
        for _ in range(2):
            chosen_buttons.pop(0)
            chosen_pics.pop(0)
        if change == "YES":
            on_turn, off_turn = off_turn, on_turn
            on_turn_label['text'] = on_turn
        # print(on_turn)

    if player1_score_label["text"] + player2_score_label["text"] == 18:
        game_over = Label(root,text="",font=("Tahoma",30,"bold"),bg=main_bg,fg=on_turn_mark_color)
        game_over.place(x=180,y=230)
        if player1_score_label["text"] > player2_score_label["text"]:
            winner = f"{player1} WINS!"
            game_over['text'] = winner
        elif player1_score_label["text"] < player2_score_label["text"]:
            winner = f"{player2} WINS!"
            game_over['text'] = winner
        else:
            game_over["text"] = "It's a draw!"

           

    root.after(10,remove_or_not)
    
# clearing the success/no success text
def clear_success():
    
    success_label["text"] = ''
    root.after(2000,clear_success)

# randomizing pictures on buttons
def randomize():
    new_pic = new_images[randint(0,len(new_images)-1)]
    while True:

        if new_pic not in used_images:
            used_images.append(new_pic)            
            return new_pic
        elif new_pic not in used_images_2:
            used_images_2.append(new_pic)
            return new_pic
        else:
            new_pic = new_images[randint(0,len(new_images)-1)]

# set up the main game elements
def create_playground():
    global player1
    global player2
    global on_turn
    global off_turn
    global player1_score_label
    global player2_score_label
    global on_turn_label

    player1 = player_1_start_entry.get()
    player2 = player_2_start_entry.get()

    player_1_score = 0
    player_2_score = 0

    on_turn = player1
    off_turn = player2

    start_game.destroy()
    name_start_label.destroy()
    name_start_label2.destroy()
    player_1_start.destroy()
    player_1_start_entry.destroy()
    player_2_start.destroy()
    player_2_start_entry.destroy()
   
    player1_label = Label(root, text=player1,font=("Tahoma",20,),bg=main_bg,fg=player_color)
    player1_label.place(x=710, y=240)
    player2_label = Label(root, text=player2,font=("Tahoma",20,),bg=main_bg,fg=player_color)
    player2_label.place(x=710, y=440)

    name_label = Label(root, text="The Ivos",font=("Tahoma",22),bg=main_bg,fg=main_fg)
    name_label.place(x=700, y=40)
    name_label2 = Label(root, text="PEXESO GAME",font=("Tahoma",24,"bold"),bg=main_bg,fg=main_fg)
    name_label2.place(x=700, y=75)

    on_turn_mark_label = Label(root, text="currently on turn >>",font=("Tahoma",14,),bg=main_bg,fg=on_turn_mark_color)
    on_turn_mark_label.place(x=710, y=140)
    on_turn_label = Label(root, text=on_turn,font=("Tahoma",24,"bold"),bg=main_bg,fg=on_turn_color)
    on_turn_label.place(x=730, y=166)

    player1_score_label = Label(root, text=player_1_score,font=("Tahoma",38,),bg=main_bg,fg=player_color)
    player1_score_label.place(x=730, y=280)
    player2_score_label = Label(root, text=player_2_score,font=("Tahoma",38,),bg=main_bg,fg=player_color)
    player2_score_label.place(x=730, y=480)
    
    for i in range(6):
        nd = i    
        columnses = 30
        rowses = 50 + (i*105)
        i = f"R{i}"
        r = f"{i}"
        imr = randomize()


        i = Button(root,text=f'R{columnses},{rowses}',image=defualt_new,command=lambda img=imr,btn=r:click(rows_in_game[btn],img))
        rows_in_game[f'R{nd}'] = i
        i.place(x=rowses,y=columnses)

        for j in range(1,6):
            cd = j
            columnses = 30+j*105
            j = f"C{j}{nd}"
            c = f"{j}"
            imj=randomize()

            j = Button(root,text=f'C{columnses},{rowses}',image=defualt_new,command=lambda img=imj,btn=c:click(rows_in_game[btn],img))
            
            rows_in_game[f'C{cd}{nd}'] = j
            j.place(x=rowses,y=columnses)

#DEFAULT GAME SETTINGS
player1 = ""
player2 = ""

on_turn = player1
off_turn = player2

player_1_score = 0
player_2_score = 0

rows_in_game = {}
rowses = 0
columnses = -1

#COLORS SETS
main_bg = "#0E8800"
main_fg = "#0C4400"
success_color = "#A63F00"
player_color = "#E0E0E0"
on_turn_mark_color = "#82FF3F"
on_turn_color = "#813208"
warning_color = "#B20000"
entry_color = "#68E164"

#MAIN SCREEN SET UP
root = Tk()
root.title("The Ivos PEXESO GAME")
root.geometry("1000x700")
root.resizable(False,False)
root.config(bg=main_bg)
root.iconbitmap("images/icon.ico")

frame_game = Frame(root, bg=main_bg)
frame_game.pack(expand=True)

# raw images list
raw_images = ["images/animal_01.png","images/animal_02.png","images/animal_03.png",
            "images/animal_04.png","images/animal_05.png","images/animal_06.png","images/animal_07.png",
            "images/animal_08.png","images/animal_09.png","images/animal_10.png","images/animal_11.png",
            "images/animal_12.png","images/animal_13.png","images/animal_14.png","images/animal_15.png",
            "images/animal_16.png","images/animal_17.png","images/animal_18.png",     
                ]

# images transformed for using in tkinter
new_images = []

# default image for every button
default_raw = Image.open("images/animal_00.png")
default_resize = default_raw.resize((100,100), Image.LANCZOS)
defualt_new = ImageTk.PhotoImage(default_resize)

# cycle for the rest of the images
for i in raw_images:
    raw = Image.open(i)
    resize = raw.resize((100,100), Image.LANCZOS)
    new = ImageTk.PhotoImage(resize)
    new_images.append(new)
    new_images.append(new)


# lists for assigning only 2 of a kind
used_images = []
used_images_2 = []

# storing the pics and buttons for system to check if there is a match
chosen_pics = []
chosen_buttons = []

#LABELS
warning_label = Label(root, text="",font=("Tahoma",16,),bg=main_bg,fg=warning_color)
warning_label.place(x=710, y=210)

success_label = Label(root, text="",font=("Tahoma",32,"bold"),bg=main_bg,fg=success_color)
success_label.place(x=710, y=350)

player1_score_label = Label(root, text=player_1_score,font=("Tahoma",38,),bg=main_bg,fg=main_bg)
player1_score_label.place(x=730, y=280)

player2_score_label = Label(root, text=player_2_score,font=("Tahoma",38,),bg=main_bg,fg=main_bg)
player2_score_label.place(x=730, y=480)

on_turn_mark_label = Label(root, text="currently on turn >>",font=("Tahoma",14,),bg=main_bg,fg=main_bg)
on_turn_mark_label.place(x=710, y=140)

on_turn_label = Label(root, text=on_turn,font=("Tahoma",24,"bold"),bg=main_bg,fg=main_bg)
on_turn_label.place(x=730, y=166)

name_start_label = Label(root, text="The Ivos",font=("Tahoma",26),bg=main_bg,fg=main_fg)
name_start_label.place(x=200, y=25)
name_start_label2 = Label(root, text="PEXESO GAME",font=("Tahoma",30,"bold"),bg=main_bg,fg=main_fg)
name_start_label2.place(x=200, y=75)

quit_label = Button(root, text="QUIT GAME",font=("Tahoma",14,"bold"),fg=main_fg,bg=main_bg,command=quit_game)
quit_label.place(x=820, y=620)

player_1_start = Label(root,text="PLAYER 1 NAME: ",font=("Tahoma",24,"bold"),bg=main_bg,fg=player_color)
player_1_start.place(x=70, y=200)
player_1_start_entry = Entry(root,bg=entry_color,font=("Tahoma",24,"bold"),fg=main_fg,width=20)
player_1_start_entry.place(x=360, y=200)
player_1_start_entry.insert(END,"Ivos")
player_1_start_entry.focus()

player_2_start = Label(root,text="PLAYER 2 NAME: ",font=("Tahoma",24,"bold"),bg=main_bg,fg=player_color)
player_2_start.place(x=70, y=260)
player_2_start_entry = Entry(root,bg=entry_color,font=("Tahoma",24,"bold"),fg=main_fg,width=20)
player_2_start_entry.place(x=360, y=260)
player_2_start_entry.insert(END,"Retrivr")

start_game = Button(root,text="START GAME!",font=("Tahoma",24,"bold"),command=create_playground)
start_game.place(x=440,y=330)

#LOOP EVENT CHECKS
root.after(10,remove_or_not)
root.after(2000,clear_success)

#MAIN SCREEN LOOP
root.mainloop()