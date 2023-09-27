from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("800x800")
label=Label(top, text="Bangla", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(top, width= 40)
entry.focus_set()
entry.pack()

label1=Label(top, text="English", font=("Courier 22 bold"))
label1.pack()

#Create an Entry widget to accept User Input
entry1= Entry(top, width= 40)
entry1.focus_set()
entry1.pack()


# label=Label(top, text="English", font=("Courier 22 bold"))
# label.pack()

# #Create an Entry widget to accept User Input
# entry= Entry(top, width= 40)
# entry.focus_set()
# entry.pack()
def get_value():
    global b, e
    b=int(entry.get())
    e=int(entry1.get())
    b_g = ''
    if(b>0 and b < 33 ):
        b_g = 'F'
    elif(b>32 and b < 40):
        b_g = 'D'
    elif(b>39 and b < 50 ):
        b_g = 'C'
    elif(b>49 and b < 60):
        b_g = 'B'

    elif(b>59 and b < 70 ):
        b_g = 'A-'

    elif(b>69 and b < 80):
        b_g = 'A'

    else:
        b_g = 'A+'
    Label(top, text="Bangla Grade= "+b_g, font= ('Century 15 bold')).pack(pady=20)
    Label(top, text="English Score= "+str(e), font= ('Century 15 bold')).pack(pady=40)
B = Button(top, text ="Calculate Grade" , command=get_value)
B.place(x=400,y=200)
top.mainloop()