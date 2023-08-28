# Библиотека tkinter отвечает за GUI проекта
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
# Библиотека для работы с медиа
from PIL import ImageTk, Image
# Библиотека для системных команд
import os
# Использую для трансформации str в dict
import json

win = Tk()

win.title("CoakValley")
win.attributes('-fullscreen', True)
win["background"] = "black"

######################## Всякие переменные ########################################################

# сейв
player_save = {
    "name": "username",
    "lastlevel": 0,
    "screen_width": 1920,
    "screen_height": 1080
}

# открываем сейв
if not os.path.isfile("player_save.txt"):
    save = open("player_save.txt", "w+")
    json.dump(player_save, save)
else:
    save = open("player_save.txt", "r+")
    player_save = json.load(save)

# Параметры размера экрана
screen_width = player_save["screen_width"]
screen_height = player_save["screen_height"]

# Относительные единицы. vh = 1% от высоты экрана, vw = 1% от ширины экрана
vh = screen_height / 100
vw = screen_width / 100


class Quest(object):
    def __init__(self, id, text, place_button_height, place_button_width):
        self.id = id
        self.text = text
        self.place_button_height = place_button_height
        self.place_button_width = place_button_width


quests = []
for i in range(10):
    match i:
        case 0:
            # Площадь северная - шут
            quests.append(Quest(i, "Задача 1", 28 * vh, 73 * vw))
        case 1:
            # Площадь южная - шут
            quests.append(Quest(i, "Задача 2", 85 * vh, 67 * vw))
        case 2:
            # Площадь западная - повар
            quests.append(Quest(i, "Задача 3", 62 * vh, 22.5 * vw))
        case 3:
            # Причал - повар
            quests.append(Quest(i, "Задача 4", 9 * vh, 64 * vw))
        case 4:
            # Башня мага - маг
            quests.append(Quest(i, "Задача 5", 31 * vh, 43.5 * vw))
        case 5:
            # Утес - маг
            quests.append(Quest(i, "Задача 6", 23 * vh, 5 * vw))
        case 6:
            # Главный штаб - генерал
            quests.append(Quest(i, "Задача 7", 32 * vh, 54 * vw))
        case 7:
            # Карчма - генерал
            quests.append(Quest(i, "Задача 8", 77 * vh, 35 * vw))
        case 8:
            # Дворец - королева
            quests.append(Quest(i, "Задача 9", 51 * vh, 56 * vw))
        case 9:
            quests.append(Quest(i, "Задача 10", 27 * vh, 0 * vw))

########################################################################################################################


######################## Создание виджетов для карты с квестами ########################################################
map_img = ImageTk.PhotoImage(Image.open('png/map.png').resize((screen_width, screen_height)))
map_label = Label(image=map_img)
complited_quest_img = ImageTk.PhotoImage(Image.open('png/complited_quest.png').resize((int(2 * vw), int(2 * vw))))
not_complited_quest_img = ImageTk.PhotoImage(
    Image.open('png/not_complited_quest.png').resize((int(2 * vw), int(2 * vw))))
locked_quest_img = ImageTk.PhotoImage(Image.open('png/locked_quest.png').resize((int(2 * vw), int(2 * vw))))
travelpoint_img = ImageTk.PhotoImage(Image.open('png/travelpoint.png').resize((int(2 * vw), int(2 * vw))))
buttons_for_quest = []
for i in range(10):
    buttons_for_quest.append(Button(borderwidth=0, highlightthickness=0, relief=FLAT, image=complited_quest_img))


########################################################################################################################


def make_map_window():
    map_label.place(x=-1, y=-1)
    for i in range(10):
        # cur_button = buttons_for_quest[i]
        # if i < player_save["lastlevel"]:
        #    cur_button["image"] = complited_quest_img
        # if i == player_save["lastlevel"]:
        #    cur_button["image"] = not_complited_quest_img
        # if i > player_save["lastlevel"]:
        #    cur_button["image"] = locked_quest_img
        # cur_button.configure(command=lambda k=i: make_main_game_window(k, quests[k].text))
        # buttons_for_quest[i] = cur_button
        buttons_for_quest[i].configure(command=lambda k=i: make_main_game_window(k, quests[k].text),
                                       image=travelpoint_img)
        buttons_for_quest[i].place(x=quests[i].place_button_width, y=quests[i].place_button_height, width=int(2 * vw), height=int(2 * vw))


######################## Создание виджетов для главного экрана с игрой #################################################
background_img = ImageTk.PhotoImage(Image.open('png/code_background.png').resize((screen_width, screen_height)))
background_label = Label(image=background_img)
gamename_label = Label(bg="White", text="CoakValley", font="Arial 100", padx=5 * vw, pady=5 * vh)
startgame_button = ttk.Button(text="Подключиться")
settings_button = ttk.Button(text="Настройки")
exit_button = ttk.Button(text="Отключиться")
########################################################################################################################


def make_menu_window():
    background_label.place(x=-1, y=-1)
    gamename_label.place(x=25 * vw, y=10 * vh, width=50 * vw, height=20 * vh)
    startgame_button.place(x=35 * vw, y=40 * vh, width=30 * vw, height=10 * vh)
    settings_button.place(x=35 * vw, y=55 * vh, width=30 * vw, height=10 * vh)
    exit_button.place(x=35 * vw, y=70 * vh, width=30 * vw, height=10 * vh)


def destroy_menu_window():
    background_label.destroy()
    gamename_label.destroy()
    startgame_button.destroy()
    settings_button.destroy()
    exit_button.destroy()


############################ Создание виджетов для главного экрана с игрой #############################################
input_label = Label(text="Входные данные")
output_label = Label(text="Выходные данные")
verdict_label = Label(text="Результат")
input_txt = Text(bg="#9ACD32")
output_txt = Text(bg="#9ACD32")
verdict_txt = Text(bg="#9ACD32")
scrollbar_input_txt = Scrollbar(orient="vertical", command=input_txt.yview, bg="#808000")
scrollbar_output_txt = Scrollbar(orient="vertical", command=output_txt.yview, bg="#808000")
scrollbar_verdict_txt = Scrollbar(orient="vertical", command=verdict_txt.yview, bg="#808000")
change_mode_btn = Button(bg="#006400")
play_btn = Button(bg="#006400")
guidebook_btn = Button(bg="#006400")
menu_btn = Button(bg="#006400")
code_label = Label(text="Редактор")
code_numbering_txt = Text(font="sans-serif 20", bg='#2763a3', fg='white', state='disabled')
code_txt = Text(font="sans-serif 20", bg='#2763a3', fg='white')
font = Font(font=code_txt['font'])
tab = font.measure('    ')
code_txt.config(tabs=tab)
code_txt.insert("0.0",
                """#include <bits/stdc++.h>\n\nusing namespace std;\n\nint main(){\n   freopen("output.txt", "w", stdout);\n\n   int a = 1;\n   for(int i = 0; i < 10; i++){\n      cout << a + i << endl;\n   }\n}""")


def multiple_yview(*args):
    code_numbering_txt.yview(*args)
    code_txt.yview(*args)


scrollbar_code_txt = Scrollbar(orient="vertical", command=multiple_yview, bg="#808000")
minigame = Frame(bg="black")
story_label = Label(text="Задача")
story_txt = Text(bg="#9ACD32")
scrollbar_story_txt = Scrollbar(orient="vertical", command=story_txt.yview, bg="#808000")


########################################################################################################################

def make_main_game_window(id, quest_text):
    input_label.place(width=25 * vw, height=2 * vh, x=0, y=0)
    input_txt.place(width=24 * vw, height=23 * vh, x=0, y=2 * vh)
    scrollbar_input_txt.place(width=1 * vw, height=25 * vh, x=24 * vw, y=0 * vh)
    output_label.place(width=25 * vw, height=2 * vh, x=0, y=25 * vh)
    output_txt.place(width=24 * vw, height=23 * vh, x=0, y=27 * vh)
    scrollbar_output_txt.place(width=1 * vw, height=25 * vh, x=24 * vw, y=25 * vh)
    verdict_label.place(width=25 * vw, height=2 * vh, x=0, y=50 * vh)
    verdict_txt.place(width=25 * vw, height=25 * vh, x=0, y=52 * vh)
    scrollbar_verdict_txt.place(width=1 * vw, height=25 * vh, x=24 * vw, y=50 * vh)
    change_mode_btn.place(width=12.5 * vw, height=12.5 * vh, x=0, y=75 * vh)
    play_btn.place(width=12.5 * vw, height=12.5 * vh, x=12.5 * vw, y=75 * vh)
    menu_btn.place(width=12.5 * vw, height=12.5 * vh, x=0, y=87.5 * vh)
    guidebook_btn.place(width=12.5 * vw, height=12.5 * vh, x=12.5 * vw, y=87.5 * vh)
    code_label.place(width=39 * vw, height=2 * vh, x=25 * vw, y=0)
    code_numbering_txt.place(width=3 * vw, height=98 * vh, x=25 * vw, y=2 * vh)
    code_txt.place(width=36 * vw, height=98 * vh, x=28 * vw, y=2 * vh)
    scrollbar_code_txt.place(width=1 * vw, height=100 * vh, x=64 * vw, y=0)
    minigame.place(width=35 * vw, height=35 * vw, x=65 * vw, y=0)
    story_label.place(width=35 * vw, height=2 * vh, x=65 * vw, y=35 * vw)
    story_txt.place(width=34 * vw, height=98 * vh - 35 * vw, x=65 * vw, y=35 * vw + 2 * vh)
    scrollbar_story_txt.place(width=1 * vw, height=100 * vh - 35 * vw, x=99 * vw, y=35 * vw)
    input_txt["yscrollcommand"] = scrollbar_input_txt.set
    output_txt["yscrollcommand"] = scrollbar_output_txt.set
    verdict_txt["yscrollcommand"] = scrollbar_verdict_txt.set
    code_txt["yscrollcommand"] = scrollbar_code_txt.set
    code_numbering_txt["yscrollcommand"] = scrollbar_code_txt.set
    story_txt["yscrollcommand"] = scrollbar_story_txt.set

    story_txt.insert("0.0", quest_text)


def click_play_btn():
    f = open("player_code.cpp", "w")
    f.write(code_txt.get("1.0", "end-1c"))
    print(code_txt.get("1.0", "end-1c"))
    f.close()
    os.system("g++ player_code.cpp -o player_program")
    os.system("./player_program")


def exit():
    win.destroy()


startgame_button["command"] = lambda: [make_map_window(), destroy_menu_window()]
exit_button["command"] = exit

make_menu_window()

win.mainloop()

#       #include <bits/stdc++.h>
#
#       using namespace std;
#
#       int main(){
#       	freopen("output.txt", "w", stdout);
#       	int a = 1;
#       	for(int i = 0; i < 10; i++){
#       		cout << a + i << endl;
#       	}
#       }
