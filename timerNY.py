# таймер до нового года
import datetime
from datetime import timedelta
from tkinter import *

window = Tk()
window.title('Таймер')

def new_year(window):
    
    new_y = datetime.datetime(2023, 1, 1,0,0)
    my_time = datetime.datetime.today()    
    timer = new_y - my_time
    timer -= timedelta(microseconds=timer.microseconds)
    a = f'До нового года осталось: {timer}'
    lbl = Label(window, text=a)         # вывод времени дни, часы, минуты и секунды
    lbl.grid(row= 0, column=1)
    window.after(1000, new_year, window)
    seconds = timer.seconds + timer.days * 86400
    seconds_2 = f'До нового года осталось: {seconds} сек'
    lbl_2 = Label(window, text=seconds_2) # вывод времени секундами
    lbl_2.grid(row=2, column=1)

new_year(window)
window.geometry('240x260')
window.mainloop()  