from tkinter import*

class hotelmanagementsysyem :
    def __init__(self,root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geomatry("1200x600")

if __name__ == "__main__":
    root = Tk()
    h1 = hotelmanagementsysyem(root)
    root.mainloop()