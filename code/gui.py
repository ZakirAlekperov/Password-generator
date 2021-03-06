from msilib.schema import Font
from multiprocessing import Value
from pyexpat.errors import messages
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Checkbutton
from turtle import left 
import main


def generate_button_click():
    ischeck = False
    isdigit = False
    if main.check_checboxs_correct(numbers_checkbutton_state.get(),
                                  lowercase_checkbutton_state.get(),
                                  capital_letter_checkbutton_state.get(),
                                  special_symbols_checkbutton_state.get()):
        main.check_checkboxs_value(numbers_checkbutton_state.get(), 
                               lowercase_checkbutton_state.get(),
                               capital_letter_checkbutton_state.get(),
                               special_symbols_checkbutton_state.get())
        ischeck = True
    else: 
        messagebox.showinfo("ERROR", "Выберете символы для пароля")
        ischeck = False
    if main.is_correct_length(number_of_signs_textbox_text.get()):
        isdigit = True
        pass
    else:
        messagebox.showinfo("ERROR", "Длина пароля должна быть числом, меньшим 50")
        isdigit = False
    if ischeck and isdigit:
        password_textbox_text.set(main.password_print(number_of_signs_textbox_text.get(), 
                                                      numbers_checkbutton_state.get(),
                                                      lowercase_checkbutton_state.get(),
                                                      capital_letter_checkbutton_state.get(),
                                                      special_symbols_checkbutton_state.get()))


def copy_button_click():
    MainWindow.clipboard_append(password_textbox_text.get())

def delete_button_click():
    password_textbox.delete(0, END)

MainWindow = Tk() #главное окно
w,h = MainWindow.winfo_screenwidth(), MainWindow.winfo_screenheight()
w = w // 2
w = w - 250
h = h // 2
h = h - 150
MainWindow.geometry('700x200+{}+{}'.format(w, h)) #Начальное положение окна по середине
MainWindow.resizable(False, False)

MainWindow.title("Генератор паролей")

# Метка для поля пароля
password_label = Label(MainWindow, 
                       text="Сгенерированный пароль", 
                       font=("Arial Bold", 10)) 
password_label.grid(columnspan=4, row=0)

# Текстовое поле для пароля
password_textbox_text = StringVar()
password_textbox = Entry(MainWindow, 
                         width=40, 
                         font=("Arial Bold", 15),
                         #state='disabled', 
                         textvariable=password_textbox_text) 
password_textbox.grid(columnspan=4,
                      row=1,
                      padx=5)

#Ввод колличества символов в пароле
number_of_signs_textbox_text = StringVar()
number_of_signs_label = Label(MainWindow, 
                              text="Длина пароля", 
                              font=("Arial Bold", 10), 
                              width=20,
                              )
number_of_signs_label.grid(column=5, 
                           row=0,
                           padx=5,
                           pady=5)
number_of_signs_textbox = Entry(MainWindow,
                                width=4, 
                                font=("Arial Bold", 10),
                                textvariable=number_of_signs_textbox_text)
number_of_signs_textbox.grid(column=6,
                             row=0, 
                             padx=5)
number_of_signs_textbox.focus()

#Использование цифр в пароле
numbers_label = Label(MainWindow, 
                      text="Цифры", 
                      font=("Arial Bold", 10), 
                      width=20, 
                      justify=RIGHT)
numbers_checkbutton_state = BooleanVar()
numbers_checkbutton_state.set(TRUE)
numbers_checkbutton = Checkbutton(MainWindow,
                                  text="", 
                                  variable=numbers_checkbutton_state)
numbers_label.grid(column=5, 
                   row=1)
numbers_checkbutton.grid(column=6, 
                         row=1)

#Использование строчных букв в пароле
lowercase_label = Label(MainWindow,
                        text="Строчные буквы", 
                        font=("Arial Bold", 10), 
                        width=20,justify=LEFT)
lowercase_checkbutton_state = BooleanVar()
lowercase_checkbutton_state.set(TRUE)
lowercase_checkbutton = Checkbutton(MainWindow, 
                                    text="", 
                                    variable=lowercase_checkbutton_state)
lowercase_label.grid(column=5, row=2)
lowercase_checkbutton.grid(column=6, row=2)

#Использование заглавных букв в пароле
capital_letter_label = Label(MainWindow, 
                             text="Заглавные буквы", 
                             font=("Arial Bold", 10), 
                             width=20)
capital_letter_checkbutton_state = BooleanVar()
capital_letter_checkbutton_state.set(TRUE)
capital_letter_checkbutton = Checkbutton(MainWindow, 
                                         text="", 
                                         variable=capital_letter_checkbutton_state)
capital_letter_label.grid(column=5, row=3),
capital_letter_checkbutton.grid(column=6, row=3)

#Использование спец символов
special_symbols_label = Label(MainWindow, 
                              text="Спец. символы", 
                              font=("Arial Bold", 10), 
                              width=20)
special_symbols_checkbutton_state = BooleanVar()
special_symbols_checkbutton_state.set(FALSE)
special_symbols_checkbutton = Checkbutton(MainWindow, 
                                          text="", 
                                          variable=special_symbols_checkbutton_state)
special_symbols_label.grid(column=5, row=4)
special_symbols_checkbutton.grid(column=6, row=4)

#Кнопка генерации пароля
generate_button = Button(MainWindow, 
                         text="Сгеннерировать", 
                         width=62, 
                         padx=4, 
                         pady=8, 
                         command=generate_button_click
                         )
generate_button.grid(columnspan=4, row=2)

#Кнопка копирования пароля
copy_button = Button(MainWindow, 
                     text="Скопировать", 
                     width=30, 
                     padx=2, 
                     pady=8, 
                     command=copy_button_click
                     )
copy_button.grid(columnspan=2,row=3)

#Кнопка очистки поля пароля
delete_button = Button(MainWindow, 
                       text="Очистить поле", 
                       width=30, 
                       padx=2, 
                       pady=8, 
                       command=delete_button_click
                       )
delete_button.grid(column=2, columnspan=2, row=3)

MainWindow.mainloop()