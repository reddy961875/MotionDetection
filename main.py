import tkinter as tk
import tkinter.font as font
from FindMotion import find_motion
#import tensorflow as tf



window =  tk.Tk()
window.title = "find stolen"
window.geometry("450x200")


#label
label = tk.Label(window, text="Welcome")
label.grid(row=0, column=1)
label['font'] = font.Font(size=35, weight='bold',family='Helvetica')

#button font
btn_font = font.Font(size=15, weight='bold',family='Helvetica')

button1 = tk.Button(window, text="spot diff",fg="green", height=3, width=10, command=find_motion)
button1['font'] = btn_font
button1.grid(row=1, pady=(25,10),padx=(10,0), column = 0)


#exit button
button2 = tk.Button(window, text="exit",fg="red", height=3, width=10, command=window.quit)
button2['font'] = btn_font
button2.grid(row=1, pady=(25,10), column=2)




window.mainloop()

