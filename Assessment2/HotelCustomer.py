from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class customer_details:
    def __init__(self,root) :
        self.root=root
        self.root.title("HotelManagementSystem")
        self.root.geometry("1130x480+150+150")

        # ==============================variables=================================
        self.var_name = StringVar()        
        self.var_address = StringVar()
        self.var_number = StringVar()
        self.var_no_of_days = StringVar()

        #  =================================Title==================================

        lbl_title = Label(self.root,relief="groove" , text="YOU CLIKED ON      :      CHECK INN", font=("Arial 25 bold"),bg="white")
        lbl_title.place(x=5,y=5, width=1115, height=80)

        # --------------------------------row1-----------------------------------
        frame = Frame(relief=GROOVE, bg="white", bd=2)
        label_name = Label(self.root, text="ENTER YOUR NAME                    :", font=("Arial 15 bold"), bg="white")
        label_name.place(x=50, y=100, height= 40, width=360)
        entry_name = ttk.Entry(self.root,textvariable=self.var_name, font=("Arial 18"))
        entry_name.place(x=430, y=98, height=35, width=600)
        button = Button(self.root, text="OK", font=("Arial 15"), bg="white", cursor="hand2")
        button.place(x=1050, y=98, width=50, height=35)
        frame.place(x=5,y=89,height=280, width=1115)

        # --------------------------------row2-----------------------------------
        label_name = Label(self.root, text="ENTER YOUR ADDRESS             :", font=("Arial 15 bold"), bg="white")
        label_name.place(x=50, y=140, height= 40, width=360)
        entry_name = ttk.Entry(self.root,textvariable=self.var_address, font=("Arial 18"))
        entry_name.place(x=430, y=138, height=35, width=600)
        button = Button(self.root, text="OK", font=("Arial 15"), bg="white", cursor="hand2")
        button.place(x=1050, y=138, width=50, height=35)

        # --------------------------------row3-----------------------------------
        label_name = Label(self.root, text="ENTER YOUR NUMBER               :", font=("Arial 15 bold"), bg="white")
        label_name.place(x=50, y=180, height= 40, width=360)
        entry_name = ttk.Entry(self.root,textvariable=self.var_number, font=("Arial 18"))
        entry_name.place(x=430, y=178, height=35, width=600)
        button = Button(self.root, text="OK", font=("Arial 15"), bg="white", cursor="hand2")
        button.place(x=1050, y=178, width=50, height=35)

        # --------------------------------row4-----------------------------------
        label_name = Label(self.root, text="NUMBER OF DAYS                      :", font=("Arial 15 bold"), bg="white")
        label_name.place(x=50, y=221, height= 40, width=360)
        entry_name = ttk.Entry(self.root,textvariable=self.var_no_of_days, font=("Arial 18"))
        entry_name.place(x=430, y=221, height=35, width=600)
        button = Button(self.root, text="OK", font=("Arial 15"), bg="white", cursor="hand2")
        button.place(x=1050, y=221, width=50, height=35)

        # --------------------------------row5-----------------------------------
        label_name = Label(self.root, text="CHOOSE YOUR ROOM", font=("Arial 12 bold"), bg="white")
        label_name.place(x=220, y=260, height= 30, width=360)

        # --------------------------------row6-----------------------------------
        label_checkbutton1 = Checkbutton(self.root, text="DELUXE", font=("Arial 12 bold"), bg="white")
        label_checkbutton1.place(x=150, y=280, height=15, width=100)

        label_checkbutton2 = Checkbutton(self.root, text="GENERAL", font=("Arial 12 bold"), bg="white")
        label_checkbutton2.place(x=489, y=280, height=15, width=120)

        # --------------------------------row7-----------------------------------
        label_checkbutton3 = Checkbutton(self.root, text="FULL DELUXE", font=("Arial 12 bold"), bg="white")
        label_checkbutton3.place(x=123, y=300, height=15, width=200)

        label_checkbutton4 = Checkbutton(self.root, text="JOINT", font=("Arial 12 bold"), bg="white")
        label_checkbutton4.place(x=483, y=300, height=15, width=100)

        # --------------------------------row8-----------------------------------
        label_name = Label(self.root, text="CHOOSE PAYMENT METHOD", font=("Arial 12 bold"), bg="white")
        label_name.place(x=200, y=325, height= 15, width=360)

        #--------------------------------row9----------------------------------
        label_checkbutton5 = Checkbutton(self.root, text="By cash", font=("Arial 12 bold"), bg="white")
        label_checkbutton5.place(x=147, y=340, height=22, width=100)

        label_checkbutton6 = Checkbutton(self.root, text="By credit/debit card", font=("Arial 12 bold"), bg="white")
        label_checkbutton6.place(x=443, y=340, height=22, width=280)

        button = Button(self.root, text="SUBMIT", font=("Arial 15 bold"), bg="white", cursor="hand2")
        button.place(x=720, y=280, width=170, height=80)

        self.fetch_data()

        # =================================Title==================================
        lbl_title = Label(self.root, text="name has been inputed\naddress has been inputed\ninvalid input please input a valid mobile number\nmobile number has been inputed", font=("Arial 8"),bg="white",bd=2, relief=GROOVE)
        lbl_title.place(x=5,y=372, width=1115, height=75)

        # =================================buttons===================================
        button_add = Button(self.root,text="Add",command=self.add_customer_details,font=("Arial 10 bold"),relief=GROOVE,bd=2,bg="white",width=33,height=0)
        button_add.place(x=5,y=450)

        button_update = Button(self.root,text="Update",font=("Arial 10 bold"),relief=GROOVE,bd=2,bg="white",width=33,height=0)
        button_update.place(x=285,y=450)

        button_delete = Button(self.root,text="Delete",font=("Arial 10 bold"),relief=GROOVE,bd=2,bg="white",width=33,height=0)
        button_delete.place(x=565,y=450)

        button_reset = Button(self.root,text="Reset",font=("Arial 10 bold"),relief=GROOVE,bd=2,bg="white",width=33,height=0)
        button_reset.place(x=846,y=450)

    def add_customer_details(self):
        if self.var_number.get()=="" or self.var_address.get()=="":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        else:
            try :
                d_base = pymysql.connect(host="localhost",user="root",passwd="",database="customer")
                my_cursor = d_base.cursor()
                my_cursor.execute("insert into customer_details values(%s,%s,%s,%s)",
                (
                self.var_name.get(),
                self.var_address.get(),
                self.var_number.get(),
                self.var_no_of_days.get()
                ))
                d_base.commit()
                self.fetch_data()
                d_base.close()
                messagebox.showinfo("Entry Added Successfully.","Customer has been added.",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}.",parent=self.root)


                
if __name__=="__main__":
    root=Tk()
    hc1 = customer_details(root)
    root.mainloop()