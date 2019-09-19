#Name:Pratik Singh
#Student id: 1001670417

from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("450x450")
root.title("Login Portal")
lbl = Label(root, text="Please Login", justify='center')
lbl.pack()
label1 = Label(root, text="Username:", width=20)
label1.place(x=3, y=130)
username = StringVar()
password = StringVar()
entry1 = Entry(root, textvariable=username)
entry1.place(x=135, y=130)
label2 = Label(root, text="Password:", width=20)
label2.place(x=5, y=180)
entry2 = Entry(root, textvariable=password, show="*")
entry2.place(x=135, y=180)


def compute_area():
    top = Toplevel()
    top.title("Calculate Hypotenuse")
    top.geometry("550x170")
    labela = Label(top, text='Side A')
    labela.place(x=2, y=2)
    sideA = StringVar()
    sideB = StringVar()
    sideC = StringVar()

    entrya = Entry(top, textvariable=sideA, width=20)
    entrya.place(x=60, y=2)
    labelb = Label(top, text='Side B')
    labelb.place(x=2, y=30)
    entryb = Entry(top, textvariable=sideB, width=20)
    entryb.place(x=60, y=30)
    labelc = Label(top, text='Side C')
    labelc.place(x=2, y=60)
    entryc = Entry(top, textvariable=sideC, width=20)
    entryc.place(x=60, y=60)
    entryc.configure(state="disabled")
    Button(top, text="Calculate", width=7, command=lambda: computearea(sideA.get(), sideB.get())).place(x=100, y=100)
    Button(top, text="Exit", width=7, command=root.destroy).place(x=180, y=100)

    def computearea(s1, s2):
        s3 = (int(s1) ** 2) + (int(s2) ** 2)
        s3 = s3 ** 0.5
        sideC.set('{:.3f}'.format(s3))




def open_window(user, password):
    pass_text = open('users.txt', 'r')
    line = pass_text.readline()
    while (line != ''):
        lin = line.strip()
        ar = lin.split("|")
        if (ar[0] == user and ar[1] == password):
            compute_area()
            break
        else:
            line = pass_text.readline()
    else:
        messagebox.showwarning("Login", " Please try again")
        pass

    pass_text.close()


Button(root, text="Login", width=7, command=lambda: open_window(username.get(), password.get())).place(x=100, y=220)
Button(root, text="Exit", width=7, command=root.destroy).place(x=160, y=220)
root.mainloop()




