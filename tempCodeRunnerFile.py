from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import os
import cv2


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # Load and set the full background image
        img1 = Image.open(r"college_images\background.jpg")  # Update to your correct file path
        img1 = img1.resize((1400, 790))  # Resize to fit the window
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Create a Label to display the background image
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1400, height=790)

        # Title Label overlay on the background
        title_lbl = Label(
            self.root,
            text="TRAIN DATA SET",
            font=("times new roman", 30, "bold"),
            bg="#F5F5DC",  # Light beige background for the title
            fg="#000066"
        )
        title_lbl.place(relx=0.5, y=50, anchor="center")

        # Button overlay on the background
        b1_1 = Button(
            self.root,
            text="TRAIN DATA",
            cursor="hand2",
            font=("times new roman", 12, "bold"),
            bg="#F5F5DC",
            fg="#000066"
        )
        b1_1.place(relx=0.5, y=200, anchor="center", width=180, height=40)


# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
