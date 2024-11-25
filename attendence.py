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

        

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE)
        left_inside_frame.place(x=0,y=50,width=600,height=360)
        #ATTENDENCE ID
        AttendenceID_label=Label(left_inside_frame,text="Attendence ID :",font=("times new roman",12,"bold"))
        AttendenceID_label.grid(row=0,column=0,padx=20,pady=8,sticky=W)

        AttendenceID_entry=ttk.Entry(left_inside_frame,width=15,font=("times new roman",12))
        AttendenceID_entry.grid(row=0,column=1,padx=5,sticky=W,pady=8)
        #ROLL
        Roll_label=Label(left_inside_frame,text="Roll :",font=("times new roman",12,"bold"))
        Roll_label.grid(row=0,column=2,padx=20,pady=8,sticky=W)

        Roll_entry=ttk.Entry(left_inside_frame,width=15,font=("times new roman",12))
        Roll_entry.grid(row=0,column=3,sticky=W,pady=8)



        #NAME
        Name_label=Label(left_inside_frame,text="Name :",font=("times new roman",12,"bold"))
        Name_label.grid(row=1,column=0,padx=20,pady=8,sticky=W)

        Name_entry=ttk.Entry(left_inside_frame,width=15,font=("times new roman",12))
        Name_entry.grid(row=1,column=1,padx=5,sticky=W,pady=8)
        #DEp
        Department_label=Label(left_inside_frame,text="Department :",font=("times new roman",12,"bold"))
        Department_label.grid(row=1,column=2,padx=20,pady=8,sticky=W)

        Department_entry=ttk.Entry(left_inside_frame,width=15,font=("times new roman",12))
        Department_entry.grid(row=1,column=3,padx=5,sticky=W,pady=8)
        


        #TIME
        Time_label=Label(left_inside_frame,text="Time :",font=("times new roman",12,"bold"))
        Time_label.grid(row=2,column=0,padx=20,pady=8,sticky=W)

        Time_entry=ttk.Entry(left_inside_frame,width=15,font=("times new roman",12))
        Time_entry.grid(row=2,column=1,padx=5,sticky=W,pady=8)
        #DATE
        Date_label=Label(left_inside_frame,text="Date :",font=("times new roman",12,"bold"))
        Date_label.grid(row=2,column=2,padx=20,pady=8,sticky=W)

        Date_entry=ttk.Entry(left_inside_frame,width=15,font=("times new roman",12))
        Date_entry.grid(row=2,column=3,padx=5,sticky=W,pady=8)

        #combo box
        Attendence_label=Label(left_inside_frame,text="Attendence Status :",font=("times new roman",12,"bold"))
        Attendence_label.grid(row=3,column=0,padx=20,sticky=W)

        Attendence_combo=ttk.Combobox(left_inside_frame,font=("times new roman",12),width=15,state="read only")
        Attendence_combo['values']=("Status","Present","Absent") #tuple
        Attendence_combo.current(0)#indexing so 0 per select Attendence  first per hoga
        Attendence_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)#padding



            #buttton frame
        btn_frame=Frame(left_inside_frame,relief=RIDGE)
        btn_frame.place(x=5,y=300,width=585,height=50)

        Import_btn=Button(btn_frame,text="Import csv",font=("times new roman",12,"bold"),width=13,bg="#000066",fg="white")
        Import_btn.grid(row=0,column=0,padx=8)

        Export_btn=Button(btn_frame,text="Export csv",font=("times new roman",12,"bold"),width=13,bg="#000066",fg="white")
        Export_btn.grid(row=0,column=1,padx=6)

        Update_btn=Button(btn_frame,text="Update",font=("times new roman",12,"bold"),width=13,bg="#000066",fg="white")
        Update_btn.grid(row=0,column=2,padx=6)

        Reset_btn=Button(btn_frame,text="Reset",font=("times new roman",12,"bold"),width=13,bg="#000066",fg="white")
        Reset_btn.grid(row=0,column=3,padx=6)
        

        #RIGHT lable frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendence System",font=("times new roman",12,"bold"))
        right_frame.place(x=640,y=10,width=620,height=470)

        table_frame=Frame(right_frame,relief=RIDGE,bd=2)
        table_frame.place(x=5,y=5,width=600,height=400)

#_____________SCROLL BAR________________
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.AttendenceReportTable = ttk.Treeview(
        table_frame,
        columns=("id", "roll", "name", "department", "time", "date", "attendence"),  # Fixed columns list
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attemdence")
        self.AttendenceReportTable["show"]="headings"

        self.AttendenceReportTable.column("id", width=100)
        self.AttendenceReportTable.column("roll", width=100)
        self.AttendenceReportTable.column("name", width=100)
        self.AttendenceReportTable.column("department", width=100)
        self.AttendenceReportTable.column("time", width=100)
        self.AttendenceReportTable.column("date", width=100)
        self.AttendenceReportTable.column("attendence", width=100)
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        
        #dd
if __name__== "__main__":
    root=Tk() #calling root with tool kit
    obj=student(root)
    root.mainloop()

