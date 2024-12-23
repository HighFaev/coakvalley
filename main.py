# Библиотека tkinter отвечает за GUI проекта
import string
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import Font

# Библиотека для работы с медиа
from PIL import ImageTk, Image
# Библиотека для системных команд
import os
import psutil
import time
# Использую для трансформации str в dict
import json
# Многопоточность
from threading import Thread

import pdb

win = Tk()

win.title("CoakValley")
win.attributes('-fullscreen', True)
win["background"] = "black"

######################## Всякие переменные  #############################################################################

# Массив всех шрифтов
fonts = list(font.families())

# сейв
player_save = {
    "lastlevel": 0,
    "screen_width": 1920,
    "screen_height": 1080,
    "last_code": """#include <bits/stdc++.h>\n\nusing namespace std;\n\nint main(){\n   freopen("gen_output.txt", "w", stdout);\n\n   int a = 1;\n   for(int i = 0; i < 10; i++){\n      cout << a + i << endl;\n   }\n}""",
}

# открываем сейв
if not os.path.isfile("player_save.txt"):
    save = open("player_save.txt", "w+")
    json.dump(player_save, save)
    save.close()
else:
    save = open("player_save.txt", "r+")
    player_save = json.load(save)
    save.close()

# Параметры размера экрана
screen_width = player_save["screen_width"]
screen_height = player_save["screen_height"]

# Относительные единицы. vh = 1% от высоты экрана, vw = 1% от ширины экрана
vh = screen_height / 100
vw = screen_width / 100

# Настройки основного шрифта
font_size = int(screen_height / 54)
font_name = "MS Gothic"


temp = {
    "cur_stage": 1,  # 1 - menu, 2 - map, 3 - dialog, 4 - editor
    "cur_task": 0,
    "test_mode": 0,
    "time_limit": 0
}

class Quest(object):
    def __init__(self, id, text, place_button_height, place_button_width):
        self.id = id
        self.text = text
        self.place_button_height = place_button_height
        self.place_button_width = place_button_width


def make_special_symbols(s):
    k = 0
    for c in s:
        match c:
            case '|':
                s = s[:k] + '\n' + s[k + 1:]
        k += 1
    return s


quests = []
for i in range(9):
    match i:
        case 0:
            # Площадь северная - шут
            quests.append(Quest(i, make_special_symbols(open("tasks/text/" + str(i + 1) + ".txt", "r+").read()), 21 * vh, 81.5 * vw))
        case 1:
            # Площадь южная - шут
            quests.append(Quest(i, "Задача 2", 72.5 * vh, 77 * vw))
        case 2:
            # Площадь западная - повар
            quests.append(Quest(i, "Задача 3", 56 * vh, 29 * vw))
        case 3:
            # Причал - повар
            quests.append(Quest(i, "Задача 4", 4.5 * vh, 60 * vw))
        case 4:
            # Башня мага - маг
            quests.append(Quest(i, "Задача 5", 31.6 * vh, 46.5 * vw))
        case 5:
            # Утес - маг
            quests.append(Quest(i, "Задача 6", 18 * vh, 15 * vw))
        case 6:
            # Главный штаб - генерал
            quests.append(Quest(i, "Задача 7", 28.2 * vh, 54 * vw))
        case 7:
            # Карчма - генерал
            quests.append(Quest(i, "Задача 8", 71.5 * vh, 38.7 * vw))
        case 8:
            # Дворец - королева
            quests.append(Quest(i, "Задача 9", 40 * vh, 59 * vw))


black_screen = Label(bg="black")

########################################################################################################################


def new_text(obj, text):
    obj.delete(0, "end")
    obj.insert.insert(0, text)


def exit():
    save = open("player_save.txt", "w+")
    json.dump(player_save, save)
    save.close()
    win.destroy()


def esc_pressed():
    match temp["cur_stage"]:
        case 1:
            exit()
        case 2:
            destroy_map_window()
            make_menu_window()
        case 3:
            ...
        case 4:
            destroy_main_game_window()
            make_map_window()
        case 5:
            destroy_help_window()
            make_main_game_window(temp["cur_task"])


def key_pressed(key):
    match key.keysym:
        case "Escape":
            esc_pressed()
        case other:
            ...


def fit_text_in_box(text: string, font: Font, width: float, height: float):
    #print(text)
    #print(font)
    #print(width)
    #print(height)
    gen_text = ""
    last_line = ""
    new_word = ""
    one_line_height = font.metrics('linespace')
    number_of_lines = 1
    i = 0
    while i < len(text):
        #print('\n' + str(i))
        need_space = ''
        need_paragraph = ''
        #print(font["size"])
        if not last_line == "":
            need_space = ' '
        if not gen_text == "":
            need_paragraph = '\n'
        if text[i] == ' ':
            #print("A", end="")
            if font.measure(last_line+need_space+new_word) <= width:
                #print("B", end="")
                #print(1)
                last_line += need_space + new_word
                new_word = ""
            else:
                #print("C", end="")
                if font.measure(new_word) > width:
                    i = -1
                    last_line = ""
                    gen_text = ""
                    new_word = ""
                    font["size"] -= 1
                    number_of_lines = 1
                    one_line_height = font.metrics('linespace')
                else:
                    gen_text += need_paragraph + last_line
                    last_line = new_word
                    new_word = ""
                    number_of_lines += 1
        else:
            #print("D", end="")
            new_word += text[i]
        if i + 1 == len(text):
            if font.measure(last_line+need_space+new_word) <= width:
                last_line += need_space + new_word
                gen_text += '\n' + last_line
                number_of_lines += 1
            else:
                gen_text += '\n' + last_line
                last_line = new_word
                if font.measure(last_line) > width:
                    i = -1
                    last_line = ""
                    gen_text = ""
                    new_word = ""
                    font["size"] -= 1
                    number_of_lines = 1
                    one_line_height = font.metrics('linespace')
                else:
                    gen_text += '\n' + last_line
                    number_of_lines += 1
        if number_of_lines * one_line_height > height:
            #print("F", end="")
            i = -1
            last_line = ""
            gen_text = ""
            new_word = ""
            font["size"] -= 1
            number_of_lines = 1
            one_line_height = font.metrics('linespace')
        i += 1
        #print("\nCUR GEN_TEXT:\n" + gen_text + "\nCUR LAST_LINE:\n" + last_line + "\nCUR NEW_WORD:\n" + new_word)
    return gen_text, font


########################################################################################################################
########################################################################################################################


######################## Виджеты для карты с квестами ##################################################################


map_img = ImageTk.PhotoImage(Image.open('png/map.png').resize((screen_width, screen_height)))
map_label = Label(image=map_img)
complited_quest_img = ImageTk.PhotoImage(Image.open('png/complited_quest.png').resize((int(2 * vw), int(2 * vw))))
not_complited_quest_img = ImageTk.PhotoImage(
    Image.open('png/not_complited_quest.png').resize((int(2 * vw), int(2 * vw))))
locked_quest_img = ImageTk.PhotoImage(Image.open('png/locked_quest.png').resize((int(2 * vw), int(2 * vw))))
travelpoint_img = ImageTk.PhotoImage(Image.open('png/travelpoint.png').resize((int(2 * vw), int(2 * vw))))
buttons_for_quest = []
for i in range(9):
    buttons_for_quest.append(Button(borderwidth=0, highlightthickness=0, relief=FLAT, image=complited_quest_img))


########################################################################################################################


def make_map_window():
    temp["cur_stage"] = 2
    map_label.place(x=-1, y=-1)
    for i in range(9):
        buttons_for_quest[i].configure(
            command=lambda k=i: [make_dialog_window(k), destroy_map_window()],
            image=travelpoint_img)
        buttons_for_quest[i].place(x=quests[i].place_button_width, y=quests[i].place_button_height, width=int(2 * vw),
                                   height=int(2 * vw))


def destroy_map_window():
    map_label.place_forget()
    for i in range(9):
        buttons_for_quest[i].place_forget()


########################################################################################################################
########################################################################################################################


############################################ Настройки #################################################################
background_menu_img = ImageTk.PhotoImage(Image.open('png/code_background.png').resize((screen_width, screen_height)))
settings_exit_img = ImageTk.PhotoImage(Image.open('png/settings_exit.png').resize((int(20*vh), int(20*vh))))
settings_label_img = ImageTk.PhotoImage(Image.open('png/settings.png').resize((int(60*vw), int(20*vh))))
settings_height_img = ImageTk.PhotoImage(Image.open('png/settings_height.png').resize((int(20*vw), int(10*vh))))
settings_width_img = ImageTk.PhotoImage(Image.open('png/settings_width.png').resize((int(20*vw), int(10*vh))))
settings_save_img = ImageTk.PhotoImage(Image.open('png/save_settings.png').resize((int(40*vw), int(20*vh))))
settings_exit_button = Button(image=settings_exit_img, borderwidth=0, highlightthickness=0, relief=FLAT,)
settings_save_button = Button(image=settings_save_img, borderwidth=0, highlightthickness=0, relief=FLAT,)
settings_label = Label(image=settings_label_img)
settings_width_label = Label(image=settings_width_img)
settings_height_label = Label(image=settings_height_img)
settings_width_txt = Text(font=(font_name, int((font_size + 1) * 0.75 * 2)), bg='#000000', fg='#17FF00', insertbackground="#17FF00", wrap="word",highlightthickness=0)
settings_height_txt = Text(font=(font_name, int((font_size + 1) * 0.75 * 2)), bg='#000000', fg='#17FF00', insertbackground="#17FF00", wrap="word",highlightthickness=0)
########################################################################################################################

def make_settings_window():
    settings_exit_button.place(x=5*vw, y=5*vh, width=int(20*vh), height=int(20*vh))
    settings_label.place(x=20*vw, y=5*vh, width=int(60*vw), height=int(20*vh))
    settings_width_label.place(x=20*vw, y=30*vh, width=int(20*vw), height=int(10*vh))
    settings_height_label.place(x=20*vw, y=45*vh, width=int(20 * vw), height=int(10 * vh))
    settings_width_txt.place(x=25*vw+int(20 * vw), y=30*vh, width=int(35 * vw), height=int(10 * vh))
    settings_height_txt.place(x=25*vw+int(20 * vw), y=45*vh, width=int(35 * vw), height=int(10 * vh))
    settings_save_button.place(x=30*vw, y=60*vh, width=int(40*vw), height=int(20*vh))

    settings_width_txt.insert("0.0", player_save["screen_width"])
    settings_height_txt.insert("0.0", player_save["screen_height"])
def destroy_settings_window():
    settings_exit_button.place_forget()
    settings_label.place_forget()
    settings_width_label.place_forget()
    settings_height_label.place_forget()
    settings_width_txt.place_forget()
    settings_height_txt.place_forget()
    settings_width_txt.delete("0.0", "end")
    settings_height_txt.delete("0.0", "end")
    settings_save_button.place_forget()

def save_settings():
    try:
        player_save["screen_width"] = int(settings_width_txt.get("0.0", "end"))
        player_save["screen_height"] = int(settings_height_txt.get("0.0", "end"))
    finally:
        settings_width_txt.delete("0.0", "end")
        settings_height_txt.delete("0.0", "end")
        settings_width_txt.insert("0.0", player_save["screen_width"])
        settings_height_txt.insert("0.0", player_save["screen_height"])

########################################################################################################################
########################################################################################################################

################################################# Диалоги ##############################################################

lines = []
cur_line = 0
dialog_background_img = ImageTk.PhotoImage(Image.open("png/code_background.png").resize((screen_width, screen_height)))
dialog_font = Font(name=font_name, size=40)
dialog_text = Text(bg='#000000', fg='#17FF00', highlightcolor="#17FF00", highlightthickness=2, highlightbackground="#17FF00", wrap=WORD, state=DISABLED)
dialog_background = Label(image=dialog_background_img)
dialog_buttons = []
for i in range(3):
    dialog_buttons.append(Button(bg='#000000', fg='#17FF00', highlightcolor="#17FF00", highlightthickness=2, highlightbackground="#17FF00", state=DISABLED))
########################################################################################################################


def make_dialog_list(id):
    file_open = open("dialogs/" + str(id) + ".txt", "r+")
    file = file_open.read()
    file_open.close()
    #print(file)
    dialog = {
        "type": "",
        "text": "",
        "icon": "",
        "bg": "",
        "ch": [],
        "fontsz": ""
    }
    lines = []
    i = 0
    while i < len(file):
        if file[i] == '@':
            i += 1
            new_line = dialog.copy()
            if len(lines) > 0:
                new_line = lines[len(lines)-1].copy()
            #print(new_line)
            str_r = ""
            setting_name = ""
            read_choises = False
            choises = []
            choise = ["", 0]
            number_of_spec = 0
            while True:
                c = file[i]
                match c:
                    case ':':
                        setting_name = str_r
                        str_r = ""
                        if setting_name == "ch":
                            read_choises = True
                        else:
                            read_choises = False
                    case '+':
                        if not read_choises:
                            new_line[setting_name] = str_r
                        else:
                            new_line[setting_name] = choises
                        str_r = ""
                    case '@':
                        lines.append(new_line)
                        break
                    case '\n':
                        ...
                    case other:
                        if read_choises and c == '|':
                            number_of_spec += 1
                            if number_of_spec % 2 == 0:
                                choise[1] = int(str_r)
                                str_r = str(str_r)
                                choises.append((choise[0], choise[1]))
                            else:
                                choise[0] = str_r
                            str_r = ""
                        else:
                            str_r += c
                i += 1
        i += 1

    print(lines)

    return lines


def make_dialog_window():
    global dialog_background, dialog_background_img, dialog_text, dialog_font, dialog_buttons, lines
    lines = make_dialog_list(0)

    #Фон
    dialog_background_img = ImageTk.PhotoImage(Image.open(lines[cur_line]["bg"]).resize((screen_width, screen_height)))
    dialog_background["image"] = dialog_background_img
    dialog_background.place(width=screen_width, height=screen_height)
    win.update()

    txt_width = 0
    txt_height = 0
    txt_x = 0
    txt_y = 0

    btn_setting = {
        "width": 10*vw,
        "height": 20*vh,
        "x": 0,
        "y": 60*vh,
        "text": "",
        "line_to_go": 0,
        "image": 0
    }
    btn_settings = []


    match lines[cur_line]["type"]:
        case '1':
            txt_width = 45*vw
            txt_height = 30*vh
            txt_x = 45*vw
            txt_y = 20*vh

            for i in range(len(lines[cur_line]["ch"])):
                btn_setting_cp = btn_setting.copy()
                btn_setting_cp["x"] = 45*vw + 15*i*vw
                btn_setting_cp["text"] = lines[cur_line]["ch"][i][0]
                btn_setting_cp["line_to_go"] = lines[cur_line]["ch"][i][1]
                btn_settings.append(btn_setting_cp)
        case '2':
            txt_width = 50*vw
            txt_height = 25*vh
            txt_x = 10*vw
            txt_y = 65*vh

            btn_setting_cp = btn_setting.copy()
            btn_setting_cp["width"] = 25*vh
            btn_setting_cp["height"] = 25*vh
            btn_setting_cp["x"] = 65*vw
            btn_setting_cp["y"] = 65*vh
            btn_setting_cp["image"] = lines[cur_line]["ch"][0][0]
            btn_setting_cp["line_to_go"] = lines[cur_line]["ch"][0][1]
            btn_settings.append(btn_setting_cp)
        case '3':
            txt_width = 70*vw
            txt_height = 25*vh
            txt_x = 5*vw
            txt_y = 70*vh

            btn_setting_cp = btn_setting.copy()
            btn_setting_cp["width"] = 25 * vh
            btn_setting_cp["height"] = 25 * vh
            btn_setting_cp["x"] = 80 * vw
            btn_setting_cp["y"] = 70 * vh
            btn_setting_cp["image"] = lines[cur_line]["ch"][0][0]
            btn_setting_cp["line_to_go"] = lines[cur_line]["ch"][0][1]
            btn_settings.append(btn_setting_cp)

    #Текст
    dialog_font["size"] = lines[cur_line]["fontsz"]
    dialog_text["font"] = dialog_font
    dialog_text["state"] = NORMAL
    dialog_text.delete("0.0", "end")
    dialog_text.insert("0.0", lines[cur_line]["text"])
    dialog_text["state"] = DISABLED
    dialog_text.place(x=txt_x, y=txt_y, width=txt_width, height=txt_height)
    dialog_text.lift()

    #Кнопки
    for i in range(len(btn_settings)):
        dialog_buttons[i].place(x=btn_settings[i]["x"], y=btn_settings[i]["y"], width=btn_settings[i]["width"], height=btn_settings[i]["height"])
        if lines[cur_line]["type"] == '1':
            btn_text_setting = fit_text_in_box(btn_settings[i]["text"], dialog_font, btn_settings[i]["width"], btn_settings[i]["height"])
            dialog_buttons[i]["font"] = btn_text_setting[1]
            dialog_buttons[i].configure(text=btn_text_setting[0])

    win.update()


########################################################################################################################
########################################################################################################################

######################## Виджеты для меню ##############################################################################
gamename_img = ImageTk.PhotoImage(Image.open('png/gamename_label3.png').resize((int(50*vw), int(20*vh))))
startgame_img = ImageTk.PhotoImage(Image.open('png/startgame.png').resize((int(30*vw), int(10*vh))))
settings_img = ImageTk.PhotoImage(Image.open('png/settings.png').resize((int(30*vw), int(10*vh))))
exit_menu_img = ImageTk.PhotoImage(Image.open('png/menu_exit.png').resize((int(30*vw), int(10*vh))))
background_label = Label(image=background_menu_img)
gamename_label = Label(image=gamename_img)
startgame_button = Button(image=startgame_img, borderwidth=0, highlightthickness=0, relief=FLAT,)
settings_button = Button(image=settings_img, borderwidth=0, highlightthickness=0, relief=FLAT,)
exit_button = Button(image=exit_menu_img, borderwidth=0, highlightthickness=0, relief=FLAT,)


########################################################################################################################


def make_menu_window():
    temp["cur_stage"] = 1
    background_label.place(x=-1, y=-1)
    gamename_label.place(x=25 * vw, y=10 * vh, width=int(50 * vw), height=int(20 * vh))
    startgame_button.place(x=35 * vw, y=40 * vh, width=30 * vw, height=10 * vh)
    settings_button.place(x=35 * vw, y=55 * vh, width=30 * vw, height=10 * vh)
    exit_button.place(x=35 * vw, y=70 * vh, width=30 * vw, height=10 * vh)


def destroy_menu_window():
    background_label.place_forget()
    gamename_label.place_forget()
    startgame_button.place_forget()
    settings_button.place_forget()
    exit_button.place_forget()


########################################################################################################################
########################################################################################################################


############################ Создание виджетов для гайд-книги ##########################################################
guide_locked_image = ImageTk.PhotoImage(Image.open('png/guide_locked_5.png').resize((int(35 * vw), int(20 * vh))))
guide_1_image = ImageTk.PhotoImage(Image.open('png/guide_1_5.png').resize((int(35 * vw), int(20 * vh))))
guide_2_image = ImageTk.PhotoImage(Image.open('png/guide_2_5.png').resize((int(35 * vw), int(20 * vh))))
guide_3_image = ImageTk.PhotoImage(Image.open('png/guide_3_5.png').resize((int(35 * vw), int(20 * vh))))
guide_4_image = ImageTk.PhotoImage(Image.open('png/guide_4_5.png').resize((int(35 * vw), int(20 * vh))))
guide_5_image = ImageTk.PhotoImage(Image.open('png/guide_5_5.png').resize((int(35 * vw), int(20 * vh))))
guide_exit_image = ImageTk.PhotoImage(Image.open('png/guide_exit_4.png').resize((int(35 * vw), int(20 * vh))))
guide_background = ImageTk.PhotoImage(Image.open('png/guide_background.png').resize((int(101 * vw), int(101 * vh))))
help_background = Label(image=guide_background)#9ED2F4#001D3D#131a28
guides = []
for i in range(6):
    guides.append(Button(borderwidth=0, highlightthickness=0, relief=FLAT,))
########################################################################################################################
def make_help_window():
    temp["cur_stage"] = 5
    help_background.place(x=0, y=0, width=100*vw, height=100*vh)
    for i in range(6):
        x_place = 0
        y_place = 0
        if i % 2 == 0:
            x_place = 10*vw
            y_place = 10*vh + (i/2)*30*vh
        else:
            x_place = 55*vw
            y_place = 10*vh + ((i-1)/2)*30*vh
        guides[i].place(x=x_place, y=y_place, width=int(35*vw), height=int(20*vh))
        match i:
            case 0:
                if player_save["lastlevel"] >= 0:
                    guides[i]["image"] = guide_1_image
            case 1:
                if player_save["lastlevel"] >= 2:
                    guides[i]["image"] = guide_2_image
                else:
                    guides[i]["image"] = guide_locked_image
            case 2:
                if player_save["lastlevel"] >= 4:
                    guides[i]["image"] = guide_3_image
                else:
                    guides[i]["image"] = guide_locked_image
            case 3:
                if player_save["lastlevel"] >= 6:
                    guides[i]["image"] = guide_4_image
                else:
                    guides[i]["image"] = guide_locked_image
            case 4:
                if player_save["lastlevel"] >= 8:
                    guides[i]["image"] = guide_5_image
                else:
                    guides[i]["image"] = guide_locked_image
            case 5:
                guides[i]["image"] = guide_exit_image
                guides[i]["command"] = lambda: [destroy_help_window(), make_main_game_window(temp["cur_task"])]


def destroy_help_window():
    help_background.place_forget()
    for i in range(6):
        guides[i].place_forget()

########################################################################################################################
########################################################################################################################


############################ Создание виджетов для главного экрана с игрой #############################################


play_button_img = ImageTk.PhotoImage(Image.open('png/play_btn.png').resize((int(12.5 * vw), int(12.5 * vh))))
wait_button_img = ImageTk.PhotoImage(Image.open('png/wait_btn.png').resize((int(12.5 * vw), int(12.5 * vh))))
test_button_active_img = ImageTk.PhotoImage(Image.open('png/test_active_btn.png').resize((int(12.5 * vw), int(12.5 * vh))))
test_button_disable_img = ImageTk.PhotoImage(Image.open('png/test_notactive_btn.png').resize((int(12.5 * vw), int(12.5 * vh))))
map_button_img = ImageTk.PhotoImage(Image.open('png/map_btn.png').resize((int(12.5 * vw), int(12.5 * vh))))
help_button_img = ImageTk.PhotoImage(Image.open('png/help_btn.png').resize((int(12.5 * vw), int(12.5 * vh))))
input_label_img = ImageTk.PhotoImage(Image.open('png/input_label.png').resize((int(2 * int(12.5 * vw) - int(1 * vw)), int(2 * vh))))
output_label_img = ImageTk.PhotoImage(Image.open('png/output_label.png').resize((int(2 * int(12.5 * vw) - int(1 * vw)), int(2 * vh))))
verdict_label_img = ImageTk.PhotoImage(Image.open('png/verdict_label.png').resize((int(2 * int(12.5 * vw) - int(1 * vw)), int(2 * vh))))
code_label_img = ImageTk.PhotoImage(Image.open('png/code_label.png').resize((int(100 * vw - 2 * int(12.5 * vw) - int(35 * vw) - int(1 * vw)), int(2 * vh))))
story_label_img = ImageTk.PhotoImage(Image.open('png/story_label.png').resize((int(int(35 * vw) - int(1 * vw)), int(2 * vh))))
input_label = Label(image=input_label_img)
output_label = Label(image=output_label_img)
verdict_label = Label(image=verdict_label_img)
input_txt = Text(font=(font_name, int((font_size + 1) * 0.75)), bg='#000000', fg='#17FF00', insertbackground="#17FF00", state=DISABLED)
output_txt = Text(font=(font_name, int((font_size + 1) * 0.75)), bg='#000000', fg='#17FF00', insertbackground="#17FF00", state=DISABLED)
verdict_txt = Text(font=(font_name, int((font_size + 1) * 0.75)), bg='#000000', fg='#17FF00', insertbackground="#17FF00", state=DISABLED, wrap="word")
scrollbar_input_txt = Scrollbar(orient="vertical", command=input_txt.yview, bg="#444444")
scrollbar_output_txt = Scrollbar(orient="vertical", command=output_txt.yview, bg="#444444")
scrollbar_verdict_txt = Scrollbar(orient="vertical", command=verdict_txt.yview, bg="#444444")
change_mode_button = Button(borderwidth=0, highlightthickness=0, relief=FLAT, image=test_button_disable_img)
play_button = Button(borderwidth=0, highlightthickness=0, relief=FLAT, image=play_button_img)
help_button = Button(borderwidth=0, highlightthickness=0, relief=FLAT, image=help_button_img)
menu_button = Button(borderwidth=0, highlightthickness=0, relief=FLAT, image=map_button_img)
code_label = Label(image=code_label_img)
code_numbering_txt = Text(font="sans-serif 20", bg='#2763a3', fg='white', state='disabled')
code_txt = Text(font=(font_name, font_size), bg='#000000', fg='#17FF00', insertbackground="#17FF00")
font = Font(font=code_txt['font'])
tab = font.measure('    ')
code_txt.config(tabs=tab)


def multiple_yview(*args):
    code_numbering_txt.yview(*args)
    code_txt.yview(*args)


scrollbar_code_txt = Scrollbar(orient="vertical", command=multiple_yview, bg="#444444")
minigame = Frame(bg="black")
story_label = Label(image=story_label_img)
story_txt = Text(font=(font_name, font_size), bg='#000000', fg='#17FF00', insertbackground="#17FF00", wrap="word")
scrollbar_story_txt = Scrollbar(orient="vertical", command=story_txt.yview, bg="#444444")


########################################################################################################################

def make_main_game_window(id):  # Блять, если это тебе придется менять, то земля пухом
    temp["cur_stage"] = 4
    temp["cur_task"] = id
    # Первая колонка
    first_column_label_width = 2 * int(12.5 * vw) - int(1 * vw)
    first_column_label_height = int(2 * vh)
    first_column_txt_width = 2 * int(12.5 * vw) - int(1 * vw)
    first_column_txt_height = (100 * vh - 3 * int(2 * vh) - 2 * int(12.5 * vh)) / 3
    first_column_button_width = 12.5 * vw
    first_column_button_height = 12.5 * vh

    input_label.place(width=first_column_label_width, height=first_column_label_height, x=0, y=0)
    output_label.place(width=first_column_label_width, height=first_column_label_height, x=0, y=first_column_txt_height + first_column_label_height)
    verdict_label.place(width=first_column_label_width, height=first_column_label_height, x=0, y=2 * first_column_txt_height + 2 * first_column_label_height)

    input_txt.place(width=first_column_txt_width, height=first_column_txt_height, x=0, y=first_column_label_height)
    output_txt.place(width=first_column_txt_width, height=first_column_txt_height, x=0, y=1 * first_column_txt_height + 2 * first_column_label_height)
    verdict_txt.place(width=first_column_txt_width, height=first_column_txt_height, x=0, y=2 * first_column_txt_height + 3 * first_column_label_height)

    scrollbar_input_txt.place(width=int(1 * vw), height=first_column_txt_height + first_column_label_height, x=first_column_txt_width, y=0)
    scrollbar_output_txt.place(width=int(1 * vw), height=first_column_txt_height + first_column_label_height, x=first_column_txt_width, y=1 * first_column_txt_height + 1 * first_column_label_height)
    scrollbar_verdict_txt.place(width=int(1 * vw), height=first_column_txt_height + first_column_label_height, x=first_column_txt_width, y=2 * first_column_txt_height + 2 * first_column_label_height)

    change_mode_button.place(width=first_column_button_width, height=first_column_button_height, x=0, y=3 * first_column_txt_height + 3 * first_column_label_height)
    play_button.place(width=first_column_button_width, height=first_column_button_height, x=first_column_button_width, y=3 * first_column_txt_height + 3 * first_column_label_height)
    menu_button.place(width=first_column_button_width, height=first_column_button_height, x=0, y=3 * first_column_txt_height + 3 * first_column_label_height + first_column_button_height)
    help_button.place(width=first_column_button_width, height=first_column_button_height, x=first_column_button_width, y=3 * first_column_txt_height + 3 * first_column_label_height + first_column_button_height)

    input_txt["yscrollcommand"] = scrollbar_input_txt.set
    output_txt["yscrollcommand"] = scrollbar_output_txt.set
    verdict_txt["yscrollcommand"] = scrollbar_verdict_txt.set

    # Вторая колонка
    second_column_label_width = 100 * vw - 2 * int(12.5 * vw) - int(35 * vw) - int(1 * vw)
    second_column_label_height = int(2 * vh)
    second_column_txt_width = 100 * vw - 2 * int(12.5 * vw) - int(35 * vw) - int(1 * vw)
    second_column_txt_height = 100 * vh - int(2 * vh)

    code_label.place(width=second_column_label_width, height=second_column_label_height, x=first_column_label_width + int(1 * vw), y=0)
    code_txt.place(width=second_column_txt_width, height=second_column_txt_height, x=first_column_label_width + int(1 * vw), y=second_column_label_height)
    # code_numbering_txt.place(width=3 * vw, height=98 * vh, x=25 * vw, y=2 * vh)
    scrollbar_code_txt.place(width=int(1 * vw), height=100 * vh, x=first_column_label_width + int(1 * vw) + second_column_txt_width, y=0)

    code_txt["yscrollcommand"] = scrollbar_code_txt.set
    code_txt.insert("0.0", str(player_save["last_code"]))
    # code_numbering_txt["yscrollcommand"] = scrollbar_code_txt.set

    # Третья колонка
    third_column_frame_width = int(35 * vw)
    third_column_frame_height = int(35 * vw)
    third_column_label_width = int(35 * vw) - int(1 * vw)
    third_column_label_height = int(2 * vh)
    third_column_txt_width = int(35 * vw) - int(1 * vw)
    third_column_txt_height = 100 * vh - int(2 * vh) - int(35 * vw)

    minigame.place(width=third_column_frame_width, height=third_column_frame_height, x=first_column_label_width + int(1 * vw) + second_column_label_width + int(1 * vw), y=0)
    story_label.place(width=third_column_label_width, height=third_column_label_height, x=first_column_label_width + int(1 * vw) + second_column_label_width + int(1 * vw), y=third_column_frame_height)
    story_txt.place(width=third_column_txt_width, height=third_column_txt_height, x=first_column_label_width + int(1 * vw) + second_column_label_width + int(1 * vw), y=third_column_frame_height + third_column_label_height)

    scrollbar_story_txt.place(width=int(1 * vw), height=third_column_txt_height + third_column_label_height, x=first_column_label_width + int(1 * vw) + second_column_label_width + int(1 * vw) + third_column_label_width, y=third_column_frame_height)

    minigame["bg"] = "black"
    story_txt["yscrollcommand"] = scrollbar_story_txt.set
    story_txt.insert("0.0", quests[id].text)
    story_txt["state"] = DISABLED
    input_txt["state"] = DISABLED
    output_txt["state"] = DISABLED
    verdict_txt["state"] = DISABLED


def destroy_main_game_window():
    input_txt.delete("1.0", "end")
    output_txt.delete("1.0", "end")
    verdict_txt.delete("1.0", "end")
    input_label.place_forget()
    input_txt["state"] = NORMAL
    input_txt.delete("1.0", "end")
    input_txt.place_forget()
    scrollbar_input_txt.place_forget()
    output_label.place_forget()
    output_txt["state"] = NORMAL
    output_txt.delete("1.0", "end")
    output_txt.place_forget()
    scrollbar_output_txt.place_forget()
    verdict_label.place_forget()
    verdict_txt["state"] = NORMAL
    verdict_txt.delete("1.0", "end")
    verdict_txt.place_forget()
    scrollbar_verdict_txt.place_forget()
    change_mode_button.place_forget()
    play_button.place_forget()
    menu_button.place_forget()
    help_button.place_forget()

    player_save["last_code"] = code_txt.get("1.0", "end")
    code_txt.delete("1.0", "end")
    code_label.place_forget()
    # code_numbering_txt.place_forget()
    code_txt.place_forget()
    scrollbar_code_txt.place_forget()

    story_txt["state"] = NORMAL
    story_txt.delete("1.0", "end")
    minigame.place_forget()
    story_label.place_forget()
    story_txt.place_forget()
    scrollbar_story_txt.place_forget()

    temp["test_mode"] = 0


def click_change_mode_button():
    temp["test_mode"] = int((temp["test_mode"] + 1) % 2)
    print(temp["test_mode"])
    match temp["test_mode"]:
        case 0:
            change_mode_button["image"] = test_button_disable_img
            input_txt.delete("1.0", "end")
            input_txt["state"] = DISABLED

        case 1:
            change_mode_button["image"] = test_button_active_img
            input_txt["state"] = NORMAL


def click_play_button(): #Это просто пиздееееееееец

    temp["time_limit"] = 0
    verdict_txt["state"] = NORMAL
    output_txt["state"] = NORMAL
    input_txt["state"] = NORMAL
    verdict_txt.delete("1.0", "end")

    # Делаем заставку песочных часов
    play_button["image"] = wait_button_img
    win.update_idletasks()

    # Записываем код
    f = open("player_code.cpp", "w")
    code_string = code_txt.get("1.0", "end-1c")
    line = ""
    need_to_insert = False
    for k in range(len(code_string)):
        if code_string[k] == '\n' or code_string[k] == ' ':
            line = ""
        else:
            line += code_string[k]

        if line == 'main':
            need_to_insert = True

        if code_string[k] == '{' and need_to_insert:
            code_string = code_string[:k + 1] + """\n\tfreopen("input.txt", "r", stdin);\n\tfreopen("output.txt", "w", stdout);\n""" + code_string[k + 1:]
            need_to_insert = False
    f.write(code_string)
    f.close()

    # Компилируем и запускаем программу
    os.system("g++ player_code.cpp -o player_program")

    # Если программу не удалось скомпилировать
    if not os.path.exists("player_program"):
        print("COMPILATION_ERROR")
        verdict_txt.insert("1.0","Ой, кажется в программе есть синтаксическая ошибка, так что надо переписать код..")
        verdict_txt["state"] = DISABLED
        input_txt["state"] = DISABLED
        output_txt["state"] = DISABLED
        play_button["image"] = play_button_img
        minigame["bg"] = "red"
    else:
        def stop_player_program():
            for proc in psutil.process_iter():
                if proc.name() == "player_program":
                    proc.kill()
                    print("stop_player_program")
                    temp["time_limit"] = 1


        def start_player_program():
            print("start_player_program")
            os.system("./player_program")

        score = 0
        wrong_test_input = ""
        wrong_test_output = ""
        for i in range(30):
            # Подставляем нужные входные данные
            if temp["test_mode"] == 1:
                f = open("input.txt", "w+")
                print(input_txt.get("1.0", "end"))
                f.write(input_txt.get("1.0", "end"))
                print(open("input.txt", "w+").read())
                f.close()
            else:
                f = open("input.txt", "w+")
                f.write(open("tasks/test/" + str(temp["cur_task"] + 1) + "/gen_input/input" + str(i + 1) + ".txt").read())
                f.close()

            # Мультипоточность для закрытия программы, в случае долгой работы
            Thread(target=start_player_program).start()
            time.sleep(0.2)
            Thread(target=stop_player_program).start()
            time.sleep(0.1)

            # Если решение совпало
            if open("output.txt", "r+").read() == open(
                    "tasks/test/" + str(temp["cur_task"] + 1) + "/gen_output/output" + str(i + 1) + ".txt", "r+").read():
                score += 1
            else:
                if wrong_test_input == "":
                    wrong_test_input = open("input.txt", "r+").read()
                    wrong_test_output = open("output.txt", "r+").read()

            # Заранне остановить проверку всех тестов
            if temp["time_limit"] == 1:
                break

            if temp["test_mode"] == 1:
                break

        output_txt.delete("1.0", "end")
        input_txt.delete("1.0", "end")

        if temp["time_limit"] == 1:
            print("TIME_LIMIT")
            verdict_txt.insert("1.0","Ой, кажется программа выполнялась слишком долго. У лягушек нет такой мощной техники, так что надо упростить код..")
            output_txt.insert("1.0", wrong_test_output)
            input_txt.insert("1.0", wrong_test_input)
            verdict_txt["state"] = DISABLED
            output_txt["state"] = DISABLED
            input_txt["state"] = DISABLED
            minigame["bg"] = "blue"
        elif temp["test_mode"] == 1:
            print("DEBUG_MODE")
            output_txt.insert("1.0", open("output.txt", "r+").read())
            input_txt.insert("1.0", open("input.txt", "r+").read())
            verdict_txt["state"] = DISABLED
            output_txt["state"] = DISABLED
            input_txt["state"] = DISABLED
            minigame["bg"] = "purple"
        elif score == 30:
            print("OKEY")
            verdict_txt.insert("1.0","Ура, это решение прошло все тесты! Вы отлично справились!")
            output_txt.insert("1.0", open("output.txt", "r+").read())
            input_txt.insert("1.0", open("input.txt", "r+").read())
            verdict_txt["state"] = DISABLED
            output_txt["state"] = DISABLED
            input_txt["state"] = DISABLED
            minigame["bg"] = "green"
            player_save["lastlevel"] = max(temp["cur_task"] + 1, player_save["lastlevel"])
        elif score > 0:
            print("WA")
            verdict_txt.insert("1.0", "Это заработало " + str(score) + " из 30 баллов. Еще чуть чуть и вы полностью решите эту задачу!\n\nПервый тест, который не прошел, и ваш ответ будут представлены в полях Входные и Выходные данные")
            output_txt.insert("1.0", wrong_test_output)
            input_txt.insert("1.0", wrong_test_input)
            verdict_txt["state"] = DISABLED
            output_txt["state"] = DISABLED
            input_txt["state"] = DISABLED
            minigame["bg"] = "yellow"
        else:
            print("WA0")
            verdict_txt.insert("1.0", "Это решение не решило ни одного теста, стоит поменять решение\n\nПервый тест, который не прошел, и ваш ответ будут представлены в полях Входные и Выходные данные")
            output_txt.insert("1.0", wrong_test_output)
            input_txt.insert("1.0", wrong_test_input)
            verdict_txt["state"] = DISABLED
            output_txt["state"] = DISABLED
            input_txt["state"] = DISABLED
            minigame["bg"] = "red"


    # Возвращаем все в исходный вид
    play_button["image"] = play_button_img
    temp["time_limit"] = 0
    if os.path.exists("output.txt"):
        os.remove("output.txt")
    if os.path.exists("input.txt"):
        os.remove("input.txt")
    if os.path.exists("player_program"):
        os.remove("player_program")
    if os.path.exists("player_code.cpp"):
        os.remove("player_code.cpp")
    change_mode_button["image"] = test_button_disable_img

########################################################################################################################
########################################################################################################################


startgame_button["command"] = lambda: [make_dialog_window(), destroy_menu_window()]#make_map_window(), destroy_menu_window()]
settings_button["command"] = lambda: [make_settings_window(), destroy_menu_window()]

settings_save_button["command"] = lambda: [save_settings()]
settings_exit_button["command"] = lambda: [make_menu_window(), destroy_settings_window()]


change_mode_button["command"] = lambda: [click_change_mode_button()]
play_button["command"] = lambda: [click_play_button()]
menu_button["command"] = lambda: [destroy_main_game_window(), make_map_window()]
help_button["command"] = lambda: [destroy_main_game_window(), make_help_window()]
exit_button["command"] = exit



#make_dialog_window()
make_menu_window()

win.bind("<KeyPress>", key_pressed)
win.mainloop()

#       #include <bits/stdc++.h>
#
#       using namespace std;
#
#       int main(){
#       	freopen("gen_output.txt", "w", stdout);
#       	int a = 1;
#       	for(int i = 0; i < 10; i++){
#       		cout << a + i << endl;
#       	}
#       }
