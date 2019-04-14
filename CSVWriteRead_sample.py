import tkinter as tk
import csv

def csv_writer():
    csv_file = open('./python.csv', 'w', newline='')
    writer = csv.writer(csv_file)
    
    row = ('python', '-', 'izm', '1')
    writer.writerow(row)
    
    rows = []
    rows.append(('python', '-', 'izm', '2'))
    rows.append(('python', '-', 'izm', '3'))
    rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
    writer.writerows(rows)
    
    csv_file.close()

def csv_reader():
    csv_file = open('./python.csv', 'r', newline='')
    reader = csv.reader(csv_file)
    
    for row in reader:
        print('-------------------')
        data = []    
        for cell in row:
            data.append(cell)
            print(cell)
        print(data)
 
    csv_file.close()

root = tk.Tk()

btn1 = tk.Button(text="書き出し", command=csv_writer)
btn1.pack()

btn2 = tk.Button(text="読み込み", command=csv_reader)
btn2.pack()

root.mainloop()