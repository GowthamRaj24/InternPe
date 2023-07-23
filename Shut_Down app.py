import tkinter as tk
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_after_time():
    os.system("shutdown /r /t 20")

def log_out():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /r /t 1")

mw = tk.Tk()  
mw.title("ShutDown App")
mw.geometry("500x500")
mw.config(bg="Blue")

# Create buttons with their respective actions
restart_button = tk.Button(mw, text="Restart", font=("Times New Roman", 20, "bold"),
                           relief=tk.RAISED, cursor="plus", command=restart)
restart_button.place(x=150, y=60, height=50, width=200)

restart_time_button = tk.Button(mw, text="Restart Time", font=("Times New Roman", 20, "bold"),
                                relief=tk.RAISED, cursor="plus", command=restart_after_time)
restart_time_button.place(x=150, y=170, height=50, width=200)

log_out_button = tk.Button(mw, text="Log-Out", font=("Times New Roman", 20, "bold"),
                           relief=tk.RAISED, cursor="plus", command=log_out)
log_out_button.place(x=150, y=270, height=50, width=200)

shutdown_button = tk.Button(mw, text="Shutdown", font=("Times New Roman", 20, "bold"),
                            relief=tk.RAISED, cursor="plus", command=shutdown)
shutdown_button.place(x=150, y=370, height=50, width=200)

# Start the Tkinter main loop
mw.mainloop()
