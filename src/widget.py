import tkinter as tk
import queue as qu
import threading as th
from tkinter import scrolledtext as st
from tkinter.ttk import Progressbar 

class Widget(tk.Frame):
        def __init__(self, parent,cola : qu.Queue):
            tk.Frame.__init__(self, parent, bg="green")
            self.parent = parent
            self.widgets()
            self.cola =cola
            self.parent.after(1000,self.worker)
            self.parent.configure(background='black')
            
        def widgets(self):
            self.text = st.ScrolledText(self, width=50, height=2)
            self.text.insert(tk.INSERT, "Hello World\n")
            self.text.insert(tk.END, "nueva sentencia\n")
            self.text.insert(tk.END, "This is the first frame")
            self.text.grid(row=10, column=1)
            self.progress_bar = Progressbar(self,orient=tk.HORIZONTAL,length=500)
            self.progress_bar.grid(row=11, column=1)
            

            # self.scroll = tk.Scrollbar(self, bg='gray70')
            # self.scroll.grid(row=0,column=2)            

        def polling(self,cola:qu.Queue):
            self.text.insert(tk.END,cola.get()+"entrada polling \n")

        def worker(self):
            self.text.insert(tk.END,"nueva al final")
            tread = th.Thread(target=self.polling,args=(self.cola,))
            tread.start()
            

        


