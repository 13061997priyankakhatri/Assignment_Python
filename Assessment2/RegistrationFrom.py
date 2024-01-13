from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class register :
    
    def __init__(self,root) :

        self.root = root
        self.root.title("Regiatration Form")
        self.root.geometry("550x450+710+180")

        # =================================Frame==================================
        frame = Frame(self.root, bg="lightgray")

        # =================================Title==================================
        lbl_title = Label(self.root, text="Please enter details below", font=("Arial 12 bold"), bg="orange", fg="beige")
        lbl_title.place(x=0,y=0, width=1280, height=25)

        # ==============================Label and entry===========================

        # --------------------------------row1-----------------------------------
        label_name = Label(self.root, text="Name* :", font=("Arial 12"), bg="lightgray")
        label_name.place(x=50, y=50, height= 20, width=100)
        entry_name = ttk.Entry(self.root, font=("Arial 12"))
        entry_name.place(x=150, y=50, height=30, width=150)

        # --------------------------------row2-----------------------------------
        label_contact = Label(self.root, text="Contact* :", font=("Arial 12"), bg="lightgray")
        label_contact.place(x=55, y=100, height=20, width=100)
        entry_contact = ttk.Entry(self.root, font=("Arial 12"))
        entry_contact.place(x=149, y=100, height=30, width=150)

        # --------------------------------row3-----------------------------------
        label_email =Label(self.root, text="Email* :", font=("Arial 12"), bg="lightgray")
        label_email.place(x=50, y=150, height=20, width=100)
        entry_email = ttk.Entry(self.root,  font=("Arial 12"))
        entry_email.place(x=150, y=150, height=30, width=150)

        # --------------------------------row4-----------------------------------
        gender = IntVar()

        lbl_gender = Label(self.root,text="Gender* : ", font=("Arial 12"), bg="lightgray")
        lbl_gender.place(x=55,y=200, height=20, width=100)

        radio = Radiobutton(self.root, text ="Male", font=("Arial 12"),bg="lightgray",variable=gender, value=1)
        radio.place(x=140, y=205, height=20, width=80, anchor="w")

        radio = Radiobutton(self.root, text ="Female", font=("Arial 12"),bg="lightgray",variable=gender, value=2)
        radio.place(x=220, y=205, height=20, width=80, anchor="w")


        # --------------------------------row5-----------------------------------
        label_city = Label(frame, text ="City* :", font=("Arial 12"), bg="lightgray", fg="black")
        label_city.place(x=70, y=215)

        self.combobox = ttk.Combobox(frame,font=("Arial 12"),state ="readonly")
        self.combobox["values"] = ("Select","Palanpur","Bhuj","Ahemadabad","Surat")
        self.combobox.place(x=150, y=215, width=250, height=30)
        self.combobox.current(0)

        # --------------------------------row6-----------------------------------
        label_state = Label(frame, text ="State* :", font=("Arial 12"), bg="lightgray", fg="black")
        label_state.place(x=70, y=260)


        self.combobox = ttk.Combobox(frame,font=("Arial 12"),state ="readonly")
        self.combobox["values"] = ("Select","Gujarat","Maharastra","Madyapradesh","Utterpradesh")
        self.combobox.place(x=150, y=260, width=250, height=30)
        self.combobox.current(0)

        # ==================================Label---row7---=================================
        lbl_title = Label(self.root, text="fill the empty field!!!", font=("Arial 12"), bg="lightgray",bd=2)
        lbl_title.place(x=120,y=330, width=180, height=25)

        # =================================button---row8----=================================
        button = Button(self.root, text="Register", bg="orange", font=("Arial 10"), cursor="hand2")
        button.place(x=150, y=370, width=100, height=25)

        frame.place(x=0, y=25, height=622, width=1280)

if __name__=="__main__":

    root = Tk()
    c1 = register(root)
    root.mainloop()