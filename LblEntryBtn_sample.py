import tkinter as tk

def text_delete(event):
    ebTest.delete(0, tk.END)

root = tk.Tk()
root.title(u"Software Title")
root.geometry("400x300")
lblTest = tk.Label(text=u'test')
lblTest.place(x=0,y=0)
ebTest = tk.Entry()
ebTest.place(x=100,y=0)
btnTest = tk.Button(text=u'test')
btnTest.place(x=200,y=0)
btnTest.bind('<Button-1>', text_delete)
root.mainloop()