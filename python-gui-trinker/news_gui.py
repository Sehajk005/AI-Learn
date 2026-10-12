import tkinter as tk
from io import BytesIO
import webbrowser
import requests
from urllib.request import urlopen
from PIL import Image, ImageTk



class NewsApp:

    def __init__(self):

        # Load Data
        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=99d79382daac4583ace0594061ba609e").json()
        # Initial GUI Load
        self.load_gui()
        # Load 1st News
        self.load_news(0)

    def load_gui(self):
        self.root = tk.Tk()
        self.root.title("News Letter")
        self.root.geometry("350x600")
        self.root.resizable(0,0)
        self.root.configure(background="black")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news(self, index):

        # clear
        self.clear()

        # Image

        try:
            img_url = self.data['articles'][index].get('urlToImage')

            if not img_url:
                raise ValueError("No image URL available")

            response = requests.get(
                img_url,
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=10
            )
            response.raise_for_status()

            im = Image.open(BytesIO(response.content)).convert("RGB")
            im = im.resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        except (requests.RequestException, ValueError, OSError) as e:
            print("Image loading failed:", e)

            # Display a placeholder instead of making another failing network request
            im = Image.new("RGB", (350, 250), color="black")
            photo = ImageTk.PhotoImage(im)


        label = tk.Label(self.root, image=photo)
        label.pack()

        heading = tk.Label(self.root, text=self.data['articles'][index]['title'], bg="black", fg="white",
                           wraplength=350, justify="center")
        heading.pack(pady=(10, 20))
        heading.config(font=("verdana", 15))

        details = tk.Label(self.root, text=self.data['articles'][index]['description'], bg="black", fg="white",
                           wraplength=350, justify="center")
        details.pack(pady=(2, 20))
        details.config(font=("verdana", 12))

        frame = tk.Frame(self.root, bg="black")
        frame.pack(expand=True, fill="both")

        if index != 0:
            prev = tk.Button(frame, text="Prev", width=16, height=3, command=lambda: self.load_news(index - 1))
            prev.pack(side="left")

        read = tk.Button(frame, text="Read More", width=16, height=3, command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side="left")

        if index != len(self.data['articles']) - 1:
            next = tk.Button(frame, text="Next", width=16, height=3, command=lambda: self.load_news(index + 1))
            next.pack(side="left")


        self.root.mainloop()

    def open_link(self, url):
        webbrowser.open_new_tab(url)


obj = NewsApp()

