from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import os #for getting images
import cv2 #more than 2500+ algorithms
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # Get the screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        
        img1 = Image.open(r"college_images\traindatainner2.jpg")
        img1 = img1.resize((screen_width, screen_height), Image.Resampling.LANCZOS)  # Resize dynamically
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Create a Label to display the background image
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=screen_width, height=screen_height)  

        # Title Label overlay on the background
         
        title_lbl = Label(
            self.root,
            text="TRAIN DATA SET",
            font=("times new roman", 30, "bold"),
            bg="#2B2B2B",  # Background color to match the image's darker tone
            fg="#FFFFFF",  # White text color for contrast
            padx=10,  # Add some padding for better appearance
            pady=10
        )
        title_lbl.place(relx=0.02, rely=0.4, anchor="w")  # Centered vertically on the left

        # Button overlay on the background
        b1_1 = Button(
            self.root,
            text="TRAIN DATA",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="#2B2B2B",  # Matching the background color
            fg="#FFFFFF",  # White text for better contrast
            command=self.train_classifier,
            padx=20,  # Button padding
            pady=5
        )
        b1_1.place(relx=0.08, rely=0.5, anchor="w", width=180, height=50)  # Centered below the title

    def train_classifier(self):
          data_dir=("data") #alll data move to data dir
          path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] #all data move to path
          faces=[]
          ids=[]
          for image in path:
               img=Image.open(image).convert("L")#gray scale image conversion
               imageNp=np.array(img,'uint8') #dataype
               id=int(os.path.split(image)[1].split('.')[1])

               faces.append(imageNp)
               ids.append(id)
               cv2.imshow("Training",imageNp)
               cv2.waitKey(1)==13

          ids=np.array(id)#id converting to numpy #88% fast performance
         # _____________train the classifier--------------
          clf=cv2.face.LBPHFaceRecognizer_create()
          clf.train(faces,ids)
          clf.write("classifier.xml")
          cv2.destroyAllWindows()
          messagebox.showinfo("Result","Completed")

          
# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
