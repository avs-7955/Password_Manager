import json
import pyperclip
from random import randint, choice, shuffle
from tkinter import messagebox
from tkinter import *
# Change this to your most frequently used email id.
EMAIL_ID = "dummy@gmail.com"


# --------------------PASSWORD GENERATOR --------------------#


def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Getting a random required length for numbers,symbols and letters and using list comprehension to generate list of random letters, numbers and symbols
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Merging all into one list and shuffling them
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Converting the list into a string
    password = "".join(password_list)

    pwd_entry.insert(0, password)
    pyperclip.copy(password)


# ----------------- SAVE PASSWORD --------------------- #


def save():
    # Getting the entries
    website = website_entry.get()
    email = user_name_entry.get()
    pwd = pwd_entry.get()
    # Making a json object
    new_data = {
        website: {
            "email": email,
            "password": pwd,
        }
    }

    # If any website or password empty - show error message
    if(len(website) == 0 or len(pwd) == 0):
        messagebox.showwarning(
            title="Oops!", message="Please don't leave any fields empty.")
    else:
        try:
            # Writing the entries in the json file
            with open("data.json", mode='r') as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old data
            data.update(new_data)

            with open("data.json", mode='w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Deleting the entries for a fresh entry
            website_entry.delete(0, 'end')
            pwd_entry.delete(0, 'end')
            # Bring the focus back to website entry for smooth user experience
            website_entry.focus()


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

canvas.grid(row=0, column=1)

# Website label
website_label = Label(text="Website:", width=16)
website_label.grid(row=1, column=0, pady=4)

# Website entry
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2, pady=4)
# To autofocus it as soon as the app is launched.
website_entry.focus()

# user_name label
user_name_label = Label(text="Email/Username:", width=16)
user_name_label.grid(row=2, column=0, pady=4)

# user_name entry
user_name_entry = Entry(width=45)
user_name_entry.grid(row=2, column=1, columnspan=2, pady=4)
# Adding predefined email id so that entry is already filled with our primary email id when program starts.
user_name_entry.insert(0, EMAIL_ID)

# pwd label
pwd_label = Label(text="Password:", width=16)
pwd_label.grid(row=3, column=0, pady=4)

# pwd entry
pwd_entry = Entry(width=45)
pwd_entry.grid(row=3, column=1, columnspan=2, pady=4)

# generate password button
gen_pwd = Button(text="Generate Password",
                 relief="raised", width=18, command=generate_pwd)
gen_pwd.grid(row=4, column=1, pady=4, sticky="w", padx=0)


# Add button
add_pwd = Button(text="Add", relief="raised",
                 highlightthickness=0, width=38, command=save)
add_pwd.grid(row=5, column=1, pady=4, columnspan=2)

# Search button
search_btn = Button(text="Search Password", width=18)
search_btn.grid(row=4, column=2, pady=4, columnspan=1, sticky="w")

window.mainloop()
