# create an application to find  average

from tkinter import *
# package great for predefined windows to share information, errors, ask  question,etc
from tkinter import messagebox


class averageFind:
    def __init__(self):
        self.window = Tk()
        self.window.title('Average converter')
        self.window.geometry("550x250")

    #===================================== FRAMES ==============================================

        self.top_frame1 = Frame(self.window)

        self.top_frame2 = Frame(self.window)

        self.top_frame3 = Frame(self.window)

        self.bottom_frame = Frame(self.window)

        self.result_frame = Frame(self.window)

    # ==================================== Widgets ================================================

        self.prompt_label1 = Label(self.top_frame1, text="Enter Number 1: ",
                                   font=("carrier new", 10, 'bold'), padx=10)
        self.prompt_label2 = Label(self.top_frame2, text="Enter Number 2: ",
                                   font=("carrier new", 10, 'bold'), padx=10)
        self.prompt_label3 = Label(self.top_frame3, text="Enter Number 3: ",
                                   font=("carrier new", 10, 'bold'), padx=10)

        self.num1_entry = Entry(self.top_frame1)
        self.num2_entry = Entry(self.top_frame2)
        self.num3_entry = Entry(self.top_frame3)

    # for ,command you use a function without argument.

        self.result = StringVar(value="Result : N/A")
        self.average_btn = Button(self.bottom_frame, text="Average", padx=15, background="yellow",
                                  command=self.averagenum)
        self.average_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.exit_btn = Button(self.bottom_frame, text="Quit", padx=10, background="orange", command=self.quite_app)
        self.exit_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.result_label = Label(self.result_frame, textvariable=self.result,
                                  font=("carrier new", 10, 'bold'), fg="brown")
    #=====================================Pack Widgets ===========================================
        self.prompt_label1.pack(pady=10, side="left")
        self.prompt_label2.pack(pady=10, side="left")
        self.prompt_label3.pack(pady=10, side="left")
        self.num1_entry.pack(pady=14, padx=10)
        self.num2_entry.pack(pady=14, padx=10)
        self.num3_entry.pack(pady=14, padx=10)
        self.average_btn.pack(side="left", padx=5)
        self.exit_btn.pack()
        self.result_label.pack()

    # ===================================pack Frames===============================================
        self.top_frame1.pack()
        self.top_frame2.pack()
        self.top_frame3.pack()
        self.bottom_frame.pack(pady=10, side='bottom', padx=20)
        self.result_frame.pack(padx=10)

        mainloop()

# create function for find average of 3 number.

    def averagenum(self):
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        num3 = self.num3_entry.get()

        if num1.isnumeric() and num2.isnumeric() and num3.isnumeric():
            average =(int(num1) + int(num2) + int(num3))/3
            self.result.set(f'Result :{average :.2f}')
            print(average)
        elif num1 == "" or num2 == "" or num3 == "":
            messagebox.showinfo("Information", "empty :please input any number ")

        else:
            messagebox.showerror("ERROR", "BAD TYPE OF INPUT!\nInput has to be numeric\nEX: 1, 2, 3.4 ...")
            self.num1_entry.delete(0, 'end')
            self.num2_entry.delete(0, 'end')
            self.num3_entry.delete(0, 'end')
            self.result.set("Result : N/A")
# create function for quit application.

    def quite_app(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to quit the application?"):
            self.window.destroy()


w1 = averageFind()
