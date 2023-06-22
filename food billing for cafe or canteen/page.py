from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Canteen Management System")

Tops = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

# ------------------TIME--------------
localtime = time.asctime(time.localtime(time.time()))

# -----------------INFO TOP------------
lblinfo = Label(Tops, font=('aria', 50, 'bold'), text="Canteen Management System", fg="steel blue", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 20), text=localtime, fg="steel blue", anchor=W)
lblinfo.grid(row=1, column=0)

# ---------------Calculator------------------
text_Input = StringVar()
operator = ""

txtdisplay = Entry(f2, font=('ariel', 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg="white",
                   justify='right')
txtdisplay.grid(columnspan=4)


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def clrdisplay():
    global operator
    operator = ""
    text_Input.set("")


def equals():
    global operator
    sumup = str(eval(operator))

    text_Input.set(sumup)
    operator = ""


def Ref():
    x = random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof = float(Fries.get())
    colfries = float(Largefries.get())
    cob = float(Burger.get())
    cofi = float(Filet.get())
    cochee = float(Cheese_burger.get())
    codr = float(Drinks.get())

    costoffries = cof * 35
    costoflargefries = colfries * 75
    costofburger = cob * 40
    costoffilet = cofi * 190
    costofcheeseburger = cochee * 50
    costofdrinks = codr * 35

    costofmeal = "Rs." + str('%.2f' % (costoffries + costoflargefries + costofburger + costoffilet +
                                       costofcheeseburger + costofdrinks))
    PayTax = ((costoffries + costoflargefries + costofburger + costoffilet +
               costofcheeseburger + costofdrinks) * 0.33)
    Totalcost = costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks
    Ser_Charge = Totalcost / 99
    Service = "Rs." + str('%.2f' % Ser_Charge)
    OverAllCost = "Rs." + str(PayTax + Totalcost + Ser_Charge)
    PaidTax = "Rs." + str('%.2f' % PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()


def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")


# ---------------Buttons-----------------
btn7 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="7", bg="powder blue",
              command=lambda: btnclick(7))
btn7.grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="8", bg="powder blue",
              command=lambda: btnclick(8))
btn8.grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="9", bg="powder blue",
              command=lambda: btnclick(9))
btn9.grid(row=2, column=2)

btnC = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="C", bg="powder blue",
              command=clrdisplay)
btnC.grid(row=2, column=3)

btn4 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="4", bg="powder blue",
              command=lambda: btnclick(4))
btn4.grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="5", bg="powder blue",
              command=lambda: btnclick(5))
btn5.grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="6", bg="powder blue",
              command=lambda: btnclick(6))
btn6.grid(row=3, column=2)

btnplus = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="+", bg="powder blue",
                 command=lambda: btnclick("+"))
btnplus.grid(row=3, column=3)

btn1 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="1", bg="powder blue",
              command=lambda: btnclick(1))
btn1.grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="2", bg="powder blue",
              command=lambda: btnclick(2))
btn2.grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="3", bg="powder blue",
              command=lambda: btnclick(3))
btn3.grid(row=4, column=2)

btnminus = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="-", bg="powder blue",
                  command=lambda: btnclick("-"))
btnminus.grid(row=4, column=3)

btn0 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="0", bg="powder blue",
              command=lambda: btnclick(0))
btn0.grid(row=5, column=0)

btnequal = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="=", bg="powder blue",
                  command=equals)
btnequal.grid(row=5, column=1)

btndiv = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="/", bg="powder blue",
                command=lambda: btnclick("/"))
btndiv.grid(row=5, column=2)

btnmult = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="*", bg="powder blue",
                 command=lambda: btnclick("*"))
btnmult.grid(row=5, column=3)

# ------------------RESTAURANT INFO 1----------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()

lblreference = Label(f1, font=('ariel', 16, 'bold'), text="Reference", bd=16, anchor='w')
lblreference.grid(row=0, column=0)
txtreference = Entry(f1, font=('ariel', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="powder blue",
                     justify='right')
txtreference.grid(row=0, column=1)

lblfries = Label(f1, font=('ariel', 16, 'bold'), text="Fries", bd=16, anchor='w')
lblfries.grid(row=1, column=0)
txtfries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg="powder blue",
                 justify='right')
txtfries.grid(row=1, column=1)

lblLargefries = Label(f1, font=('ariel', 16, 'bold'), text="Lunch Meal", bd=16, anchor='w')
lblLargefries.grid(row=2, column=0)
txtLargefries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Largefries, bd=10, insertwidth=4, bg="powder blue",
                      justify='right')
txtLargefries.grid(row=2, column=1)

lblburger = Label(f1, font=('ariel', 16, 'bold'), text="Burger Meal", bd=16, anchor='w')
lblburger.grid(row=3, column=0)
txtburger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg="powder blue",
                  justify='right')
txtburger.grid(row=3, column=1)

lblFilet = Label(f1, font=('ariel', 16, 'bold'), text="Pizza Meal", bd=16, anchor='w')
lblFilet.grid(row=4, column=0)
txtFilet = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Filet, bd=10, insertwidth=4, bg="powder blue",
                 justify='right')
txtFilet.grid(row=4, column=1)

lblCheese_burger = Label(f1, font=('ariel', 16, 'bold'), text="Cheese Burger", bd=16, anchor='w')
lblCheese_burger.grid(row=5, column=0)
txtCheese_burger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Cheese_burger, bd=10, insertwidth=4,
                         bg="powder blue", justify='right')
txtCheese_burger.grid(row=5, column=1)

# ------------------RESTAURANT INFO 2----------
lbldrinks = Label(f1, font=('ariel', 16, 'bold'), text="Drinks", bd=16, anchor='w')
lbldrinks.grid(row=0, column=2)
txtdrinks = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="powder blue",
                  justify='right')
txtdrinks.grid(row=0, column=3)

lblcost = Label(f1, font=('ariel', 16, 'bold'), text="Cost of Meal", bd=16, anchor='w')
lblcost.grid(row=1, column=2)
txtcost = Entry(f1, font=('ariel', 16, 'bold'), textvariable=cost, bd=10, insertwidth=4, bg="powder blue",
                justify='right')
txtcost.grid(row=1, column=3)

lblService_Charge = Label(f1, font=('ariel', 16, 'bold'), text="Service Charge", bd=16, anchor='w')
lblService_Charge.grid(row=2, column=2)
txtService_Charge = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4,
                          bg="powder blue", justify='right')
txtService_Charge.grid(row=2, column=3)

lblTax = Label(f1, font=('ariel', 16, 'bold'), text="GST", bd=16, anchor='w')
lblTax.grid(row=3, column=2)
txtTax = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="powder blue",
               justify='right')
txtTax.grid(row=3, column=3)

lblSubtotal = Label(f1, font=('ariel', 16, 'bold'), text="Sub Total", bd=16, anchor='w')
lblSubtotal.grid(row=4, column=2)
txtSubtotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Subtotal, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtSubtotal.grid(row=4, column=3)

lblTotal = Label(f1, font=('ariel', 16, 'bold'), text="Total Cost", bd=16, anchor='w')
lblTotal.grid(row=5, column=2)
txtTotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="powder blue",
                 justify='right')
txtTotal.grid(row=5, column=3)

# ------------------Buttons-----------------
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('ariel', 16, 'bold'), width=10, text="Total",
                  bg="powder blue", command=Ref)
btnTotal.grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('ariel', 16, 'bold'), width=10, text="Reset",
                  bg="powder blue", command=reset)
btnReset.grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('ariel', 16, 'bold'), width=10, text="Exit",
                 bg="powder blue", command=qexit)
btnExit.grid(row=7, column=3)

root.mainloop()
