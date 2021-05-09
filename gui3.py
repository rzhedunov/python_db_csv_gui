#!/usr/bin/env python3.8
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *


class MyTable (ttk.Treeview):
    COLUMNS = [        
        ("Номер", 100, tk.CENTER),
        ("Имя", 100, tk.CENTER),
    ]
    
    def __init__ (self, * args, ** kw):
        super () .__init__ (* args, ** kw)
        self.config (
            show = "headings",
            # NOTE: colums = [0, 1, 2, 3]
            columns = list (range (len (self.COLUMNS))),
        )
        for idx, (text, width, anchor) in enumerate (self.COLUMNS):
            self.heading (idx, text = text)
            self.column (idx, width = width, anchor = anchor)

def close_window():
    import sys
    sys.exit()

def pbLoadClick(m):
    #messagebox.showinfo("Сообщение", "Пытаемся прочитать файл")    
    file1 = open("data.csv", "r")
    while True:
        line = file1.readline()
        if not line:
            break
        c = line.split(';')
        #~ print(c[0],c[1])
        m.insert ("", tk.END, values = [c[0], c[1]])
        
def pbAddClick(m, tb1,tb2):
    m.insert ("", tk.END, values = [tb1.get(), tb2.get()])
    # ~ messagebox.showinfo("Сообщение", "Якобы добавили строчку")
    # ~ print("Якобы добавили строчку")


    
def main():
    root = tk.Tk()
    frame = ttk.Frame(root)    
    frame.pack(fill = tk.BOTH, expand = tk.YES)
    
    frame2 = ttk.Frame(root)    
    frame2.pack(fill = tk.BOTH, expand = tk.YES)
    
    treeA = MyTable(frame)
    treeA.pack()
    knopkaLoad = Button(frame, text = "Загрузить", width = 20, command=lambda: pbLoadClick(treeA))
    knopkaLoad.pack()
    knopkaDelete = Button(frame, text = "Удалить", width = 20)
    knopkaSort1 = Button(frame, text = "Сортировать1", width = 20)
    knopkaSort2 = Button(frame, text = "Сортировать2", width = 20)
    knopkaSelect = Button(frame, text = "Выбрать по условию", width = 20)
    knopkaSave = Button(frame, text = "Сохранить", width = 20)
    knopkaExit = Button(frame, text = "Выход", width = 20, command=close_window)
    
    col1 = Entry(frame, justify='center')    
    col1.insert(END, '999')
    col1.pack()
    col2 = Entry(frame, justify='center')
    col2.insert(END, 'new value')
    col2.pack()
    
    knopkaAdd = Button(frame, text = "Добавить", width = 20, command=lambda: pbAddClick(treeA, col1, col2))    
    knopkaAdd.pack()    
    
    knopkaDelete.pack()
    knopkaSort1.pack()
    knopkaSort2.pack()
    knopkaSelect.pack()
    knopkaSave.pack()
    knopkaExit.pack()
    
    root.title('Простой GUI')
    w = 800
    h = 650
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    root.mainloop ()
    
if __name__ =='__main__':
    main()
