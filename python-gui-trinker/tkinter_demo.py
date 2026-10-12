import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = pass_input.get()

    if email == "sehaj@gmail.com" and password == "1234":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Login Failed")

root = tk.Tk()

# used to change the title
root.title("Login")
# used to change the logo
root.iconbitmap('icon.png')
# minimum size
#root.minsize(800, 600)
#maxsize
#root.maxsize(1000, 800)
# to create a window for a specific size
root.geometry("350x500")
# to set a background color
root.configure(bg="#0096DC")
# resize an image
img = Image.open("flipcart.jpg")
resize_image = img.resize((70,70))
img = ImageTk.PhotoImage(resize_image) # img = ImageTk.PhotoImage(Image.open("flipcart.jpg")) or img = ImageTk.PhotoImage(file="flipcart.jpg")
img_label = tk.Label(root, image=img)

img_label.pack(pady=(10,10))

text_label = tk.Label(root, text="Flipkart", fg="white", bg="#0096DC")
text_label.pack()
text_label.config(font=("Arial", 24))

email_label = tk.Label(root, text="Enter Email:", fg="white", bg="#0096DC")
email_label.pack(pady=(20,5))
email_label.config(font=("Arial", 12))

email_input = tk.Entry(root, width=40)
email_input.pack(ipady=6, pady=(1,15))

pass_label = tk.Label(root, text="Enter Password:", fg="white", bg="#0096DC")
pass_label.pack(pady=(20,5))
pass_label.config(font=("Arial", 12))

pass_input = tk.Entry(root, width=40)
pass_input.pack(ipady=6, pady=(1,15))

login_button = tk.Button(root, text="Login", fg="black", bg="white", width=20, height=2, command=handle_login)
login_button.pack(pady=(10,20))
login_button.config(font=("Arial", 10))

root.mainloop()