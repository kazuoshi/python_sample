import tkinter as tk

def btn_event():
    subWindow = tk.Toplevel()
    subWindow.title("test")
    subBtn = tk.Button(subWindow, text="キャンセル", command=subWindow.destroy)
    subBtn.pack()


root = tk.Tk()
btn1 = tk.Button(root, text="新しいウィンドウ", command=btn_event)
btn1.pack()
btn2 = tk.Button(root, text="閉じる", command=root.destroy)
btn2.pack()
root.mainloop()