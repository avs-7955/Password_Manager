from tkinter import *
# --------------------PASSWORD GENERATOR -------------------- #

# ----------------- SAVE PASSWORD --------------------- #

# --------------------- UI SETUP ------------------------ #
# Creating a window
window = Tk()
window.title("My Pass")
window.config(padx=20, pady=20)
# window.minsize(width=240, height=240)


# Creating a Canvas widget
canvas = Canvas(height=200, width=200)
# Importing image
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.pack()

window.mainloop()
