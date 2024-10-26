import tkinter as tk
from tkinter import messagebox

def validate_login():
    username=entry_username.get()
    password=entry_password.get()
    if username=="username"and password=="password":
        messagebox.showinfo("Login Success","Welcome!!!!")
    else:
        messagebox.showerror("login failed","Invalid credentials.Please try again")
root=tk.Tk()
root.title("Login Page")
root.geometry("300x200")
label_username=tk.Label(root,text="Username:")
label_username.pack(pady=10)

entry_username=tk.Entry(root)
entry_username.pack(pady=5)

label_password=tk.Label(root,text="Password:")
label_password.pack(pady=10)

entry_password=tk.Entry(root,show='*')
entry_password.pack(pady=5)

button_login=tk.Button(root,text="Login",command=validate_login)
button_login.pack(pady=20)

root.mainloop()