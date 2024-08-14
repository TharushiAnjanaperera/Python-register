import tkinter as tk
from tkinter import messagebox
import mysql.connector

def register_user():
    firstname = entry_first_name.get()
    lastname = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()

 
    if not (firstname and lastname and email and password):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

   
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="register"
        )
        cursor = conn.cursor()

      
        cursor.execute("INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)",
                       (firstname, lastname, email, password))

        conn.commit()
        messagebox.showinfo("Success", "Registration Successful!")
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

root = tk.Tk()
root.title("User Registration")
root.geometry("400x300")


root.eval('tk::PlaceWindow . center')

tk.Label(root, text="First Name", font=('Arial', 12)).grid(row=0, column=0, pady=10, padx=10, sticky="e")
entry_first_name = tk.Entry(root, font=('Arial', 12), width=25)
entry_first_name.grid(row=0, column=1, pady=10, padx=10)

tk.Label(root, text="Last Name", font=('Arial', 12)).grid(row=1, column=0, pady=10, padx=10, sticky="e")
entry_last_name = tk.Entry(root, font=('Arial', 12), width=25)
entry_last_name.grid(row=1, column=1, pady=10, padx=10)

tk.Label(root, text="Email", font=('Arial', 12)).grid(row=2, column=0, pady=10, padx=10, sticky="e")
entry_email = tk.Entry(root, font=('Arial', 12), width=25)
entry_email.grid(row=2, column=1, pady=10, padx=10)

tk.Label(root, text="Password", font=('Arial', 12)).grid(row=3, column=0, pady=10, padx=10, sticky="e")
entry_password = tk.Entry(root, font=('Arial', 12), width=25, show="*")
entry_password.grid(row=3, column=1, pady=10, padx=10)

tk.Button(root, text="Register", font=('Arial', 12), command=register_user).grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
