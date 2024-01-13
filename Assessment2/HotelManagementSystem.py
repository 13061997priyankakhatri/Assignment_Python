from tkinter import *
from HotelCustomer import customer_details 

class hotelmanagementsystem :

    def __init__(self,root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1280x600+0+0")

        # =================================Frame==================================
        frame = Frame(relief=GROOVE , bd=2, bg="#d3d3d3")
        
        # =================================Title==================================
        lbl_title = Label(self.root, text="WELCOME", font=("Arial 25 bold"), bg="#d3d3d3", fg="#010203")
        lbl_title.place(x=22,y=50, width=1180, height=25)

        # =================================Menu==================================
        button1 = Button(self.root, text="1.CHECK INN", command=self.hotelcustomer_details, fg="#010203", bg="#d3d3d3", font=("Arial 10 bold"), relief=RAISED, bd=2, cursor="hand2")
        button1.place(x=310, y=200, width=350, height=80, anchor=SW)

        button2 = Button(self.root, text="2.SHOW GHEST LIST", fg="#010203", bg="#d3d3d3", font=("Arial 10 bold"), relief=RAISED, bd=2, cursor="hand2")
        button2.place(x=310, y=290, width=350, height=80, anchor=SW)

        button3 = Button(self.root, text="3.CHECK OUT", fg="#010203", bg="#d3d3d3", font=("Arial 10 bold"), relief=RAISED, bd=2, cursor="hand2")
        button3.place(x=310, y=380, width=350, height=80, anchor=SW)

        button4 = Button(self.root, text="4.GET INFO OF ANY GHEST", fg="#010203", bg="#d3d3d3", font=("Arial 10 bold"), relief=RAISED, bd=2, cursor="hand2")
        button4.place(x=310, y=470, width=350, height=80, anchor=SW)

        button5 = Button(self.root, text="5.EXIT", fg="#010203", bg="#d3d3d3", font=("Arial 10 bold"), relief=RAISED, bd=2, cursor="hand2")
        button5.place(x=310, y=560, width=350, height=80, anchor=SW)

        # ==========================Right side text================================
        text_lbl = Label(self.root, text="HOTEL MANAGEMENT", bg="#d3d3d3", font=("BahnschriftCondensed 35 bold"))
        text_lbl.place(x=660,y=130, width=560, height=50, anchor=NW)

        text_lbl = Label(self.root, text="PYTHON TKINTER", bg="#d3d3d3", font=("Bahnschrift 45 bold"))
        text_lbl.place(x=660,y=230, width=550, height=50, anchor=NW)

        text_lbl = Label(self.root, text="GUI", bg="#d3d3d3", font=("Impact 100"))
        text_lbl.place(x=670,y=330, width=450, height=150, anchor=NW)

        frame.place(x=20,y=20, width=1235, height=605)

    # def register_details(self):
        
    #     self.new_window = Toplevel(self.root)
    #     self.app = register(self.new_window)
        
    def hotelcustomer_details(self):
        
        self.new_window = Toplevel(self.root)
        self.app = customer_details(self.new_window)

if __name__ == "__main__":

    root = Tk()
    h1 = hotelmanagementsystem(root)
    root.mainloop()