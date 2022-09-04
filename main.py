import tkinter as tk    #Импорт библиотеки ТКинтер
from tkinter import ttk    #Модуль для виджета
#from tkinter import Image, ImageTk
import sqlite3

class Main(tk.Frame):                #Класс главного окна
    #Функция конструктора
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()
#Инцелизация графического интерфейса
    def init_main(self):

        toolbar = tk.Frame(bg='#d7d8e0', bd=2)    #Создание  бара и цвет фона bg - цвет фона bd - граница
        toolbar.pack(side=tk.TOP, fill=tk.X)        #Отображение тулбара первый аргумент закреп в верхней части экрана и второй растянет его по горизонтали

        self.add_img = tk.PhotoImage(file='ic_add.png')   #Класс который умеет читать + имя или путь к файлу
        btn_open_dialog = tk.Button(toolbar, text='Добавить запись', command=self.open_dilog, bg='#d7d8e0', bd=0, compound=tk.TOP, image=self.add_img)     #Код добавления кнопки и отрибуты(какому фрему пренадлежит(toolbar), текст кнопки, позиция, какая фунция при нажатии(открытия дочернего окна), фон кнопки, отступ, свойсво compoint, переменная иконки)
        btn_open_dialog.pack(side=tk.LEFT)  #РАсположение кнопки

        self.update_img = tk.PhotoImage(file='ic_edit.png')
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#d7d8e0', bd=0, image=self.update_img, compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='ic_delete.png')
        btn_delete_dialog = tk.Button(toolbar, text='Удалить', bg='#d7d9e0', bd=0, image=self.delete_img, compound=tk.TOP, command=self.delete_record)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='ic_search.png')
        btn_search_dialog = tk.Button(toolbar, text='Поиск', bg='#d7d9e0', bd=0, image=self.search_img, compound=tk.TOP, command=self.open_search_dialog)
        btn_search_dialog.pack(side=tk.LEFT)

        self.report_img = tk.PhotoImage(file='ic_report.png')
        btn_report_dialog = tk.Button(toolbar, text='Debug', bg='#d7d9e0', bd=0, image=self.report_img, compound=tk.TOP, command=self.open_report_dialog)
        btn_report_dialog.pack(side=tk.RIGHT)


        self.refresh_img = tk.PhotoImage(file='ic_refresh.png')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d9e0', bd=0, image=self.refresh_img, compound=tk.TOP,
                                     command=self.view_records)
        self.test_img = tk.PhotoImage(file='ic_test.png')
        btn_test_dialog = tk.Button(toolbar, text='Тест', bg='#d7d8e0', bd=0, image=self.test_img,
                                    compound=tk.TOP, command=self.open_test_window)
        btn_test_dialog.pack(side=tk.LEFT)

        btn_refresh.pack(side=tk.LEFT)
                                       #Колонки в таблицы                          #высота колонки
        self.tree = ttk.Treeview(self, columns=('ID', 'engineer', 'date', 'organization', 'installation_location', 'model', 'serial_number', 'application_content',
                                                'number_of_copies', 'list_of_works', 'to_replace_name', 'tochangepn', 'quantity',
                                                'parts_installation', 'note'), height=15, show='headings') #Добавление виджета(таблицы) на гланое окно программы
                       #Название #Размер  #расположение в ячейке
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('engineer', width=200, anchor=tk.CENTER) #Параметры колонки width=ширина
        self.tree.column('date', width=150, anchor=tk.CENTER)
        self.tree.column('organization', width=100, anchor=tk.CENTER)
        self.tree.column('installation_location', width=150, anchor=tk.CENTER)
        self.tree.column('model', width=150, anchor=tk.CENTER)
        self.tree.column('serial_number', width=150, anchor=tk.CENTER)
        self.tree.column('application_content', width=250, anchor=tk.CENTER)
        self.tree.column('number_of_copies', width=100, anchor=tk.CENTER)
        self.tree.column('list_of_works', width=200, anchor=tk.CENTER)
        self.tree.column('to_replace_name', width=150, anchor=tk.CENTER)
        self.tree.column('tochangepn', width=150, anchor=tk.CENTER)
        self.tree.column('quantity', width=50, anchor=tk.CENTER)
        self.tree.column('parts_installation', width=300, anchor=tk.CENTER)
        self.tree.column('note', width=150, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID') #Добавление названия к колонкам
        self.tree.heading('engineer', text='Инженер')
        self.tree.heading('date', text='Дата')
        self.tree.heading('organization', text='Организация')
        self.tree.heading('installation_location', text='Место установки')
        self.tree.heading('model', text='Модель')
        self.tree.heading('serial_number', text='Сер №')
        self.tree.heading('application_content', text='Содержание заявки')
        self.tree.heading('number_of_copies', text='Кол-во копии')
        self.tree.heading('list_of_works', text='Перечень работ')
        self.tree.heading('to_replace_name', text='К замене наименование')
        self.tree.heading('tochangepn', text='К замене P/N')
        self.tree.heading('quantity', text='Кол-во')
        self.tree.heading('parts_installation', text='Установка деталей')
        self.tree.heading('note', text='Примечание')

        #Скроллбар по горизонтали для главной таблицы(Бета)
        #self.scroll = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        #self.scroll.pack(side='bottom', fill='x', = '100')
        #self.tree.configure(xscrollcommand=scroll.set)

        self.tree.pack(side=tk.TOP) #Отображение Таблицы

        scroll = tk.Scrollbar(self, command=self.tree.xview, orient='horizontal')
        scroll.pack(side=tk.TOP, fill=tk.X)
        self.tree.configure(xscrollcommand=scroll.set)



         #Запись данных
    def records(self, engineer, date, organization, installation_location, model, serial_number,
                application_content, number_of_copies, list_of_works, to_replace_name, tochangepn, quantity, parts_installation, note):
        self.db.insert_data(engineer, date, organization, installation_location, model, serial_number,
                            application_content, number_of_copies, list_of_works, to_replace_name, tochangepn, quantity, parts_installation, note)
        self.view_records()
           #Редактор данных
    def update_record(self, engineer, date, organization, installation_location, model, serial_number,
                      application_content, number_of_copies, list_of_works, to_replace_name, tochangepn, quantity, parts_installation, note):
        self.db.c.execute('''UPDATE base_engineer SET engineer=?, date=?, organization=?, installation_location=?, model=?,
        serial_number=?, application_content=?, number_of_copies=?, list_of_works=?, to_replace_name=?, tochangepn=?, quantity=?,
        parts_installation=?, note=? WHERE ID=?''', (engineer, date, organization, installation_location, model, serial_number,
                                                    application_content, number_of_copies, list_of_works, to_replace_name, tochangepn, quantity, parts_installation, note,
                                                     self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()    #Сохранении изменений в БД
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM base_engineer''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('',  'end', values = row) for row in self.db.c.fetchall()]

    #Удаление записи
    def delete_record(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM base_engineer WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()
        #Поиск данных
    def search_records(self, engineer):
        engineer = ('%' + engineer + '%', )
        self.db.c.execute('''SELECT * FROM base_engineer WHERE engineer LIKE ?''', engineer)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_search_dialog(self):
        Search()




    def open_dilog(self):    #Вызов дочеренго окна
        Child()

    def open_update_dialog(self):
        Update()

    def open_report_dialog(self):
        Report()


    def open_test_window(self):
        TestWindow()


#Создание дочерного окна
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()      #Вызов функции init_child
        self.view = app

        #im_pribters = tk.PhotoImage(file='im_printer.png')
        #label = tk.Label(self, image=im_pribters)
        #label.image_ref = im_pribters
        # label.pack()
        #label.place(x=790, y=20, )


    def  init_child(self):
        self.title('Добавить запись')    #Добавление окна и название
        self.geometry("1000x250+400+300")    #Размер дочернего окна
        self.resizable(False, False)            #Запретить изменять окно

        im_pribters = tk.PhotoImage(file='im_printer.png')
        label = tk.Label(self, image=im_pribters)
        label.image_ref = im_pribters
        # label.pack()
        label.place(x=790, y=20, )

        label_title_organization = tk.Label(self, text='Организация')
        label_title_organization.place(x=130, y=5)
        label_engineer = tk.Label(self, text='Инженер') #Добавления тексат на окно
        label_engineer.place(x=20, y=30)
        label_date = tk.Label(self, text='Дата')
        label_date.place(x=20, y=60)
        label_organization = tk.Label(self, text='Организация')
        label_organization.place(x=20, y=90)
        label_installation_location = tk.Label(self, text='Место установки')
        label_installation_location.place(x=20, y=120)
        label_model = ttk.Label(self, text='Модель')
        label_model.place(x=300, y=30)
        label_serial_number = ttk.Label(self, text='Сер №')
        label_serial_number.place(x=300, y=60)
        label_application_content = ttk.Label(self, text='Содержание заявки')
        label_application_content.place(x=20, y=150)
        label_number_of_copies = ttk.Label(self, text='Кол-во копии')
        label_number_of_copies.place(x=300, y=90)
        label_list_of_works = ttk.Label(self, text='Перечнь работ')
        label_list_of_works.place(x=300, y=120)
        label_to_replace_name = ttk.Label(self, text='К замене наименование')
        label_to_replace_name.place(x=563, y=30)
        label_tochangepn = ttk.Label(self, text='К замене P/N')
        label_tochangepn.place(x=563, y=60)
        label_quantity = ttk.Label(self, text= 'Кол-во')
        label_quantity.place(x=563, y=90)
        label_parts_installation = ttk.Label(self, text='Установка деталей')
        label_parts_installation.place(x=413, y=150)
        label_note = ttk.Label(self, text='Примечание')
        label_note.place(x=20, y=180)

        #im_printer_label = tk.PhotoImage(file='im_printer.png')
        #label_im_printer = tk.Label(self, image = im_printer_label)
        #label_im_printer.place(x=50, y=50)
        #label_im_printer.pack()







        #Элементы для поля ввода
        self.entry_engineer = ttk.Entry(self)     #Поле для ввода данных
        self.entry_engineer.place(x=150, y=90, width=128)  #Расположение

        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x=150, y=60, width=128)

        #Виджет выпадение окна(combobox)
        self.combobox = ttk.Combobox(self, values=[u'Акатов', u'Иванов']) #Свойсва выпадения списка
        self.combobox.current(0) #Выбранный элемент по дефолту в комбобоксе 0=первое значение
        self.combobox.place(x=150, y=30, width=128) #Расположение комбобокса

        self.entry_organization = ttk.Entry(self)

        self.entry_installation_location = ttk.Entry(self)
        self.entry_installation_location.place(x= 150, y= 120, width=128)

        self.entry_model = ttk.Entry(self)
        self.entry_model.place(x=413, y=30, width=128)

        self.entry_serial_number = ttk.Entry(self)
        self.entry_serial_number.place(x=413, y=60, width=128)

        self.entry_application_content = ttk.Entry(self)
        self.entry_application_content.place(x=150, y=150, width=240)

        self.entry_number_of_copies = ttk.Entry(self)
        self.entry_number_of_copies.place(x=413, y=90, width=128)

        self.entry_list_of_works = ttk.Entry(self)
        self.entry_list_of_works.place(x=413, y=120, width=450)

        self.entry_to_replace_name = ttk.Entry(self)
        self.entry_to_replace_name.place(x=730, y=30, width=128)

        self.entry_tochangepn = ttk.Entry(self)
        self.entry_tochangepn.place(x=730, y=60, width=128)

        self.entry_quantity = ttk.Entry(self)
        self.entry_quantity.place(x=730, y=90, width=40)

        self.entry_parts_installation = ttk.Entry(self)
        self.entry_parts_installation.place(x=563, y=150, width=128)

        self.entry_note = ttk.Entry(self)
        self.entry_note.place(x=150, y=180, width=713)

        #self.im_pribters = tk.PhotoImage(file= 'ic_report.png')
        #im_pribters = tk.PhotoImage(file='im_printer.png')
        #label = tk.Label(self, image=im_pribters)
        #label.image_ref = im_pribters
        #label.pack()
        #label.place(x=790, y=20, )

        #self.add_img = tk.PhotoImage(file='im_printer.png')
        #canvas = tk.Canvas(self, height=100, width=400)
        #image = Image.open('im_printer.png')
        #photo = ImageTk.PhotoImage('im_printer.png')
        #image = canvas.create_image(0, 0, anchor='nw',image=photo)
        #canvas.grid(row=2, column=1)
        #self.mainloop()

        #im_printer = tk.PhotoImage(file='ic_edit.png') #Присваивание к обекту файл(картинка)
        #im_printer = im_printer.subsample(11, 7) #Маштабирование
        #im_printer_label = tk.Label(self, text='')   #Метка дл изображения
        #im_printer_label.image = im_printer #Запись в теку label изображение
        #im_printer_label['image'] = im_printer_label.image #запись в отрибуты
        #im_printer_label.place(x=936, y=50)












         #Добавления кнопки
        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=900, y=220) #Расположение кнопки

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=790, y=220)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.combobox.get(), self.entry_date.get(), self.entry_engineer.get(), self.entry_installation_location.get(),
                                                                  self.entry_model.get(), self.entry_serial_number.get(), self.entry_application_content.get(),
                                                                  self.entry_number_of_copies.get(), self.entry_list_of_works.get(), self.entry_to_replace_name.get(),
                                                                  self.entry_tochangepn.get(), self.entry_quantity.get(), self.entry_parts_installation.get(),
                                                                  self.entry_note.get())) #Срабатывания на левую кнопку мыши








        self.grab_set()                      #Перехзват окном все события остальных окон
        self.focus_set()               #Охватывает и удерживает окно


#окно репортов багов и тестов
class Report(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_report()
        self.view = app



    def init_report(self):
        button_add = ttk.Button(self, text='Добавить', command=self.open_dilog)
        button_add.olace(x=150, y=100)


        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=900, y=220)



        self.tree = ttk.Treeview(self, columns=(
        'ID', 'engineer', 'model'), height=15, show='headings')

        self.tree_report = ttk.Treeview(self, columns=('ID', 'engineer', 'model'), height=15, show='headings')
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('engineer', width=200, anchor=tk.CENTER)
        self.tree.column('model', width=150, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('engineer', text='Инженер')
        self.tree.heading('model', text='Модель')

        self.tree.pack(side=tk.TOP)

        self.title('Тесты и репорты')
        self.geometry('1000x430+300+200')
        self.resizable(False, False)



    def open_dilog(self):
        Child()


class TestWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_test_window()
        self.viev =app

    def init_test_window(self):
        import Test




    #Класс редактор(чаийд)
class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()
#Добавление кнопки
    def init_edit(self):
        self.title('Редактировать позиции')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=820, y=220)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.combobox.get(), self.entry_date.get(), self.entry_engineer.get(), self.entry_installation_location.get(),
                                                                  self.entry_model.get(), self.entry_serial_number.get(), self.entry_application_content.get(),
                                                                  self.entry_number_of_copies.get(), self.entry_list_of_works.get(), self.entry_to_replace_name.get(),
                                                                  self.entry_tochangepn.get(), self.entry_quantity.get(), self.entry_parts_installation.get(),
                                                                  self.entry_note.get()))
        #Убрать кнопку ок
        self.btn_ok.destroy()
          #Подтягивание данных в окно редактировать
    def default_data(self):
        self.db.c.execute('''SELECT * FROM base_engineer WHERE id=?''', (self.view.tree.set(self.view.tree.selection()[0],'#1'),))
        row = self.db.c.fetchone()
        #self.combobox.insert(0, row[1])
        if row[1] != 'Акатов':
            self.combobox.current(1)
        self.entry_date.insert(0, row[2])
        self.entry_engineer.insert(0, row[3])
        self.entry_installation_location.insert(0, row[4])
        self.entry_model.insert(0, row[5])
        self.entry_serial_number.insert(0, row[6])
        self.entry_application_content.insert(0, row[7])
        self.entry_number_of_copies.insert(0, row[8])
        self.entry_list_of_works.insert(0, row[9])
        self.entry_to_replace_name.insert(0, row[10])
        self.entry_tochangepn.insert(0, row[11])
        self.entry_quantity.insert(0, row[12])
        self.entry_parts_installation.insert(0, row[13])
        self.entry_note.insert(0, row[14])





#Поиск данных
class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)         #width - длина поля

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search =ttk.Button(self, text='Поиск')
        btn_search.place(x=75, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')



#База данных
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('Отчеты 12_07_21.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS base_engineer (id integer primary key, engineer text, date text, organization text,
             installation_location text, model text, serial_number text, application_content text, number_of_copies real, list_of_works text,
             to_replace_name text, tochangepn text, quantity real, parts_installation text, note text)''')
        self.conn.commit()

    def insert_data(self, engineer, date, organization, installation_location, model, serial_number, application_content, number_of_copies,
                    list_of_works, to_replace_name, tochangepn, quantity, parts_installation,note):
        self.c.execute('''INSERT INTO base_engineer(engineer, date, organization, installation_location, model, serial_number, application_content,
        number_of_copies, list_of_works, to_replace_name, tochangepn, quantity, parts_installation, note) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',   #SQL запрос
                       (engineer, date, organization, installation_location, model, serial_number, application_content, number_of_copies,
                    list_of_works, to_replace_name, tochangepn, quantity, parts_installation, note))
        self.conn.commit()




if __name__ == "__main__":           #Параметры окна
        root = tk.Tk()
        db = DB()
        app = Main(root)
        app.pack()
        root.title("bd_leson")
        root.geometry("1000x430+300+200")     #Размер окна
        root.resizable(False, False)        #Неизменять размер окна
        root.mainloop()