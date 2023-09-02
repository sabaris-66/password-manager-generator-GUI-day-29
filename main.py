from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    random_password = "".join(password_list)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    # random.shuffle(password_list)
    #
    # password = ""
    # for char in password_list:
    #   password += char

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title='Error', message="Please fill all the boxes")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\nClick OK to save")
        new_data = {website:
                        {'email': email,
                         'password': password}
                    }
        if is_ok:
            with open('data.json', 'r') as file:
                try:
                    data = json.load(file)
                    data.update(new_data)
                except:
                    with open('data.json', 'w') as file2:
                        json.dump(new_data, file2, indent=4)
                else:
                    with open('data.json', 'w') as file3:
                        json.dump(data, file3, indent=4)


            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

def search_password():
    with open('data.json', 'r') as file:
        saved_data = json.load(file)
        web = website_entry.get()
        try:
            req_password = saved_data[web]['password']
            req_email = saved_data[web]['email']
        except KeyError:
            messagebox.askokcancel(title="NO DATA", message="Sorry no data found related to this website")
        else:
            messagebox.askokcancel(title="Password Found", message=f"Email: {req_email}\nPassword: {req_password}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager / Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

search_button = Button(text="Search", command=search_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sabaris.elango@gmail.com")

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=pass_gen)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()