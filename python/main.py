from tkinter import *

def Reset():
    entry_cig.delete(0, END)
    entry_alcohol.delete(0, END)
    entry_gambling.delete(0, END)
    entry_dining.delete(0, END)
    entry_purchase.delete(0, END)
    entry_unnecesary.delete(0, END)
    entry_visits.delete(0, END)
    entry_total.delete(0, END)
    entry_total2.delete(0, END)
    entry_total3.delete(0, END)

def Total():
    try:
        a1 = int(cig.get())
    except:
        a1 = 0
    try:
        a2 = int(alcohol.get())
    except:
        a2 = 0
    try:
        a3 = int(gambling.get())
    except:
        a3 = 0
    try:
        a4 = int(dining.get())
    except:
        a4 = 0
    try:
        a5 = int(purchase.get())
    except:
        a5 = 0
    try:
        a6 = int(unnecesary.get())
    except:
        a6 = 0
    try:
        a7 = int(visits.get())
    except:
        a7 = 0

    totalcost = a1 + a2 + a3 + a4 + a5 + a6 + a7

    entry_total.config(state="normal")
    entry_total.delete(0, END)  
    entry_total.insert(0, str(totalcost))  
    entry_total.config(state="readonly")  

    entry_total.place(x=20, y=60)

    for widget in f11.winfo_children():
        widget.destroy()

    if totalcost >= 1000:
        message = Label(f11, text="With this budget, you have the opportunity\n to Invest in educational materials or courses\n for personal development.",font=('Times New Roman', 15), bg="#005b96", fg="black")
        message.place(x=40, y=25)
    elif totalcost >= 500:
        message1 = Label(f11, text="This amount allows you to \nPay a portion of utility bills\n like electricity, water, etc.",font=('Times New Roman', 15), bg="#005b96", fg="black")
        message1.place(x=70, y=25)
    elif totalcost >= 100:
        message2 = Label(f11, text="You can make the most of this money by \npurchasing essential groceries or household items.",font=('Times New Roman', 15), bg="#005b96", fg="black")
        message2.place(x=10, y=26)
    else:
        mes = Label(f11, text="No extravagant lifestyle, just a wise one.\n Your wallet is smiling in approval",font=('Times New Roman', 15), bg="#005b96", fg="black")
        mes.place(x=50, y=28)

def Total1():
    try:
        a1 = int(cig.get())
    except:
        a1 = 0
    try:
        a2 = int(alcohol.get())
    except:
        a2 = 0
    try:
        a3 = int(gambling.get())
    except:
        a3 = 0
    try:
        a4 = int(dining.get())
    except:
        a4 = 0
    try:
        a5 = int(purchase.get())
    except:
        a5 = 0
    try:
        a6 = int(unnecesary.get())
    except:
        a6 = 0
    try:
        a7 = int(visits.get())
    except:
        a7 = 0

    totalcost = a1 + a2 + a3 + a4 + a5 + a6 + a7
    total2 = totalcost * 30

    entry_total2.config(state="normal") 
    entry_total2.delete(0, END)  
    entry_total2.insert(0, str(total2))  
    entry_total2.config(state="readonly")  

    entry_total2.place(x=20, y=60)

    for widget in f22.winfo_children():
        widget.destroy()

    if total2 >= 40000:
        message4 = Label(f22, text="Explore possibilities with this sum by \nallocating towards retirement savings or \nlong-term investments.",font=('Times New Roman', 15), bg="#6497b1", fg="black")
        message4.place(x=60, y=25)
    elif total2 >= 20000:
        message5 = Label(f22, text="Use this fund to Invest in health insurance\n or contribute to existing coverage.",font=('Times New Roman', 15), bg="#6497b1", fg="black")
        message5.place(x=45, y=28)
    elif total2 >= 7000:
        message6 = Label(f22, text="With these funds at your disposal,\n you can Cover rent or mortgage payments.",font=('Times New Roman', 15), bg="#6497b1", fg="black")
        message6.place(x=45, y=28)
    else:
        mes1 = Label(f22, text="Who needs expensive habits? Not you!\n Your financial health is thriving.",font=('Times New Roman', 15), bg="#6497b1", fg="black")
        mes1.place(x=50, y=28)

def Total2():
    try:
        a1 = int(cig.get())
    except:
        a1 = 0
    try:
        a2 = int(alcohol.get())
    except:
        a2 = 0
    try:
        a3 = int(gambling.get())
    except:
        a3 = 0
    try:
        a4 = int(dining.get())
    except:
        a4 = 0
    try:
        a5 = int(purchase.get())
    except:
        a5 = 0
    try:
        a6 = int(unnecesary.get())
    except:
        a6 = 0
    try:
        a7 = int(visits.get())
    except:
        a7 = 0

    totalcost = a1 + a2 + a3 + a4 + a5 + a6 + a7
    total3 = totalcost * 356

    entry_total3.config(state="normal")  
    entry_total3.delete(0, END)  
    entry_total3.insert(0, str(total3))  
    entry_total3.config(state="readonly")  

    entry_total3.place(x=20, y=60)

    for widget in f33.winfo_children():
        widget.destroy()

    if total3 >= 500000:
        message7 = Label(f33, text="Make the most out of this money by \nInvesting in energy-efficient appliances \nfor long-term savings.",font=('Times New Roman', 15), bg="#b3cde0", fg="black")
        message7.place(x=50, y=25)
    elif total3 >= 300000:
        message8 = Label(f33, text="This budget empowers you to contribute\n to a down payment for a property or vehicle.",font=('Times New Roman', 15), bg="#b3cde0", fg="black")
        message8.place(x=30, y=28)
    elif total3 >= 100000:
        message9 = Label(f33, text="Leverage this amount for starting a business\n or contribute to an existing one.",font=('Times New Roman', 15), bg="#b3cde0", fg="black")
        message9.place(x=30, y=28)
    else:
        mes2 = Label(f33, text="Cheers to a bank account that's as \nhealthy as your decision-making skills!",font=('Times New Roman', 15), bg="#b3cde0", fg="black")
        mes2.place(x=50, y=28)



def TotalAll():
    Total()
    Total1()
    Total2()

root = Tk()
root.geometry("1000x490")
root.resizable(False, False)

Label(text="Smart savings, meaningful milestones.", bg="#011f4b", fg="white", font=("Times New Roman", 23), width="300", height="3").pack()

f = Frame(root, bd=5, bg="#03396c", width=400, height=370, relief=RAISED)
f.place(x=0, y=112)

f1 = Frame(root, bg="#005b96", highlightbackground="black", highlightthickness=1, height=126, width=240)
f1.place(x=350, y=111)

f11 = Frame(root, bg="#005b96", highlightbackground="black", highlightthickness=1, height=126, width=435)
f11.place(x=590, y=111)

f2 = Frame(root, bg="#6497b1", highlightbackground="black", highlightthickness=1, height=126, width=240)
f2.place(x=350, y=237)

f22 = Frame(root, bg="#6497b1", highlightbackground="black", highlightthickness=1, height=126, width=435)
f22.place(x=590, y=237)

f3 = Frame(root, bg="#b3cde0", highlightbackground="black", highlightthickness=1, height=129, width=240)
f3.place(x=350, y=362)

f33 = Frame(root, bg="#b3cde0", highlightbackground="black", highlightthickness=1, height=129, width=435)
f33.place(x=590, y=362)

cig = StringVar()
alcohol = StringVar()
gambling = StringVar()
dining = StringVar()
purchase = StringVar()
unnecesary = StringVar()
visits = StringVar()
totalbill = StringVar()
totalbill1 = StringVar()
totalbill2 = StringVar()

lbl_cig = Label(f, font=("Times New Roman", 18), text="Cigarette/E-Cig", width=12, fg="white",bg="#03396c")
lbl_alcohol = Label(f, font=("Times New Roman", 20), text="Alcohol", width=12, fg="white",bg="#03396c")
lbl_gambling = Label(f, font=("Times New Roman", 18), text="Online Gambling", width=12, fg="white",bg="#03396c")
lbl_dining = Label(f, font=("Times New Roman", 15), text="Excessive Dining Out", width=15, fg="white",bg="#03396c")
lbl_purchase = Label(f, font=("Times New Roman", 16), text="Impulsive Purchases", width=15, fg="white",bg="#03396c")
lbl_unnecesary = Label(f, font=("Times New Roman", 16), text="Unnecesary Upgrades", width=15, fg="white",bg="#03396c")
lbl_visits = Label(f, font=("Times New Roman", 15), text="Daily Shop Visits", width=12, fg="white",bg="#03396c")

lbl_cig.grid(row=1, column=0)
lbl_alcohol.grid(row=2, column=0)
lbl_gambling.grid(row=3, column=0)
lbl_dining.grid(row=4, column=0)
lbl_purchase.grid(row=5, column=0)
lbl_unnecesary.grid(row=6, column=0)
lbl_visits.grid(row=7, column=0)

entry_cig = Entry(f, font=("Times New Roman", 20, 'bold'), textvariable=cig, bd=6, width=10, bg="#b3c3d2")
entry_alcohol = Entry(f, font=("Times New Roman", 20, 'bold'), textvariable=alcohol, bd=6, width=10, bg="#b3c3d2")
entry_gambling = Entry(f, font=("Times New Roman", 20, 'bold'), textvariable=gambling, bd=6, width=10, bg="#b3c3d2")
entry_dining = Entry(f, font=("Times New Roman", 20, 'bold'), textvariable=dining, bd=6, width=10, bg="#b3c3d2")
entry_purchase = Entry(f, font=("Times New Roman", 20, 'bold'), textvariable=purchase, bd=6, width=10, bg="#b3c3d2")
entry_unnecesary = Entry(f, font=("Times New Roman", 20, 'bold'), textvariable=unnecesary, bd=6, width=10, bg="#b3c3d2")
entry_visits = Entry(f, font=("Times New Roman", 20, 'bold'), textvariable=visits, bd=6, width=10, bg="#b3c3d2")

entry_cig.grid(row=1, column=1)
entry_alcohol.grid(row=2, column=1)
entry_gambling.grid(row=3, column=1)
entry_dining.grid(row=4, column=1)
entry_purchase.grid(row=5, column=1)
entry_unnecesary.grid(row=6, column=1)
entry_visits.grid(row=7, column=1)

btn_reset = Button(f, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Reset", command=Reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(f, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Total", command=TotalAll)
btn_total.grid(row=8, column=1)

entry_total = Entry(f1, font=('Times New Roman', 20, 'bold'), textvariable=totalbill, bd=6, width=12, bg="lightgreen", state="readonly")

entry_total2 = Entry(f2, font=('Times New Roman', 20, 'bold'), textvariable=totalbill1, bd=6, width=12, bg="lightgreen", state="readonly")

entry_total3 = Entry(f3, font=('Times New Roman', 20, 'bold'), textvariable=totalbill2, bd=6, width=12, bg="lightgreen", state="readonly")

lbl_total = Label(f1, text="In a Day", font=('Times New Roman', 16, 'bold'), bg="#005b96")
lbl_total.place(x=20, y=20)

lbl_totalm = Label(f2, text="In a Month", font=('Times New Roman', 16, 'bold'), bg="#6497b1")
lbl_totalm.place(x=20, y=20)

lbl_totaly = Label(f3, text="In a Year", font=('Times New Roman', 16, 'bold'), bg="#b3cde0")
lbl_totaly.place(x=20, y=20)


root.mainloop()