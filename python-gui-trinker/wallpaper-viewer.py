import tkinter as tk
from PIL import Image, ImageTk
import os

counter = 1
def rotate_img():
    global counter
    img_label.config(image=img_arr[counter%len(img_arr)])
    counter += 1

root = tk.Tk()
root.title("Wallpaper Viewer")
root.geometry("250x400")
root.configure(background="black")

files = os.listdir('Wallpaper')

img_arr = []
for file in files:
    img = Image.open(os.path.join('Wallpaper',file))
    resized_img = img.resize((200,300))
    img_arr.append(ImageTk.PhotoImage(resized_img))

img_label = tk.Label(root, image=img_arr[0])
img_label.pack(pady=(15,10))

next_button = tk.Button(root, text='Next', fg='black', bg='white', width=28, height=2, command=rotate_img)
next_button.pack()
root.mainloop()