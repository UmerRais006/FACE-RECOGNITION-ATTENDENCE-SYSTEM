from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import os #for getting images
import cv2 #more than 2500+ algorithms



class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("Face Recognition")


        title_lbl=Label(self.root,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",20,"bold"), fg="#000066")
        title_lbl.place(x=-100,y=100,width=1530,height=40)
        #MAIN FRAME:
        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=0,y=220,width=1300,height=660)

         #MAIN FRAME:
        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=0,y=150,width=1300,height=660)

        #------------------------------------------------------------------------------------------------------------------
        #left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=620,height=470)

         #RIGHT lable frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendence System",font=("times new roman",12,"bold"))
        right_frame.place(x=640,y=10,width=620,height=470)
        







if __name__== "__main__":
    root=Tk() #calling root with tool kit
    obj=student(root)
    root.mainloop()

