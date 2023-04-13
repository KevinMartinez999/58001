import tkinter as tk

window = tk.Tk()
window.geometry("1000x600")
window.title("Full Name")

label1 = tk.Label(window, text="Given Name:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(window, text="Middle Name:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=5, pady=5)

label3 = tk.Label(window, text="Last Name:")
label3.grid(row=2, column=0, padx=5, pady=5)

entry3 = tk.Entry(window)
entry3.grid(row=2, column=1, padx=5, pady=5)

def show_full_name():
    full_name = entry1.get() + " " + entry2.get() + " " + entry3.get()
    entry4.delete(0, tk.END)
    entry4.insert(0, full_name)

button = tk.Button(window, text="Show Full Name", command=show_full_name)
button.grid(row=3, column=0, padx=5, pady=5)

entry4 = tk.Entry(window)
entry4.grid(row=3, column=1, padx=5, pady=5)

window.mainloop()

