from tkinter import *


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def click(self, btns, n):
        for j in range(len(btns)):
            if j != n:
                btns[j].configure(text='')
            else:
                btns[j].configure(text='X')

    def setUI(self):

        self.parent.title("Pythonicway PyPaint")  # Устанавливаем название окна
        self.pack(fill=BOTH, expand=1)  # Размещаем активные элементы на родительском окне

        self.columnconfigure(9, weight=1) # Даем седьмому столбцу возможность растягиваться, благодаря чему кнопки не будут разъезжаться при ресайзе
        self.rowconfigure(2, weight=1) # То же самое для третьего ряда

        self.canv = Canvas(self, bg="white")  # Создаем поле для рисования, устанавливаем белый фон
        self.canv.pack(expand=1, fill=BOTH)  # Прикрепляем канвас методом pack. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна
        self.canv.bind("<B1-Motion>", self.draw) # Привязываем обработчик к канвасу. <B1-Motion> означает "при движении зажатой левой кнопки мыши" вызывать функцию draw

        color_lab = Label(self, text="Color: ") # Создаем метку для кнопок изменения цвета кисти
        color_lab.pack(side=LEFT) # Устанавливаем созданную метку в первый ряд и первую колонку, задаем горизонтальный отступ в 6 пикселей

        red_btn = Button(self, width=5, bg='red',command=lambda: self.set_color('red')) # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов), функция вызываемая при нажатии кнопки.
        red_btn.pack(side=LEFT) # Устанавливаем кнопку

        # Кнопочки

        green_btn = Button(self, width=5, bg='green', command=lambda: self.set_color("green"))
        green_btn.pack(side=LEFT)

        blue_btn = Button(self, width=5, bg='blue', command=lambda: self.set_color("blue"))
        blue_btn.pack(side=LEFT)

        black_btn = Button(self, width=5, bg='black', command=lambda: self.set_color("black"))
        black_btn.pack(side=LEFT)

        white_btn = Button(self, width=5, bg='white', command=lambda: self.set_color("white"))
        white_btn.pack(side=LEFT)

        yellow_btn = Button(self, width=5, bg='yellow', command=lambda: self.set_color("yellow"))
        yellow_btn.pack(side=LEFT)

        clear_btn = Button(self, text="Clear all", width=10, command=lambda: self.canv.delete("all"))
        clear_btn.pack(side=LEFT)
############################################
        size_lab = Label(self, text="Brush size: ")
        size_lab.pack(side=LEFT)

        one_btn = Button(self, text="2", width=5, command=lambda: self.set_brush_size(2))
        one_btn.pack(side=LEFT)

        two_btn = Button(self, text="5", width=5, command=lambda: self.set_brush_size(5))
        two_btn.pack(side=LEFT)

        five_btn = Button(self, text="7", width=5, command=lambda: self.set_brush_size(7))
        five_btn.pack(side=LEFT)

        seven_btn = Button(self, text="10", width=5, command=lambda: self.set_brush_size(10))
        seven_btn.pack(side=LEFT)

        ten_btn = Button(self, text="12", width=5, command=lambda: self.set_brush_size(20))
        ten_btn.pack(side=LEFT)

        twenty_btn = Button(self, text="15", width=5, command=lambda: self.set_brush_size(50))
        twenty_btn.pack(side=LEFT)

        btns = [red_btn, green_btn]


def main():
    root = Tk()
    root.geometry("1080x720")
    root.minsize(800, 600)
    app = Paint(root)

    root.mainloop()


if __name__ == '__main__':
    main()