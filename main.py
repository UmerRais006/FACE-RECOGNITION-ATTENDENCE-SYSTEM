from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("SUPERIOR ATTENDENCE SYSTEM")
        
        img=Image.open(r"C:\Users\Hp\Documents\TPL PROJECT\face recog\college_images\Superior-University.png")
        img=img.resize((500,110))
        self.photoimg=ImageTk.PhotoImage(img)
        
        self.root.update()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        # getting centre of x axis
        x = (window_width - 500) // 2  #centre horizintal

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=x,y=0,width=500,height=130)

        title_lbl=Label(self.root,text="SUPERIOR ATTENDENCE SYSTEM",font=("times new roman",25,"bold"), fg="#000066")
        title_lbl.place(x=-100,y=140,width=1530,height=45)
         
       #student dtetails 
       #1

        img2=Image.open(r"C:\Users\Hp\Documents\TPL PROJECT\face recog\college_images\student.png")
        img2=img2.resize((180,180))
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(self.root,image=self.photoimg2,cursor="hand2")
        b1.place(x=200,y=200,width=180,height=180)
        b1_1 = Button(self.root, text="STUDENT DETAILS", cursor="hand2", font=("times new roman", 12, "bold"), bg="white", fg="#000066")
        b1_1.place(x=200,y=355,width=180,height=40)
    

        #face recognition
        #2
        img3=Image.open(r"C:\Users\Hp\Documents\TPL PROJECT\face recog\college_images\facerecognition.webp")
        img3=img3.resize((180,180))
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(self.root,image=self.photoimg3,cursor="hand2")
        b1.place(x=440,y=200,width=180,height=180)
        b1_1 = Button(self.root, text="FACE DETECTOR", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="#000066")
        b1_1.place(x=440,y=355,width=180,height=40)

        #ATTENDENCE
        #3
        img4=Image.open(r"C:\Users\Hp\Documents\TPL PROJECT\face recog\college_images\attendence.webp")
        img4=img4.resize((180,180))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(self.root,image=self.photoimg4,cursor="hand2")
        b1.place(x=680,y=200,width=180,height=180)
        b1_1 = Button(self.root, text="ATTENDENCE", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="#000066")
        b1_1.place(x=680,y=355,width=180,height=40)

        #CONTACT US
        #4
        img5=Image.open(r"C:\Users\Hp\Documents\TPL PROJECT\face recog\college_images\help.webp")
        img5=img5.resize((180,180))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(self.root,image=self.photoimg5,cursor="hand2")
        b1.place(x=920,y=200,width=180,height=180)
        b1_1 = Button(self.root, text="HELP", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="#000066")
        b1_1.place(x=920,y=355,width=180,height=40)

       #---------------------------------------------------------------------------------------------------------------------------------------------------------
       #TRAIN DATA
       #5
        img6=Image.open(r"C:\Users\Hp\Documents\TPL PROJECT\face recog\college_images\traindata.jpg")
        img6=img6.resize((180,180))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(self.root,image=self.photoimg6,cursor="hand2")
        b1.place(x=200,y=410,width=180,height=180)
        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2", font=("times new roman", 12, "bold"), bg="white", fg="#000066")
        b1_1.place(x=200,y=570,width=180,height=40)

       #PHOTOS
       #6
        img7=Image.open(r"C:\Users\Hp\Documents\TPL PROJECT\face recog\college_images\photos.jpg")
        img7=img7.resize((180,180))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(self.root,image=self.photoimg7,cursor="hand2")
        b1.place(x=440,y=410,width=180,height=180)
        b1_1 = Button(self.root, text="PHOTOS", cursor="hand2", font=("times new roman", 12, "bold"), bg="white", fg="#000066")
        b1_1.place(x=440,y=570,width=180,height=40)

       #DEVELOPER
       #7
        img8=Image.open(r"C:\Users\Hp\Documents\TPL PROJECT\face recog\college_images\developers.jpg")
        img8=img8.resize((180,180))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(self.root,image=self.photoimg8,cursor="hand2")
        b1.place(x=680,y=410,width=180,height=180)
        b1_1 = Button(self.root, text="DEVELOPERS", cursor="hand2", font=("times new roman", 12, "bold"), bg="white", fg="#000066")
        b1_1.place(x=680,y=570,width=180,height=40)

        
       #EXIT
       #8
        img9=Image.open(r"C:\Users\Hp\Documents\TPL PROJECT\face recog\college_images\exit.png")
        img9=img9.resize((180,180))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(self.root,image=self.photoimg9,cursor="hand2")
        b1.place(x=920,y=410,width=180,height=180)
        b1_1 = Button(self.root, text="EXIT", cursor="hand2", font=("times new roman", 12, "bold"), bg="white", fg="#000066")
        b1_1.place(x=920,y=570,width=180,height=40)
    
    


if __name__== "__main__":
    root=Tk() #calling root with tool kit
    obj=Face_Recognition_System(root)
    root.mainloop()
