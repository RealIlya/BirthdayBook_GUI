from tkinter import *
from tkinter import ttk
import os

version = "v1"

phone_book = dict()
tel_list = list()


def clear():
    input_tel.delete(0, END)
    input_last_name.delete(0, END)
    input_first_name.delete(0, END)
    input_patronymic.delete(0, END)
    input_address.delete(0, END)


def add():
    tel = input_tel.get()
    if tel in phone_book:
        label_info.config(text="! Такой номер уже существует !", fg="red")
    else:
        value = list()
        value.append(input_last_name.get())
        value.append(input_first_name.get())
        value.append(input_patronymic.get())
        value.append(input_address.get())
        phone_book[tel] = value

        list_tel.insert(END, tel)


def select_list_tel(event):
    w = event.widget
    i = int(w.curselection()[0])
    tel = w.get(i)

    value = phone_book[tel]
    last_name = value[0]
    first_name = value[1]
    patronymic = value[2]
    address = value[3]

    clear()
    input_tel.insert(0, tel)
    input_last_name.insert(0, last_name)
    input_first_name.insert(0, first_name)
    input_patronymic.insert(0, patronymic)
    input_address.insert(0, address)


window = Tk()
window.title(f"PhoneBook {version}")
window.geometry("550x240")

label_tel = Label(text="Дата рождения")
label_tel.grid(row=0, column=0, padx=10, pady=5, sticky="w")

input_tel = ttk.Entry()
input_tel.grid(row=0, column=1)

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

input_address = ttk.Entry()
input_address.grid(row=4, column=1, pady=10)

label_info = Label(text="Программа готова к работе...")
label_info.grid(row=5, column=0, columnspan=4)

button_add = ttk.Button(text="Добавить", command=add)
button_add.grid(row=1, column=2, padx=38)

button_clear = ttk.Button(text="Удалить", command=clear)
button_clear.grid(row=3, column=2, padx=38)

label_list_tel = Label(text="Список дней рождений")
label_list_tel.grid(row=0, column=3)

list_tel = Listbox()
list_tel.grid(row=1, column=3, rowspan=4)

# <<ListboxSelect>> связывает Listbox и поля ввода
list_tel.bind('<<ListboxSelect>>', select_list_tel)

if os.path.exists("PhoneBook.csv"):
    with open("PhoneBook.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split(";")  # split игнорирует ;
            # (номер);(имя);(фамилия);(отчество);(адрес)
            tel = elements[0]
            last_name = elements[1]
            first_name = elements[2]
            patronymic = elements[3]
            address = elements[4]

            value = list()
            value.append(last_name)
            value.append(first_name)
            value.append(patronymic)
            value.append(address)
            phone_book[tel] = value

            list_tel.insert(END, tel)

window.mainloop()
