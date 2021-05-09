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

def pbDeleteClick(m):
    if m.selection():
        for selection in m.selection():
                item = m.item(selection)
                pole1, pole2 = item["values"][0:2]
                selected_item = m.selection()[0] ## get selected item
                m.delete(selected_item)
                children = m.get_children() 
                messagebox.showinfo("Сообщение", "Строка с "+str(pole1)+" "+str(pole2) +" удалена! Осталось "+str(len(children))+" записей")
                if len(children)>0:
                    m.selection_set(children[0])
    else:
        messagebox.showinfo("Сообщение", "Строка не выделена!")

def pbSortByColNClick(m,n):
    newlist = []
    for child in m.get_children():
        # ~ print(m.item(child)["values"])
        newlist.append([m.item(child)["values"][0], m.item(child)["values"][1].replace('\n','')])
    # ~ newlist.append([999,999])
    newlist.sort(key=lambda i: i[n])
    
    for i in m.get_children():
        m.delete(i)
    
    for z in newlist:
        m.insert ("", tk.END, values = [z[0], z[1]])
    
    # ~ messagebox.showinfo("Сообщение", "Якобы отсортировали по 1-му столбцу")
        
        
        
        
        
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
    knopkaDelete = Button(frame, text = "Удалить", width = 20, command=lambda: pbDeleteClick(treeA))
    knopkaSort1 = Button(frame, text = "Сортировать1", width = 20, command=lambda: pbSortByColNClick(treeA,0))
    knopkaSort2 = Button(frame, text = "Сортировать2", width = 20, command=lambda: pbSortByColNClick(treeA,1))
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
