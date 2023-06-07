from tkinter import *
from tkinter import ttk
from datetime import datetime

def show_bookings():
    with open(r'C:\Users\ilyas\Desktop\output.txt', 'r', encoding="utf8") as f_in:
        data = f_in.readlines()
    bookings_list = []
    for line in data:
        if line.strip():
            values = line.strip().split()
            if len(values) >= 4:
                date = values[0]
                surname = values[1]
                room = values[2]
                category = values[3]
                bookings_list.append((date, surname, room, category))
    bookings_table.delete(*bookings_table.get_children())
    for booking in bookings_list:
        bookings_table.insert(parent='', index='end', values=booking)

def sort_table():
    with open(r'C:\Users\ilyas\Desktop\output.txt', 'r', encoding="utf8") as f_in:
        data = f_in.readlines()
    bookings_list = []
    for line in data:
        if line.strip():
            values = line.strip().split()
            if len(values) >= 4:
                date = values[0]
                surname = values[1]
                room = values[2]
                category = values[3]
                bookings_list.append((date, surname, room, category))

    sorted_bookings = []
    if var.get() == 1:  # Сортировка по дате
        for booking in bookings_list:
            try:
                date = datetime.strptime(booking[0], "%d.%m.%Y")
                sorted_bookings.append((date, booking))
            except ValueError:
                pass  # Пропускаем строки, которые не являются датами
        sorted_bookings = sorted(sorted_bookings, key=lambda x: x[0])
        sorted_bookings = [booking[1] for booking in sorted_bookings]
        bookings_table.heading('Дата', text='Дата (по дате)')
    elif var.get() == 2:  # Сортировка по номеру
        sorted_bookings = sorted(bookings_list, key=lambda x: x[2])
        bookings_table.heading('Дата', text='Дата (по номеру)')
    elif var.get() == 3:  # Сортировка по категории
        sorted_bookings = sorted(bookings_list, key=lambda x: x[3])
        bookings_table.heading('Дата', text='Дата (по категории)')

    bookings_table.delete(*bookings_table.get_children())
    for booking in sorted_bookings:
        bookings_table.insert(parent='', index='end', values=booking)

root = Tk()
root.title("Hotel")
root.geometry("800x400")

var = IntVar()
var.set(0)
rad1 = Radiobutton(root, text='По дате', variable=var, value=1)
rad2 = Radiobutton(root, text='По номеру', variable=var, value=2)
rad3 = Radiobutton(root, text='По категории', variable=var, value=3)

bookings_table = ttk.Treeview(root, columns=('Дата', 'Фамилия', 'Номер', 'Категория'), show='headings')
bookings_table.heading('Дата', text='Дата')
bookings_table.heading('Фамилия', text='Фамилия')
bookings_table.heading('Номер', text='Номер')
bookings_table.heading('Категория', text='Категория')
bookings_table.pack(fill=BOTH, expand=True)

bookings_table.column('Дата', anchor='center')
bookings_table.column('Фамилия', anchor='center')
bookings_table.column('Номер', anchor='center')
bookings_table.column('Категория', anchor='center')

bookings_table.heading('Дата', text='Дата', anchor='center')
bookings_table.heading('Фамилия', text='Фамилия', anchor='center')
bookings_table.heading('Номер', text='Номер', anchor='center')
bookings_table.heading('Категория', text='Категория', anchor='center')

btn = Button(root, text="Вывести данные", command=show_bookings)
btn_sort = Button(root, text="Сортировать", command=sort_table)

rad1.pack()
rad2.pack()
rad3.pack()
btn.pack()
btn_sort.pack()
root.mainloop()
