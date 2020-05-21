"""
GUI designed for FSAN 85O project
"""

from tkinter import *
from tkinter import ttk
import math

def logistic():
    month = int(number.get())
    week = int(number2.get())

    date = (month-1)*4+week

    store_binary = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(),
                    var9.get(), var10.get(), var11.get(), var12.get(), var13.get(), var14.get(), var15.get(),
                    var16.get(), var17.get(), var18.get(), var19.get(), var20.get(), var21.get(), var22.get()]
    item_binary = [var23.get(), var24.get(), var25.get(), var26.get(), var27.get(), var28.get(), var29.get(),
                   var30.get(), var31.get(),
                   var32.get(), var33.get(), var34.get(), var35.get()]

    if sum(store_binary) * sum(item_binary) != 0:
        # calculate the probability
        b = 0
        # add the intercept
        b += -2.161486268

        store_coef = [0.075866061, 2.122238923, 1.251225426, -0.681844397, -0.445444528, -0.301341894, -1.581023881,
                      0.030883165, -2.37019748, -1.000643356, -1.276698549, -1.849610559, -1.895757733, 1.819744946,
                      0.990535624, -0.041889615, 1.884292247, -1.151375689, 2.019207813, -0.256686959, 2.267949673,
                      -1.467926862]
        item_coef = [0.981817722, -0.261769432, -0.604375483, -0.237550422, -0.152160607, 1.103607193, -0.003113623,
                     -0.611685841, 0.768833052, - 1.075925181, 0.648577934, -0.47884605, -1.935906885]

        # add the coefficients for stores
        for i in range(len(store_coef)):
            b += store_coef[i] * store_binary[i]
        # add the coefficients for items
        for j in range(len(item_coef)):
            b += item_coef[j] * item_binary[j]
        # add the week
        b += 0.001371503 * date
        p = math.exp(b)/(math.exp(b)+1)
        print(f"The probability that on sale is {p}")

if __name__ == '__main__':
    master = Tk()
    master.title("FSAN 850 Project: Savvy Sue")
    # title for the whole project
    Label(master, text="Savvy Sue: What is the probability that on sale?").grid(row=0, column=1, sticky=W)

    Label(master, text="Store Choice:").grid(row=1, sticky=W)
    var1 = IntVar()
    Checkbutton(master, text="Adidas", variable=var1).grid(row=2, sticky=W)
    var2 = IntVar()
    Checkbutton(master, text="Bestbuy", variable=var2).grid(row=3, sticky=W)
    var3 = IntVar()
    Checkbutton(master, text="Bloomingdales", variable=var3).grid(row=4, sticky=W)
    var4 = IntVar()
    Checkbutton(master, text="Calvin Klein", variable=var4).grid(row=5, sticky=W)
    var5 = IntVar()
    Checkbutton(master, text="Costco", variable=var5).grid(row=6, sticky=W)
    var6 = IntVar()
    Checkbutton(master, text="Express", variable=var6).grid(row=7, sticky=W)
    var7 = IntVar()
    Checkbutton(master, text="Gap", variable=var7).grid(row=8, sticky=W)
    var8 = IntVar()
    Checkbutton(master, text="H&M", variable=var8).grid(row=9, sticky=W)
    var9 = IntVar()
    Checkbutton(master, text="Hollister", variable=var9).grid(row=10, sticky=W)
    var10 = IntVar()
    Checkbutton(master, text="J Crew", variable=var10).grid(row=11, sticky=W)
    var11 = IntVar()
    Checkbutton(master, text="J Crew Factory", variable=var11).grid(row=12, sticky=W)
    var12 = IntVar()
    Checkbutton(master, text="Levis", variable=var12).grid(row=13, sticky=W)
    var13 = IntVar()
    Checkbutton(master, text="Lowes", variable=var13).grid(row=14, sticky=W)
    var14 = IntVar()
    Checkbutton(master, text="Macy's", variable=var14).grid(row=15, sticky=W)
    var15 = IntVar()
    Checkbutton(master, text="Neiman Marcus", variable=var15).grid(row=16, sticky=W)
    var16 = IntVar()
    Checkbutton(master, text="Nike", variable=var16).grid(row=17, sticky=W)
    var17 = IntVar()
    Checkbutton(master, text="Nordstorm", variable=var17).grid(row=18, sticky=W)
    var18 = IntVar()
    Checkbutton(master, text="Sam's Club", variable=var18).grid(row=19, sticky=W)
    var19 = IntVar()
    Checkbutton(master, text="Sephora", variable=var19).grid(row=20, sticky=W)
    var20 = IntVar()
    Checkbutton(master, text="Uniqlo", variable=var20).grid(row=21, sticky=W)
    var21 = IntVar()
    Checkbutton(master, text="Walmart", variable=var21).grid(row=22, sticky=W)
    var22 = IntVar()
    Checkbutton(master, text="Zara", variable=var22).grid(row=23, sticky=W)

    Label(master, text="Item Choice:").grid(row=1, column=2, sticky=W)
    var23 = IntVar()
    Checkbutton(master, text="Acessory", variable=var23).grid(row=2, column=2, sticky=W)
    var24 = IntVar()
    Checkbutton(master, text="Computer", variable=var24).grid(row=3, column=2, sticky=W)
    var25 = IntVar()
    Checkbutton(master, text="Dress", variable=var25).grid(row=4, column=2, sticky=W)
    var26 = IntVar()
    Checkbutton(master, text="Eyes Makeup", variable=var26).grid(row=5, column=2, sticky=W)
    var27 = IntVar()
    Checkbutton(master, text="Headphone & Speaker", variable=var27).grid(row=6, column=2, sticky=W)
    var28 = IntVar()
    Checkbutton(master, text="Lip", variable=var28).grid(row=7, column=2, sticky=W)
    var29 = IntVar()
    Checkbutton(master, text="Makeup", variable=var29).grid(row=8, column=2, sticky=W)
    var30 = IntVar()
    Checkbutton(master, text="Outerwear", variable=var30).grid(row=9, column=2, sticky=W)
    var31 = IntVar()
    Checkbutton(master, text="Shoe", variable=var31).grid(row=10, column=2, sticky=W)
    var32 = IntVar()
    Checkbutton(master, text="Skin Makeup", variable=var32).grid(row=11, column=2, sticky=W)
    var33 = IntVar()
    Checkbutton(master, text="TV", variable=var33).grid(row=12, column=2, sticky=W)
    var34 = IntVar()
    Checkbutton(master, text="Top", variable=var34).grid(row=13, column=2, sticky=W)
    var35 = IntVar()
    Checkbutton(master, text="Underwear", variable=var35).grid(row=14, column=2, sticky=W)

    # get the week information
    Label(master, text="What is your expected purchase date?").grid(row=25, column=0, sticky=W)

    Label(master, text="Month:").grid(row=26, column=0, sticky=W)
    number = StringVar()
    numberChosen = ttk.Combobox(master, textvariable=number)
    numberChosen['value'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    numberChosen.grid(row=26, column=1, sticky=W)
    numberChosen.current(0)

    Label(master, text="Week:").grid(row=26, column=2, sticky=W)
    number2 = StringVar()
    numberChosen2 = ttk.Combobox(master, textvariable=number2)
    numberChosen2['value'] = (1, 2, 3, 4)
    numberChosen2.grid(row=26, column=3, sticky=W)
    numberChosen2.current(0)

    Button(master, text='Show', command=logistic).grid(row=27, column=1, sticky=W, pady=4)
    Button(master, text='Quit', command=master.quit).grid(row=27, column=2, sticky=W, pady=4)
    mainloop()
