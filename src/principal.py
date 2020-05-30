import widget
import tkinter
import queue as qu


window = tkinter.Tk()
# to rename the title of the window
window.title("GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "window downloader").pack()

cola = qu.Queue()
cola.put("menaje en la cola")

frame = widget.Widget(window,cola).pack()


window.mainloop()

