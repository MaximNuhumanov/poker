import turtle
import random
import logik
TILE = 40
turtle.bgpic(picname="bg.gif")
colors = ["red","green","blue","yellow","purple","brown"]
comp_dice_colors =[False for i in range(6)]
player_dice_colors =[False for i in range(6)]
end_level = False
t = turtle.Turtle()

t.screen.setup(450*TILE/32, 300*TILE/32)
t.hideturtle()
t.speed(0)
scr = t.getscreen()
turtle.tracer(0)
reroll_list = [False for i in range(5)]

t.width((TILE/32)*3)
def penup_go(x,y, resize = False):
    t.penup()
    if resize: t.goto(x*TILE/32,y*TILE/32)
    else: t.goto(x,y)
    t.pendown()
def one(x,y,tile):
    penup_go(x,y)
    t.dot()
def two(x,y,tile):
    dot_x = x-tile/6
    while dot_x < x + tile*1/3:
        penup_go(dot_x,y)
        t.dot()
        dot_x += tile/3
def three(x,y,tile):
    dot_x = x-tile/4
    while dot_x < x + tile*1/2:
        penup_go(dot_x,y)
        t.dot()
        dot_x += tile/4
def four(x,y,tile):
    dot_y = y-tile/6
    while dot_y < y + tile*1/3:
        dot_x = x-tile/6
        while dot_x < x + tile*1/3:
            penup_go(dot_x,dot_y)
            t.dot()
            dot_x += tile/3
        dot_y += tile/3
def five(x,y,tile):
    dot_y = y-tile/6
    while dot_y < y + tile*1/3:
        dot_x = x-tile/6
        while dot_x < x + tile*1/3:
            penup_go(dot_x,dot_y)
            t.dot()
            dot_x += tile/3
        dot_y += tile/3
    one(x,y,tile)
def six(x,y,tile):
    dot_y = y-tile/6
    while dot_y < y + tile*1/3:
        dot_x = x-tile/4
        while dot_x < x + tile*1/2:
            penup_go(dot_x,dot_y)
            t.dot()
            dot_x += tile/4
        dot_y += tile/3
def draw_dice(num, dice_colors, x=0,y=0,tile=TILE):
    t.setheading(0)
    penup_go(x-tile/2,y-tile/2)
    if dice_colors[num-1]:
        t.fillcolor(colors[num-1])
    else:
        t.fillcolor("white")
    t.begin_fill()
    for i in range(4):
        t.forward(tile)
        t.left(90)
    t.end_fill()
    dice_tuple[num-1](x,y,tile)
def draw_reroll_dice(num, x=0,y=0,tile=TILE):
    t.setheading(0)
    penup_go(x-tile/2,y-tile/2)
    t.fillcolor("orange")
    t.begin_fill()
    for i in range(4):
        t.forward(tile)
        t.left(90)
    t.end_fill()
    dice_tuple[num-1](x,y,tile)
def draw_set_of_dices(roll,x_start,y_start,tile=TILE, reroll =[False for i in range(5)], dice_colors =[False for i in range(5)]):
    for i, dice in enumerate(roll):
        if reroll[i]: draw_reroll_dice(dice, x = x_start + tile/2 + i*tile, y = y_start + tile/2)
        else: draw_dice(dice, dice_colors, x = x_start + tile/2 + i*tile, y = y_start + tile/2)
        t.setheading(0)
        x_start += 20*TILE//32
def make_roll():
    t.clear()
    global player_roll, computer_roll
    player_roll = [random.randint(1,6) for i in range(5)]
    computer_roll = [random.randint(1,6) for i in range(5)]
    global reroll_list
    reroll_list = [False for i in range(5)]
    
    show_roll()
def reroll_choise():
    global comp_dice_colors, player_dice_colors
    comp_dice_colors =[False for i in range(6)]
    player_dice_colors =[False for i in range(6)]
    t.clear()
    show_result()
    show_roll(rerol = True)
def reroll_1():
    reroll_list[0] = not reroll_list[0]
    if sum(map(int,reroll_list)) >3:
        reroll_list[0] = not reroll_list[0] 
        return
    reroll_choise()
def reroll_2():
    reroll_list[1] = not reroll_list[1]
    if sum(map(int,reroll_list)) >3: 
        reroll_list[1] = not reroll_list[1]
        return
    reroll_choise()
def reroll_3():
    reroll_list[2] = not reroll_list[2]
    if sum(map(int,reroll_list)) >3: 
        reroll_list[2] = not reroll_list[2]
        return
    reroll_choise()
def reroll_4():
    reroll_list[3] = not reroll_list[3]
    if sum(map(int,reroll_list)) >3: 
        reroll_list[3] = not reroll_list[3]
        return
    reroll_choise()
def reroll_5():
    reroll_list[4] = not reroll_list[4]
    if sum(map(int,reroll_list)) >3: 
        reroll_list[4] = not reroll_list[4]
        return
    reroll_choise()
def show_roll(rerol = False):
    t.clear()
    global comp_dice_colors, player_dice_colors
    comp_dice_colors =[False for i in range(6)]
    player_dice_colors =[False for i in range(6)]  
    show_result()
    penup_go(-200,-100, resize=True)
    t.write("PlAYER", font=("Tahoma",TILE//2,"bold"))
    if rerol: draw_set_of_dices(player_roll, -50*TILE//32, -100*TILE//32, reroll = reroll_list, dice_colors = player_dice_colors)
    else: draw_set_of_dices(player_roll,-50*TILE//32,-100*TILE//32, dice_colors = player_dice_colors)
    penup_go(-200,-50, resize=True)
    t.write("COMPUTER", font=("Tahoma",TILE//2,"bold"))
    draw_set_of_dices(computer_roll,-50*TILE//32,-50*TILE//32, dice_colors = comp_dice_colors)
def rerol():
    global reroll_list
    if sum(map(int,reroll_list)) == 5: return
    for i, rerol_flag in enumerate(reroll_list):
        if rerol_flag: player_roll[i] = random.randint(1,6)
    reroll_list = [True for i in range(5)]
    show_roll()
def show_result():
    comp_comb = logik.get_comb(computer_roll)
    player_comb = logik.get_comb(player_roll)

    comp_grade = logik.get_comb_grade(comp_comb)
    player_grade = logik.get_comb_grade(player_comb)

    comp_name = logik.get_comb_name(comp_grade)
    player_name = logik.get_comb_name(player_grade)

    
    for i in comp_comb:
        comp_dice_colors[i-1] = True

    for i in player_comb:
        player_dice_colors[i-1] = True

    penup_go(-200, 100, resize=True)
    t.write("PlAYER: " + player_name, font=("Tahoma",TILE//2,"bold"))
    penup_go(-200, 50, resize=True)
    t.write("COMPUTER: " + comp_name, font=("Tahoma",TILE//2,"bold"))
def show_win():
    t.clear()
    comp_comb = logik.get_comb(computer_roll)
    player_comb = logik.get_comb(player_roll)

    comp_grade = logik.get_comb_grade(comp_comb)
    player_grade = logik.get_comb_grade(player_comb)
    if comp_grade > player_grade:
        penup_go(-180, 0, resize=True)
        t.write("COMPUTER WIN", font=("Tahoma",TILE,"bold"))
    elif comp_grade < player_grade:
        penup_go(-130, 0, resize=True)
        t.write("PlAYER WIN", font=("Tahoma",TILE,"bold"))
    else:
        penup_go(-50, 0, resize=True)
        t.write("Draw ", font=("Tahoma",TILE,"bold"))


def Enter():
    global end_level
    if end_level: show_win()
    else: make_roll()
    end_level = not end_level
    
dice_tuple =(one,two,three,four,five,six)

scr.onkey(Enter,"Return")
scr.onkey(reroll_1,"1")
scr.onkey(reroll_2,"2")
scr.onkey(reroll_3,"3")
scr.onkey(reroll_4,"4")
scr.onkey(reroll_5,"5")
scr.onkey(rerol,"r")

t.goto(-200*TILE/32, TILE/32)
t.write('''Натисніть Enter, щоб почати/закінчити 
раунд. Натисніть 1/2/3/4/5/6, 
щоб обрати кубик, який ви хочете 
перекинути та натисніть R,
щоб здіснити переброс,
але перекидати можна лише 3 кубики''', font=("Tahoma",TILE//3,"bold"))

scr.listen()
turtle.mainloop()