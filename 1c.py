from pynput.keyboard import Key, Controller
from pymouse import PyMouse
import time, sys
import parse
from cv_functions import check_for_error, find_coordinates
import tkinter.messagebox as mb

mouse = PyMouse()
keyboard = Controller()


def main(table_filename):

    print('Starting... Finding fields...')

    x_create, y_create, x_student, y_student, \
    x_docs, y_docs, x_sum, y_sum, x_cat, y_cat = find_coordinates()

    print('All coordinates found.')

    table = parse.ParseTable(table_filename)

    i = 0
    try:
        for data in table.items():
            if "гос" in data[1].get('Категория').lower():
                cat = "13,"
            elif "потер" in data[1].get('Категория').lower():
                cat = "15"
            elif "сирот" in data[1].get('Категория').lower():
                cat = "15"
            elif "малообес" in data[1].get('Категория').lower():
                cat = "13"
            elif "пенсион" in data[1].get('Категория').lower():
                cat = "13"
            elif "инвал" in data[1].get('Категория').lower():
                cat = "13"
            elif "брак" in data[1].get('Категория').lower():
                cat = "15"
            elif "полис" in data[1].get('Категория').lower():
                cat = "14"
            elif "бил" in data[1].get('Категория').lower():
                cat = "14"
            elif "мед" in data[1].get('Категория').lower():
                cat = "14"
            elif "лек" in data[1].get('Категория').lower():
                cat = "14"
            elif "стомат" in data[1].get('Категория').lower():
                cat = "14"
            else:
                cat = "14"

            i+=1
            print (i, " ", cat, " ",  data[1].get('группа').lower(), " ", data[1].get('Категория').lower(), " ", data[1].get('ФИО'), " ",str(data[1].get('Сумма')))
            
            if i > 1:
                mouse.press(x_create, y_create, 1)
                time.sleep(0.3)

            mouse.press(x_student, y_student, 1)

            keyboard.type(data[1].get('ФИО'))
            time.sleep(0.2)
            if check_for_error(x_student, y_student):
                mb.showerror("Error", 'Error found, please input that person manually, after clicking ok, next person will continue input')
                continue

            keyboard.press(Key.enter)
            time.sleep(0.2)
            if check_for_error(x_student, y_student):
                mb.showerror("Error", 'Error found, please input that person manually, after clicking ok, next person will continue input')
                continue

            ##поиск категории
            mouse.press(x_cat, y_cat,1)
            time.sleep(0.2)
            keyboard.type(cat)
            time.sleep(0.6)
            keyboard.press(Key.enter)
            time.sleep(0.1)
            keyboard.press(Key.enter)
            #enter x2
            time.sleep(0.3)
            

            ##сумма
            mouse.press(x_sum, y_sum, 1)
            keyboard.type(str(data[1].get('Сумма')))
            time.sleep(0.2)
            
            ##подтверждающий документ
            mouse.press(x_docs, y_docs, 1)
            time.sleep(0.2)

            mouse.press(x_create, y_create, 1)
            time.sleep(0.5)
            
            
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    if len (sys.argv) < 2 or len (sys.argv) > 2:
        print("Unknown usage")
        exit(1)

    main(sys.argv[1])