import tkinter as tk
from tkinter import messagebox

class BirthdayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Birthday Greeting")
        self.root.geometry("500x400")
        self.root.configure(bg="#f7c6c7")
        
        # Step 1: Initial Greeting Card with Ribbon
        self.card_frame = tk.Frame(self.root, bg="#f7c6c7")
        self.ribbon_button = tk.Button(self.card_frame, text="🎁 Click to Open", font=("Arial", 16), bg="red", fg="white",
                                       command=self.open_card, width=15, height=2)
        self.ribbon_button.pack(pady=100)
        self.card_frame.pack(fill="both", expand=True)

        # Step 2: Greeting Page
        self.greeting_frame = tk.Frame(self.root, bg="#f7c6c7")
        self.greeting_label = tk.Label(self.greeting_frame, text="🎉 Happy Birthday!", font=("Arial", 24), bg="#f7c6c7", fg="purple")
        self.greeting_label.pack(pady=20)
        self.photo_label = tk.Label(self.greeting_frame, text="👤 [Photo Here]", font=("Arial", 16), bg="#f7c6c7", fg="black")
        self.photo_label.pack(pady=10)
        self.next_button1 = tk.Button(self.greeting_frame, text="Next", command=lambda: self.show_page("text"), font=("Arial", 14), bg="#4CAF50", fg="white")
        self.next_button1.pack(pady=20)

        # Step 3: Greeting Text Page
        self.text_frame = tk.Frame(self.root, bg="#f7c6c7")
        self.text_label = tk.Label(self.text_frame, text="Wishing you an amazing day filled with joy, laughter, and unforgettable memories! 🎂 🎈",
                                   wraplength=400, font=("Arial", 14), bg="#f7c6c7", fg="black")
        self.text_label.pack(pady=50)
        self.next_button2 = tk.Button(self.text_frame, text="Next", command=lambda: self.show_page("photos"), font=("Arial", 14), bg="#4CAF50", fg="white")
        self.next_button2.pack(pady=20)

        # Step 4: Photos Page
        self.photos_frame = tk.Frame(self.root, bg="#f7c6c7")
        self.photos_label = tk.Label(self.photos_frame, text="Memories", font=("Arial", 24), bg="#f7c6c7", fg="purple")
        self.photos_label.pack(pady=20)
        
        # Creating a grid of placeholder photo slots
        for i in range(2):
            for j in range(5):
                photo_slot = tk.Label(self.photos_frame, text="🖼️", font=("Arial", 16), bg="lightgray", width=8, height=4)
                photo_slot.grid(row=i, column=j, padx=5, pady=5)

    def open_card(self):
        self.card_frame.pack_forget()  # Hide the card frame
        self.greeting_frame.pack(fill="both", expand=True)  # Show the greeting frame

    def show_page(self, page):
        # Hide all frames
        self.greeting_frame.pack_forget()
        self.text_frame.pack_forget()
        self.photos_frame.pack_forget()
        
        # Show the selected frame
        if page == "text":
            self.text_frame.pack(fill="both", expand=True)
        elif page == "photos":
            self.photos_frame.pack(fill="both", expand=True)

# Create the main window and run the app
root = tk.Tk()
app = BirthdayApp(root)
root.mainloop()
