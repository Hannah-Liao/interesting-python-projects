from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbols

    shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website1 = website_entry.get()
    email1 = email_entry.get()
    password1 = password_entry.get()

    if len(website1) == 0 or len(password1) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website1,
                                       message=f"These are the details entered: \n {website1} | {email1} | {password1} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website1} | {email1} | {password1} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 110, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_entry = Entry(width=39)
email_entry.insert(0, "example@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(column=2, row=3)

add_btn = Button(width=36, text="Add", command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
