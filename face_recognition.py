from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import os
import cv2
import numpy as np
from time import strftime #for getting time
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        img1 = Image.open(r"college_images\faceR2.jpg")
        img1 = img1.resize((screen_width, screen_height), Image.Resampling.LANCZOS)  # Resize dynamically
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=screen_width, height=screen_height)  

        title_lbl = Label(
            self.root,
            text="FACE RECOGNITION",
            font=("times new roman", 30, "bold"),
            bg="#2B2B2B",  
            fg="#FFFFFF",  
            padx=10,  
            pady=10,
        )
        title_lbl.place(x=0, y=0, relwidth=1, height=50)

        b1_1 = Button(
            self.root,
            text="TRAIN DATA",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="#2B2B2B",  
            fg="#FFFFFF",  
            padx=20,  
            pady=5,
            command=self.face_recog
        )
        b1_1.place(relx=0.33, rely=0.60 , anchor="w", width=180, height=50) 

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = pymysql.connect(host="localhost", user="root", password="newpasswordnew", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Roll: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)   
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            return img

        def recognize(img, clf, faceCascade):
            return draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
#EE
        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture image")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()



#_________________ATTENDENCE MARKING____________________
    def mark_attendence(Self,i,r,n,d):
        with open("excelSheet.csv","r+",newline='\n') as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) #umer,005,cs
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n not in name_list)and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")








if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
