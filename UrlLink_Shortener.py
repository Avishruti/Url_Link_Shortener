import pyshorteners
from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("Url Shortener")
window.configure(bg="lightblue")

#Button function
def url_short():
    url = entry_box1.get()
    short = pyshorteners.Shortener().tinyurl.short(url)

    entry_box2.insert(END, short)

#Label for entering user url
Label(window,text="Enter url Link", font="impact 20 ", bg="black", fg="White").pack(fill="x")

#Entry box
entry_box1 = Entry(window, font="3", bd=3, width=33)
entry_box1.pack(pady=30)

#Button
Button(window,text="Click Here", font="impack 10 bold", bg="black", fg="white", command=url_short).pack()

#Entry
entry_box2 = Entry(window,font="10", bg="white", fg="black", width=30)
entry_box2.pack(pady=30)

mainloop()