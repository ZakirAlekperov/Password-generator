from tkinter import *


MainWindow = Tk() #главное окно
w,h = MainWindow.winfo_screenwidth(), MainWindow.winfo_screenheight()
w = w // 2
w = w - 250
h = h // 2
h = h - 150
MainWindow.geometry('500x300+{}+{}'.format(w, h)) #Начальное положение окна по середине

MainWindow.title("Генератор паролей")


password_label = Label(MainWindow, text="Сгенерированный пароль") # Метка для поля пароля
password_label.grid(column=0, row=0)




MainWindow.mainloop()