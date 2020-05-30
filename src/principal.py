import tkinter
import queue as qu
from widget import Widget
from widget import Message
from worker import Worker

window = tkinter.Tk()
# to rename the title of the window
window.title("GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "window downloader").pack()

cola = qu.Queue()

frame = Widget(window,cola).pack()



Worker(cola).start()
window.mainloop()

