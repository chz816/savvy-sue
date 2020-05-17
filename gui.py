import tkinter as tk

def result(date):
    """
    Calculate the probability for logisctic regression
    """
    return 0

# Set-up the window
window = tk.Tk()
window.title("Savvy Sue")
window.geometry("500x500")
window.resizable(width=True, height=True)

# first line: start
start_entry = tk.Frame(master=window)
expected_date = tk.Entry(master=start_entry, width=10)
start_label = tk.Label(master=start_entry, text="Expected Date: ")

expected_date.grid(row=0, column=1)
start_label.grid(row=0, column=0)

# get the selected choice
store_entry = tk.Frame(master=window)
lbl_temp = tk.Label(master=store_entry, text="Store Choice")
adidas = tk.Button(master=store_entry, text="adidas")
bestbuy = tk.Button(master=store_entry, text="bestbuy")


# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
lbl_temp.grid(row=0, column=0, sticky="w")
adidas.grid(row=2, column=0, sticky="e")
bestbuy.grid(row=3, column=0, sticky="e")

# get the selected categories
category = tk.Frame(master=window)
cat_temp = tk.Label(master=store_entry, text="Category Choice")
accessory = tk.Button(master=store_entry, text="accessory")
top = tk.Button(master=store_entry, text="top")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
cat_temp.grid(row=0, column=1, sticky="w")
accessory.grid(row=2, column=1, sticky="e")
top.grid(row=3, column=1, sticky="e")




# Create the conversion Button and result display Label
prediction = tk.Button(master=window, text="Get Prediction", command=result)

prob = tk.Label(master=window, text="On Sale Probability: ")


# Set-up the layout using the .grid() geometry manager
start_entry.grid(row=0, column=0, padx=10)
store_entry.grid(row=1, column=0, padx=10)
category.grid(row=1, column=1, padx=10)

prediction.grid(row=2, column=0, pady=10)
prob.grid(row=3, column=0, padx=10)

# Run the application
window.mainloop()