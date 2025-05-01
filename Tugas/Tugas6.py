import tkinter as tk
from tkinter import messagebox


users = {}

def open_register_window():
    reg_win = tk.Toplevel(root)
    reg_win.title("Register")
    reg_win.geometry("300x150")

    tk.Label(reg_win, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
    username_entry = tk.Entry(reg_win)
    username_entry.grid(row=0, column=1)

    tk.Label(reg_win, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
    password_entry = tk.Entry(reg_win, show="*")
    password_entry.grid(row=1, column=1)

    def register_user():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            if username in users:
                messagebox.showerror("Error", "Username sudah terdaftar")
            else:
                users[username] = password
                messagebox.showinfo("Registrasi berhasil", "Kamu telah terdaftar")
                reg_win.destroy()
        else:
            messagebox.showwarning("Warning", "Tolong isi semua field")

    tk.Button(reg_win, text="Register", command=register_user).grid(row=2, columnspan=2, pady=10)


def open_todolist(username):
    todo_win = tk.Toplevel(root)
    todo_win.title("To-Do List - " + username)
    todo_win.geometry("400x300")

    tasks = []

    task_entry = tk.Entry(todo_win, width=30)
    task_entry.pack(pady=10)

    task_listbox = tk.Listbox(todo_win, width=50)
    task_listbox.pack()

    def add_task():
        task = task_entry.get()
        if task:
            tasks.append(task)
            task_listbox.insert(tk.END, task)
            task_entry.delete(0, tk.END)

    def remove_task():
        selected = task_listbox.curselection()
        if selected:
            index = selected[0]
            task_listbox.delete(index)
            tasks.pop(index)

    tk.Button(todo_win, text="Tambah tugas", command=add_task).pack(pady=5)
    tk.Button(todo_win, text="Hapus tugas", command=remove_task).pack()


def login_user():
    username = username_var.get()
    password = password_var.get()
    if username in users and users[username] == password:
        messagebox.showinfo("Login Berhasil", f"Selamat Datang, {username}!")
        open_todolist(username)
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah")

# ---------------------- Main Window ---------------------- #
root = tk.Tk()
root.title("Login")
root.geometry("300x150")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
username_var = tk.StringVar()
tk.Entry(root, textvariable=username_var).grid(row=0, column=1)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, show="*").grid(row=1, column=1)

tk.Button(root, text="Login", command=login_user).grid(row=2, column=0, pady=10)
tk.Button(root, text="Register", command=open_register_window).grid(row=2, column=1)

root.mainloop()
