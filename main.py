from tkinter import *
from tkinter import messagebox
import sys
import random
import pyperclip
import json
from sqlalchemy.engine.result import null_result


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_entry.delete(0, END)
    #password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def show_error():
    messagebox.showerror("Error", "Please fill all mandatory fields")
    sys.exit()
def save():

    website = Website_entry.get()
    email = Email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email:" : email,
            "password:" : password
        }

    }
    if len(website) ==0 or  len(password) ==0:
        show_error()
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            Website_entry.delete(0, END)
            Email_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
        website = Website_entry.get()
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                if website in data:
                    email = data[website]["email:"]
                    password = data[website]["password:"]
                    messagebox.showinfo(website, f"Email: {email}\n password: {password}")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")

        except KeyError:
            messagebox.showerror("Error", "Website not found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

Canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
Canvas.create_image(100, 100, image=logo)
Canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1,column=0)

search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)

email = Label(text="Email/Username:")
email.grid(row=2,column=0)


password = Label(text="Password:")
password.grid(row=3,column=0)

Website_entry = Entry(width=21)
Website_entry.grid(row=1,column=1)
Email_entry = Entry(width=38)
Email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

add_password_button = Button(text="Add",width=36, command=save)
add_password_button.grid(row=4,column=1,columnspan=2)
window.mainloop()


