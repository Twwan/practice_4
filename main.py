from tkinter import *
from tkinter import colorchooser
from idlelib.tooltip import Hovertip
#from tkinter.tix import *
from PIL import ImageTk


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = 'black'
        self.mode = 'Brush'
        self.brush_size = 2
        self.setUI()

        self.x = self.y = 0

        self.rect = None

        self.start_x = None
        self.start_y = None

    def tools(self, type_brush):
        self.mode = type_brush

    def palette(self):
        color = colorchooser.askcolor()
        color = color[1]  # получаем как кортеж и берем первый эл.
        self.set_color(color)

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        if self.mode == 'Brush':
            self.canv.create_oval(event.x - self.brush_size,  # заменив на плюс, можно получить каллиграфическую кисть
                                  event.y - self.brush_size,
                                  event.x + self.brush_size,
                                  event.y + self.brush_size,
                                  fill=self.color, outline=self.color)

    def modeBrush(self, event):
        if self.mode == 'Brush':
            self.canv.bind('<B1-Motion>', self.draw)
        else:
            self.canv.bind('<ButtonPress-1>', self.modeBrush)
            self.canv.bind('<B1-Motion>', self.on_move_press)
            self.canv.bind('<ButtonRelease-1>', self.on_button_release)

            self.start_x = event.x
            self.start_y = event.y
            # x1 - откуда рисовать по x. y1 - откуда рисовать по y
            # x2 - до куда рисовать по x. y2 - до куда рисовать по y
            if self.mode == 'RectangleBrush':  # прямоугольник
                self.rect = self.canv.create_rectangle(self.x, self.y, 1, 1, width=self.brush_size, outline=self.color)
            if self.mode == 'OvalBrush':  # овал/круг
                self.rect = self.canv.create_oval(self.x, self.y, 1, 1, width=self.brush_size, outline=self.color)
            if self.mode == 'LineBrush':  # прямая
                self.rect = self.canv.create_line(self.x, self.y, 1, 1, width=self.brush_size, fill=self.color)
            if self.mode == 'TriangleBrush':  # треугольник (в будущем)
                # self.rect = self.create_polygon([x, y], [x1, y1], [x2, y2]
                pass

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)
        # отслеживаем начальные и конечные корды для отрисовки фигуры
        self.canv.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_button_release(self, event):
        pass

    def setUI(self):

        self.parent.title('PAINt')  # Устанавливаем название окна
        self.pack(fill=BOTH, expand=1)  # Размещаем активные элементы на родительском окне

        # Даём полю возможность растягиваться

        self.columnconfigure(14, weight=1)
        self.rowconfigure(4, weight=1)

        self.canv = Canvas(self, bg='white', cursor='cross')  # Создаем поле для рисования, устанавливаем белый фон
        self.canv.grid(row=4, column=0, columnspan=15, padx=5, pady=5, sticky=E+W+S+N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна

        self.canv.bind('<B1-Motion>', self.draw)

        color_lab = Label(self, text='Color')  # Создаем метку для кнопок изменения цвета кисти
        color_lab.grid(row=3, column=2, padx=6)  # Устанавливаем созданную метку в первый ряд и первую колонку, задаем горизонтальный отступ в 6 пикселей

        # Рамки

        fra1 = Frame(self, width=100, height=20, bg='#F0F0F0')
        fra1.grid(row=0, column=0)

        fra2 = Frame(self, width=50, height=20, bg='#F0F0F0')
        fra2.grid(row=0, column=4)

        fra3 = Frame(self, width=50, height=20, bg='#F0F0F0')
        fra3.grid(row=0, column=10)


        # Цвет

        red_btn = Button(self, width=5, bg='red', command=lambda: self.set_color('red'))  # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов), функция вызываемая при нажатии кнопки.
        red_btn.grid(row=0, column=1)  # Устанавливаем кнопку

        green_btn = Button(self, width=5, bg='green', command=lambda: self.set_color('green'))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, width=5, bg='blue', command=lambda: self.set_color('blue'))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, width=5, bg='black', command=lambda: self.set_color('black'))
        black_btn.grid(row=1, column=2)

        white_btn = Button(self, width=5, bg='white', command=lambda: self.set_color('white'))
        white_btn.grid(row=1, column=1)

        yellow_btn = Button(self, width=5, bg='yellow', command=lambda: self.set_color('yellow'))
        yellow_btn.grid(row=1, column=3)

        palette_btn = Button(self, text='Palette', width=5, command=self.palette)
        palette_btn.grid(row=2, column=2)

        clear_btn = Button(self, text='Clear all', width=10, command=lambda: self.canv.delete('all'))
        clear_btn.grid(row=5, column=0)

        # Размер

        size_lab = Label(self, text='Size')
        size_lab.grid(row=3, column=8, padx=5)

        one_btn = Button(self, text='2px', width=5, command=lambda: self.set_brush_size(2))
        one_btn.grid(row=0, column=7)

        two_btn = Button(self, text='5px', width=5, command=lambda: self.set_brush_size(5))
        two_btn.grid(row=0, column=8)

        five_btn = Button(self, text='7px', width=5, command=lambda: self.set_brush_size(7))
        five_btn.grid(row=0, column=9)

        seven_btn = Button(self, text='10px', width=5, command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=7)

        ten_btn = Button(self, text='20px', width=5, command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=8)

        twenty_btn = Button(self, text='30px', width=5, command=lambda: self.set_brush_size(30))
        twenty_btn.grid(row=1, column=9)

        # Инструменты

        tool_lab = Label(self, text='Tools')
        tool_lab.grid(row=3, column=12, padx=5)

        brush_btn = Button(self, text='Brush', width=8, command=lambda:
        [self.tools('Brush'), self.canv.bind('<B1-Motion>', self.modeBrush)])
        brush_btn.grid(row=1, column=12)

        line_btn = Button(self, text='Line', width=8, command=lambda:
        [self.tools('LineBrush'), self.canv.bind('<B1-Motion>', self.modeBrush)])
        line_btn.grid(row=0, column=11)

        rectangle_btn = Button(self, text='Rectangle', width=8, command=lambda:
        [self.tools('RectangleBrush'), self.canv.bind('<ButtonPress-1>', self.modeBrush)])
        rectangle_btn.grid(row=0, column=12)

        oval_btn = Button(self, text='Circle', width=8, command=lambda:
        [self.tools('OvalBrush'), self.canv.bind('<ButtonPress-1>', self.modeBrush)])
        oval_btn.grid(row=0, column=13)

        # Тултипы

        Hovertip(red_btn, 'Красный')
        Hovertip(green_btn, 'Зелёный')
        Hovertip(blue_btn, 'Синий')
        Hovertip(white_btn, 'Белый')
        Hovertip(black_btn, 'Чёрный')
        Hovertip(yellow_btn, 'Жёлтый')
        Hovertip(palette_btn, 'Палитра')

        Hovertip(brush_btn, 'Кисть')
        Hovertip(rectangle_btn, 'Прямоугольник')
        Hovertip(oval_btn, 'Овал')
        Hovertip(line_btn, 'Линия')


def main():
    root = Tk()
    root.geometry('1080x720')
    root.minsize(800, 600)
    app = Paint(root)

    root.mainloop()


if __name__ == '__main__':
    main()


# Что добавить:
# Картинки фигурам #image = ImageTk.PhotoImage(file='')
# Отображение выбранных кнопок
# Ввод текста(?)
# Тултипы
# ScrollBar
# Меню. Проработать сохранить, открыть и пр.
# Отмена действий(?)
#
#
#
#


