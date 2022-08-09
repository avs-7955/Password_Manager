from tkinter import *
# --------------------PASSWORD GENERATOR -------------------- #

# ----------------- SAVE PASSWORD --------------------- #

# --------------------- UI SETUP ------------------------ #
# Creating a window
window = Tk()
window.title("My Pass")
window.config(padx=50, pady=50)
# window.minsize(width=240, height=240)


# Creating a Canvas widget
canvas = Canvas(height=200, width=200, highlightthickness=0)
# Importing image
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=0, column=1, padx=10, pady=10)

# Website label
website_label = Label(text="Website:", width=16)
website_label.grid(row=1, column=0, pady=4)

# Website entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, pady=4)

# user_name label
user_name_label = Label(text="Email/Username:", width=16)
user_name_label.grid(row=2, column=0, pady=4)

# user_name entry
user_name_entry = Entry(width=35)
user_name_entry.grid(row=2, column=1, columnspan=2, pady=4)

# pwd label
pwd_label = Label(text="Password:", width=16)
pwd_label.grid(row=3, column=0, pady=4)

# pwd entry
pwd_entry = Entry(width=35)
pwd_entry.grid(row=3, column=1, columnspan=2, pady=4)

# generate password button
gen_pwd = Button(text="Generate Password", relief="raised", width=17)
gen_pwd.grid(row=4, column=1, pady=4)


# Add button
add_pwd = Button(text="Add", relief="raised", highlightthickness=0, width=17)
add_pwd.grid(row=4, column=2, pady=4, padx=2, sticky=W)


window.mainloop()
