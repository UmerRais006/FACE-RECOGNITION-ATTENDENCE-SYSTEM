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
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # ______variables_______
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        #__________________________________________________

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


        title_lbl=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",20,"bold"), fg="#000066")
        title_lbl.place(x=-100,y=120,width=1530,height=25)
        #MAIN FRAME:
        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=0,y=150,width=1300,height=660)

        #------------------------------------------------------------------------------------------------------------------
        #left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=620,height=470)
        
        #COURSE INFO
        Current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=5,y=10,width=600,height=130)

        #department choose
        dep_label=Label(Current_course_frame,text="Department :",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=5,sticky=W)

        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12),width=17,state="read only")
        dep_combo['values']=("Select Department","Computer","Mechanical","IT","Civil","Robotics") #tuple
        dep_combo.current(0)#indexing so 0 per select dep  first per hoga
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)#padding

        #COURSE CHOOSE
        Course_label=Label(Current_course_frame,text="Course :",font=("times new roman",12,"bold"))
        Course_label.grid(row=0,column=2,padx=5,sticky=W)

        Course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12),width=17,state="read only")
        Course_combo['values']=("Course","BSCS","SE","IT","BS PHYSICS","Robotics") #tuple
        Course_combo.current(0)#indexing so 0 per select Course  first per hoga
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)#padding

        # CHOOSE YEAR
        Year_label=Label(Current_course_frame,text="  Year :",font=("times new roman",12,"bold"))
        Year_label.grid(row=1,column=0,sticky=W)

        Year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12),width=17,state="read only")
        Year_combo['values']=("Year","2020","2021","2022","2023","2024","2025") #tuple
        Year_combo.current(0) #indexing so 0 per select Year  first per hoga
        Year_combo.grid(row=1,column=1,sticky=W)#padding

        #CHOOSE SEMESTER
        Semester_label=Label(Current_course_frame,text="Semester :",font=("times new roman",12,"bold"))
        Semester_label.grid(row=1,column=2,padx=5,sticky=W)

        Semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12),width=17,state="read only")
        Semester_combo['values']=("Semester","1st","2nd","3rd","4rt","5th","6th","7th","8th") #tuple
        Semester_combo.current(0)#indexing so 0 per select Semester  first per hoga
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)#padding

         #class student info 
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=150,width=600,height=295)
         #________________ENTRIES________________
        studentid_label=Label(class_student_frame,text="Student id :",font=("times new roman",12,"bold"))
        studentid_label.grid(row=0,column=0,padx=5,sticky=W)

        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=15,font=("times new roman",12))
        studentid_entry.grid(row=0,column=1,padx=5,sticky=W,pady=5)

        CLASSdivision_label=Label(class_student_frame,text="Class Divison :",font=("times new roman",12,"bold"))
        CLASSdivision_label.grid(row=1,column=0,padx=5,sticky=W)

       # CLASSdivision_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=15,font=("times new roman",12))
       #CLASSdivision_entry.grid(row=1,column=1,padx=5,sticky=W,pady=5)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12),width=13,state="read only")
        div_combo['values']=("A","B","C") #tuple
        div_combo.current(0)#indexing so 0 per select Semester  first per hoga
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)#padding

        gender_label=Label(class_student_frame,text="Gender :",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=5,sticky=W)

      #  gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=15,font=("times new roman",12))
      #  gender_entry.grid(row=2,column=1,padx=5,sticky=W,pady=5)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12),width=13,state="read only")
        gender_combo['values']=("Male","Female","Other") #tuple
        gender_combo.current(0)#indexing so 0 per select Semester  first per hoga
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)#padding

        email_label=Label(class_student_frame,text="Email :",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",12))
        email_entry.grid(row=3,column=1,padx=5,sticky=W,pady=5)

        Address_label=Label(class_student_frame,text="Address :",font=("times new roman",12,"bold"))
        Address_label.grid(row=4,column=0,padx=5,sticky=W)

        Address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",12))
        Address_entry.grid(row=4,column=1,padx=5,sticky=W,pady=5)

        Student_Name_label=Label(class_student_frame,text="Student Name :",font=("times new roman",12,"bold"))
        Student_Name_label.grid(row=0,column=2,padx=20,sticky=W)

        Student_Name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",12))
        Student_Name_entry.grid(row=0,column=3,padx=5,sticky=W,pady=5)


        RollNo_label=Label(class_student_frame,text="Roll No :",font=("times new roman",12,"bold"))
        RollNo_label.grid(row=1,column=2,padx=20,sticky=W)

        RollNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=15,font=("times new roman",12))
        RollNo_entry.grid(row=1,column=3,padx=5,sticky=W,pady=5)

        DOB_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"))
        DOB_label.grid(row=2,column=2,padx=20,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=15,font=("times new roman",12))
        DOB_entry.grid(row=2,column=3,padx=5,sticky=W,pady=5)


        Phone_no_label=Label(class_student_frame,text="Phone No :",font=("times new roman",12,"bold"))
        Phone_no_label.grid(row=3,column=2,padx=20,sticky=W)

        Phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=15,font=("times new roman",12))
        Phone_no_entry.grid(row=3,column=3,padx=5,sticky=W,pady=5)

        Teacher_name_label=Label(class_student_frame,text="Teacher Name :",font=("times new roman",12,"bold"))
        Teacher_name_label.grid(row=4,column=2,padx=20,sticky=W)

        Teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",12))
        Teacher_name_entry.grid(row=4,column=3,padx=5,sticky=W,pady=5)

        #radio Button
        self.var_radio1=StringVar()
        radioButton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value='YES')
        radioButton1.grid(row=5,column=0, padx=10)

        radioButton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value='NO')
        radioButton2.grid(row=5,column=1, padx=10)


        #buttton frame
        btn_frame=Frame(class_student_frame,relief=RIDGE)
        btn_frame.place(x=5,y=200,width=585,height=88)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",12,"bold"),width=13,bg="#000066",fg="white")
        save_btn.grid(row=0,column=0,padx=8)

        Update_btn=Button(btn_frame,text="Update",command=self.updateData,font=("times new roman",12,"bold"),width=13,bg="#000066",fg="white")
        Update_btn.grid(row=0,column=1,padx=6)

        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),width=13,bg="#000066",fg="white")
        Delete_btn.grid(row=0,column=2,padx=6)

        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),width=13,bg="#000066",fg="white")
        Reset_btn.grid(row=0,column=3,padx=6)

        Take_Photo_btn=Button(btn_frame,text="Take Photo",command=self.generate_dataset,font=("times new roman",12,"bold"),width=13,bg="#000066",fg="white")
        Take_Photo_btn.grid(row=1,column=0,pady=10,padx=10)
        Update_Photo_btn=Button(btn_frame,text="Update Photo",font=("times new roman",12,"bold"),width=13,bg="#000066",fg="white")
        Update_Photo_btn.grid(row=1,column=1,pady=10)

        #------------------------------------------------------------------------------------------------------------------
        #RIGHT lable frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        right_frame.place(x=640,y=10,width=620,height=470)

        #SEARCH SYSTEM
        search_system_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        search_system_frame.place(x=5,y=20,width=600,height=70)

        Search_label=Label(search_system_frame,text="Search by :",font=("times new roman",12,"bold"))
        Search_label.grid(row=0,column=0,padx=20,sticky=W)

        Search_combo=ttk.Combobox(search_system_frame,font=("times new roman",12),width=15,state="read only")
        Search_combo['values']=("Select","Roll No","Phone No") #tuple
        Search_combo.current(0)#indexing so 0 per select Search  first per hoga
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)#padding

        Search_entry=ttk.Entry(search_system_frame,width=10,font=("times new roman",12))
        Search_entry.grid(row=0,column=2,padx=5,sticky=W,pady=5)

        Search_btn=Button(search_system_frame,text="Search ",font=("times new roman",10,"bold"),width=13,bg="#000066",fg="white")
        Search_btn.grid(row=0,column=3,padx=6)

        Show_all_btn=Button(search_system_frame,text="Show All",font=("times new roman",10,"bold"),width=13,bg="#000066",fg="white")
        Show_all_btn.grid(row=0,column=4,padx=6)
        
        #table frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=100,width=600,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=('Department','Course','year','semester','id','name','div','roll','gender','dob','phone','Address','teacher','Photos'),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("Photos", text="Photos")
        self.student_table["show"]='headings'
        
        #only setting width
        self.student_table.column("Department", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("Photos", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data() # to show data in table
   #-------------------FUNCTIONS----------------------------------
    def add_data(self):
         if self.var_dep.get()=="Select Department" or self.var_std_name.get()=='' or self.var_std_id.get()=='':
             messagebox.showerror("ERROR","ALL FIELDS REQUIRED",parent=self.root)
         else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="newpasswordnew",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                  
                                                        self.var_dep.get(),
                                                        self.var_course.get(),
                                                        self.var_year.get(),
                                                        self.var_semester.get(),
                                                        self.var_std_id.get(),
                                                        self.var_std_name.get(),
                                                        self.var_div.get(),
                                                        self.var_roll.get(),
                                                        self.var_gender.get(),
                                                        self.var_dob.get(),
                                                        self.var_email.get(),
                                                        self.var_phone.get(),
                                                        self.var_address.get(),
                                                        self.var_teacher.get(),
                                                        self.var_radio1.get()

                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS", "DETAILS HAVE BEEN ADDED",parent=self.root)
            except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)

              
     #--------------------FETCH DATA________________  
    def fetch_data(self):
         conn=pymysql.connect(host="localhost",user="root",password="newpasswordnew",database="face_recognizer")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall() #all data in data variable

         if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)

            conn.commit()
            conn.close()
#   __________GET CURSOR______________
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()#cursor wala data store krega in variavle
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # _____UPDATE FUNCTION__________
    def updateData(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=='' or self.var_std_id.get()=='':
           messagebox.showerror("ERROR","ALL FIELDS REQUIRED",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("UPDATE","Do you want to update this student details",parent=self.root)
                if Update>0:
                     conn=pymysql.connect(host="localhost",user="root",password="newpasswordnew",database="face_recognizer")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                                                       self.var_dep.get(),
                                                        self.var_course.get(),
                                                        self.var_year.get(),
                                                        self.var_semester.get(),
                                                        self.var_std_name.get(),
                                                        self.var_div.get(),
                                                        self.var_roll.get(),
                                                        self.var_gender.get(),
                                                        self.var_dob.get(),
                                                        self.var_email.get(),
                                                        self.var_phone.get(),
                                                        self.var_address.get(),
                                                        self.var_teacher.get(),
                                                        self.var_radio1.get(),
                                                        self.var_std_id.get()



                     ))
                else:
                    if not Update:
                          return
                messagebox.showinfo("UPDATED","STUDENT DETAILS UPDATED",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
               messagebox.showerror("ERROR", f"Due To: {str(es)}", parent=self.root)
   # _______delete function----------
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("ERROR","STUDENT ID REQUIRED",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("DELETETION","DO YOU WANT TO DELETE STUDENT",parent=self.root)
                if delete>0:
                     conn=pymysql.connect(host="localhost",user="root",password="newpasswordnew",database="face_recognizer")
                     my_cursor=conn.cursor()
                     sql="delete from student where Student_id=%s"
                     val=(self.var_std_id.get(),)
                     my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
               messagebox.showerror("ERROR", f"Due To: {str(es)}", parent=self.root)   

   #     --------------RESET FUNCTION_______________       
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#----------------- geneerate data set take phto sample--------------------
    def generate_dataset(self):
           if self.var_dep.get()=="Select Department" or self.var_std_name.get()=='' or self.var_std_id.get()=='':
                messagebox.showerror("ERROR","ALL FIELDS REQUIRED",parent=self.root)
           else:
               try:
                     conn=pymysql.connect(host="localhost",user="root",password="newpasswordnew",database="face_recognizer")
                     my_cursor=conn.cursor()
                     my_cursor.execute("select * from student")
                     myresult=my_cursor.fetchall()
                     id=0
                     for x in myresult:
                         id+=1
                     my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                                                       self.var_dep.get(),
                                                        self.var_course.get(),
                                                        self.var_year.get(),
                                                        self.var_semester.get(),
                                                        self.var_std_name.get(),
                                                        self.var_div.get(),
                                                        self.var_roll.get(),
                                                        self.var_gender.get(),
                                                        self.var_dob.get(),
                                                        self.var_email.get(),
                                                        self.var_phone.get(),
                                                        self.var_address.get(),
                                                        self.var_teacher.get(),
                                                        self.var_radio1.get(),
                                                        int(self.var_std_id.get()) == (int(id) + 1)




                     ))
                     conn.commit()
                     self.fetch_data()
                     self.reset_data()
                     conn.close()

                    # ============LOAD PREDEFINFE DATA FRONTAL FACE==============
                    #variable me store kia file path
                     face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                     def face_cropped(img):
                         #we have to convert simple inmages to greyscale
                         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                         faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3
                         #minimum neighbour=5
                         for (x,y,w,h) in faces:
                             face_cropped=img[y:y+h,x:x+w]
                             return face_cropped
                     cap=cv2.VideoCapture(0)# opening camera
                     img_id=0
                     while True: #infinite loop
                         ret,my_frame=cap.read()
                         if face_cropped(my_frame) is not None:
                             img_id+=1
                             face=cv2.resize(face_cropped(my_frame),(450,450))
                             face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                             # Corrected path to save images
                             data_folder_path = r"C:\Users\Hp\Documents\TPL PROJECT\face recog\data"
                             file_name_path = f"{data_folder_path}\\user.{str(id)}.{str(img_id)}.jpg"
                             cv2.imwrite(file_name_path, face)  # Save the image
                             cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                             cv2.imshow("Cropped Face",face)

                         if cv2.waitKey(1)==13 or int(img_id)==100:#13=emter close ya 100 hojyein
                            break

                     cap.release()#camera off
                     cv2.destroyAllWindows()
                     messagebox.showinfo("Result","Generating dataset completed",parent=self.root)
               except Exception as es:
                  messagebox.showerror("ERROR", f"Due To: {str(es)}", parent=self.root)   
     
  


if __name__== "__main__":
    root=Tk() #calling root with tool kit
    obj=student(root)
    root.mainloop()

