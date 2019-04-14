import tkinter as tk

def BtnEvent():
    subWindow = tk.Toplevel()
    subWindow.title("test")
    subBtn = tk.Button(subWindow, text="キャンセル", command=subWindow.destroy)
    subBtn.pack()


root = tk.Tk()
btn1 = tk.Button(root, text="新しいウィンドウ", command=BtnEvent)
btn1.pack()
btn2 = tk.Button(root, text="閉じる", command=root.destroy)
btn2.pack()
root.mainloop()