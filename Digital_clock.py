import time
from tkinter import *

mw = Tk()
mw.title('DIGITAL CLOCK')
#mw.iconbitmap(r'C:\Users\mgowt\OneDrive\Desktop\INTERNPE\DC.ico')


def curr_time():
    live = time.strftime('%H:%M:%S')
    display.config(text=live)
    display.after(1000, curr_time)


internpe = Label(mw, text="INTERNPE", font=('Arail', 26))
project = Label(mw, text='TASK_2 : DIGITAL CLOCK', font=('Arial', 24))
display = Label(mw, text='TIME', fg='red', bg='black', font=('Arial', 32))
internpe.grid(row=0, column=0, columnspan=2, pady=10)
project.grid(row=1, columnspan=2, column=0, padx=10, pady=10)
display.grid(row=2, column=0, columnspan=2, pady=30)
curr_time()

mw.mainloop()
