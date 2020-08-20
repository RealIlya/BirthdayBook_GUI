from tkinter import *
from tkinter import ttk
import os

version = "v2.1"

Birthday_book = dict()
date_list = list()


def clear():
    input_date.delete(0, END)
    input_last_name.delete(0, END)
    input_first_name.delete(0, END)
    input_patronymic.delete(0, END)


def add():
    date = input_date.get()
    if date in Birthday_book:
        label_info.config(text="! Такая дата рождения уже существует !", fg="red")
    else:
        value = list()
        value.append(input_last_name.get())
        value.append(input_first_name.get())
        value.append(input_patronymic.get())
        Birthday_book[date] = value

        list_date.insert(END, date)

        with open("BirthdayBook.csv", "w") as file:
            for date in Birthday_book:
                value = Birthday_book[date]
                temp = date + ";" + value[0] + ";" + value[1] + \
                       ";" + value[2] + ";" + "\n"
                file.write(temp)


def select_list_date(event):
    w = event.widget
    i = int(w.curselection()[0])
    date = w.get(i)

    value = Birthday_book[date]
    last_name = value[0]
    first_name = value[1]
    patronymic = value[2]

    clear()
    input_date.insert(0, date)
    input_last_name.insert(0, last_name)
    input_first_name.insert(0, first_name)
    input_patronymic.insert(0, patronymic)


window = Tk()
window.title(f"DateBook {version}")
window.geometry("550x240")

label_date = Label(text="Дата рождения")
label_date.grid(row=0, column=0, padx=10, pady=10, sticky="w")

input_date = ttk.Entry()
input_date.grid(row=0, column=1)

label_last_name = Label(text="Фамилия")
label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")

input_last_name = ttk.Entry()
input_last_name.grid(row=1, column=1)

label_first_name = Label(text="Имя")
label_first_name.grid(row=2, column=0, padx=10, pady=5, sticky="w")

input_first_name = ttk.Entry()
input_first_name.grid(row=2, column=1)

label_patronymic = Label(text="Отчество")
label_patronymic.grid(row=3, column=0, padx=10, pady=5, sticky="w")

input_patronymic = ttk.Entry()
input_patronymic.grid(row=3, column=1)

label_info = Label(text="Программа готова к работе...")
label_info.grid(row=5, column=0, columnspan=4)

button_add = ttk.Button(text="Добавить", command=add)
button_add.grid(row=1, column=2, padx=38)

button_clear = ttk.Button(text="Удалить", command=clear)
button_clear.grid(row=3, column=2, padx=38)

label_list_date = Label(text="Список дней рождений")
label_list_date.grid(row=0, column=3)

list_date = Listbox()
list_date.grid(row=1, column=3, rowspan=5)

# <<ListboxSelect>> связывает Listbox и поля ввода
list_date.bind('<<ListboxSelect>>', select_list_date)

if os.path.exists("BirthdayBook.csv"):
    with open("BirthdayBook.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split(";")  # split игнорирует ;
            # (номер);(имя);(фамилия);(отчество);(адрес)
            date = elements[0]
            last_name = elements[1]
            first_name = elements[2]
            patronymic = elements[3]

            value = list()
            value.append(last_name)
            value.append(first_name)
            value.append(patronymic)
            Birthday_book[date] = value

            list_date.insert(END, date)

window.mainloop()
