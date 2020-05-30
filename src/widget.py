import tkinter as tk
import queue as qu
import threading as th
from tkinter import scrolledtext as st
from tkinter.ttk import Progressbar 
import time



class Message:
    def __init__(self,message:str, progress:int,lastmessage = False):
        self.messege = message
        self.progress = int
        self.lastmessage = lastmessage

class Widget(tk.Frame):
        def __init__(self, parent,cola : qu.Queue):
            tk.Frame.__init__(self, parent, bg="green")
            self.parent = parent
            self.widgets()
            self.cola =cola
            self.parent.after(100,self.worker)
            self.parent.configure(background='black')
            self.parent.protocol("WM_DELETE_WINDOW", self.closewidget)
            
        def widgets(self):
            self.text = st.ScrolledText(self, width=50, height=10)
            self.text.insert(tk.INSERT, "Hello World\n")
            self.text.insert(tk.END, "nueva sentencia\n")
            self.text.insert(tk.END, "This is the first frame")
            self.text.grid(row=10, column=1)
            self.progress_bar = Progressbar(self,orient=tk.HORIZONTAL,length=500)
            self.progress_bar.grid(row=11, column=1)
            
            # self.scroll = tk.Scrollbar(self, bg='gray70')
            # self.scroll.grid(row=0,column=2)            

        def worker(self):
            self.text.insert(tk.END,"nueva al final")
            #Daemon make destroy the threads when main trhead ends
            tread = th.Thread(target=self.polling,args=(self.cola,),daemon=True)
            tread.start()
            
        def polling(self,cola:qu.Queue):
            # self.text.insert(tk.END,cola.get()+"entrada polling \n")
            last_message= False
            while (not last_message):
               message: Message =  cola.get(True)
               self.text.insert(tk.END,message.messege)
               last_message = message.lastmessage
               cola.task_done()
            self.closewidget()
        
        def closewidget(self):
            print("en destoy")
            self.parent.destroy()