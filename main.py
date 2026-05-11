from tkinter import *
from tkinter import messagebox
import random
import json


window = Tk()
window.title("Password manager")
window.config(bg="#1E293B", padx=30, pady=20)

canvas = Canvas()
canvas.config(bg="#1E293B", width=200, height=190, highlightthickness=0)
logo_image = PhotoImage(file="assets/password_manager_logo_200x200.png")
canvas.create_image(100, 95, image=logo_image)
canvas.grid(column=1, row=0)


def confirm_action():
    website = website_input.get().strip()
    email = email_input.get().strip()
    password = password_input.get().strip()
    if all([website, email, password]):
        answer = messagebox.askyesno(title=website_input.get(), message=f"Email: {email_input.get()}\nPassword:"
                                                                        f" {password_input.get()}\nIs this ok?")
        new_data = {
            website:{
                    "email": email,
                    "password": password,
            }
        }
        if answer:
            try:
                with open("password_data.json", "r", encoding="utf-8") as file:
                    # Reading old data
                    data = json.load(file)
                    # Updating old data with new data
                    data.update(new_data)
                with open("password_data.json", "w", encoding="utf-8") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                with open("password_data.json", "w", encoding="utf-8") as file:
                    # Saving updated data
                    json.dump(new_data, file, indent=4)

                messagebox.showinfo(title="Saved", message="Password saved successfully.")
            finally:
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="Fill all the blank spaces and try again")


def generate_password():
    window.clipboard_clear()
    password = ""
    for i in range(18):
        random_code = random.randint(32, 126)
        password += chr(random_code)
    password_input.insert(0, password)
    window.clipboard_append(password_input.get())


def search():
    try:
        with open("password_data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data not found.")

    else:
        if website_input.get() not in data:
            messagebox.showinfo(title="Site not found", message="Check for spelling errors or try another site.")
        else:
            messagebox.showinfo(title=website_input.get(), message=f"Email: {data[website_input.get()]["email"]}\n"
                                                                   f"Password:{data[website_input.get()]["password"]}")


website_label = Label(fg="#FFFFFF", bg="#1E293B", text="Website:", font=("Montserrat Font", 8, "bold"))
website_label.grid(column=0, row=1, padx=5, pady=5)

website_input = Entry(window, bg="#39FF14")
website_input.grid(column=1, row=1, sticky="ew", padx=5, pady=5)
website_input.focus()

email_label = Label(fg="#FFFFFF", bg="#1E293B", text="Email/Username:", font=("Montserrat Font", 8, "bold"))
email_label.grid(column=0, row=2, padx=5, pady=5)

email_input = Entry(window, bg="#39FF14")
email_input.grid(column=1, row=2, columnspan=2, sticky="nsew", padx=5, pady=5)

password_label = Label(fg="#FFFFFF", bg="#1E293B", text="Password:", font=("Montserrat Font", 8, "bold"))
password_label.grid(column=0, row=3, padx=5, pady=5)

password_input = Entry(window, bg="#39FF14")
password_input.grid(column=1, row=3, sticky = "ew", padx=5, pady=5)

add_button = Button(fg="#FFFFFF",bg="#0066FF", text="Add", command=confirm_action, font=("Montserrat Font", 8, "bold"))
add_button.grid(column=1, row=4, columnspan= 2, sticky="nsew", padx=5, pady=5)

generate_button = Button(fg="#FFFFFF",bg="#0066FF", text="Generate Password", command=generate_password, font=("Montserrat Font", 8, "bold"))
generate_button.grid(column=2, row=3, sticky = "nsew", padx=5, pady=5)

search_button = Button(fg="#FFFFFF",bg="#0066FF", text="Search", command=search, font=("Montserrat Font", 8, "bold"))
search_button.grid(row=1, column=2, sticky = "nsew", padx=5, pady=5)




window.mainloop()