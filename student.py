from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk,ImageSequence
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import re


class Student:  # Create class
    def __init__(self, root):  # Constructor
        self.root = root    # Initialize
        self.root.geometry("1536x864+-10+0")  # Window size
        self.root.title("face recognition system")


        #================variables=========
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



        # # first image
        img = Image.open("college_images/second_image.jpeg")
        img = img.resize((510, 130), Image.LANCZOS)  # resize syntax
        self.photoimg = ImageTk.PhotoImage(img)

        # # Display image
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=510, height=130)  


        # # second image
        img1 = Image.open("college_images/first_image.jpeg")
        img1 = img1.resize((510, 130), Image.LANCZOS)  # resize syntax
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # # Display image
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=510, y=0, width=510, height=130)



        # # third image
        img2 = Image.open("college_images/third_image.jpeg")
        img2 = img2.resize((510, 130), Image.LANCZOS)  # resize syntax
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # # Display image
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1020, y=0, width=510, height=130)  





        # # Background image
        img3 = Image.open("college_images/bg_image.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)  # resize syntax
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # # Display image
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGMENT SYSTEM",font=("montserrat",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=20,y=50, width=1480,height=600)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("montserrat",12,"bold") )
        Left_frame.place(x=10,y=10,width = 730,height = 580)

        img_left = Image.open("college_images/third_image.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)  # resize syntax
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        # # Display image
        # f_lbl = Label(Left_frame, image=self.photoimg_left)
        # f_lbl.place(x=5, y=0, width=720, height=130)

        # current course information
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("montserrat",12,"bold") )
        current_course_frame.place(x=5,y=5,width = 720,height = 150)


        # Department
        dep_label= Label(current_course_frame,text="Department",font=("montserrat",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("montserrat",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CS","IT","ECE","EI","EE","Mech","Civil","IP")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        dep_label= Label(current_course_frame,text="Course",font=("montserrat",12,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("montserrat",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Course","BTech","MTech","MCA")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        dep_label= Label(current_course_frame,text="Year",font=("montserrat",12,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("montserrat",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Year","2021","2022","2023","2024","2025")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        dep_label= Label(current_course_frame,text="Semester",font=("montserrat",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester ,font=("montserrat",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Semester","Semester-1","Semester-2")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        
        # current student information
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Student Information",font=("montserrat",12,"bold") )
        class_student_frame.place(x=5,y=130,width = 720,height = 400)


        # student ID
        studentID_label= Label(class_student_frame,text="StudentID : ",font=("montserrat",13,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id  ,width=20,font=("montserrat",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student Name
        studentName_label = Label(class_student_frame, text="Student Name : ", font=("montserrat", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name  , width=20, font=("montserrat", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_student_frame, text="Class Division : ", font=("montserrat", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # class_div_entry = ttk.Entry(class_student_frame,textvariable=self.var_div  , width=20, font=("montserrat", 13, "bold"))
        # class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("montserrat",12,"bold"),width=17,state="readonly")
        div_combo["values"]=("A","B")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # Roll No
        roll_no_label = Label(class_student_frame, text="Roll No :", font=("montserrat", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll  ,width=20, font=("montserrat", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender :", font=("montserrat", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        # gender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender , width=20, font=("montserrat", 13, "bold"))
        # gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("montserrat",12,"bold"),width=17,state="readonly")
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DOB
        dob_label = Label(class_student_frame, text="DOB :", font=("montserrat", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob ,width=20, font=("montserrat", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email :", font=("montserrat", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email  ,width=20, font=("montserrat", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        phone_label = Label(class_student_frame, text="Phone No :", font=("montserrat", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone  , width=20, font=("montserrat", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address :", font=("montserrat", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address  ,width=20, font=("montserrat", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher 
        teacher_label = Label(class_student_frame, text="Teacher Name :", font=("montserrat", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher  ,width=20, font=("montserrat", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons

        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=284, width=715, height=35)

        # Save Button
        save_btn = Button(btn_frame, text="Save",command=self.add_data,width=17, font=("montserrat", 13, "bold"), bg="lightskyblue", fg="black")
        save_btn.grid(row=0, column=0)

        # Update Button
        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=17, font=("montserrat", 13, "bold"), bg="lightskyblue", fg="black")
        update_btn.grid(row=0, column=1)

        # Delete Button
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=("montserrat", 13, "bold"), bg="lightskyblue", fg="black")
        delete_btn.grid(row=0, column=2)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("montserrat", 13, "bold"), bg="lightskyblue", fg="black")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=330, width=715, height=35)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset,text="Take Photo Sample", width=35, font=("montserrat", 13, "bold"), bg="lightskyblue", fg="black")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=("montserrat", 13, "bold"), bg="lightskyblue", fg="black")
        update_photo_btn.grid(row=0, column=1)




        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("montserrat",12,"bold") )
        Right_frame.place(x=750,y=10,width = 720,height = 580)

        # img_right = Image.open("C:/Users/ASUS/OneDrive/Desktop/face_recognition system/college_images/third_image.jpeg")
        # img_right = img_right.resize((720, 130), Image.LANCZOS)  # resize syntax
        # self.photoimg_right = ImageTk.PhotoImage(img_right)

        # # # Display image
        # f_lbl = Label(Right_frame, image=self.photoimg_right)
        # f_lbl.place(x=5, y=0, width=720, height=130)
        

        # Right Frame for Video
        self.video_frame = Frame(Right_frame, width=720, height=130)
        self.video_frame.pack()

        # Video Label
        self.label = Label(self.video_frame)
        self.label.pack()

        # Load Video
        self.cap = cv2.VideoCapture("college_images/animated.mp4")
        self.play_video()

    
    
        
        #==========Search system====================
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("montserrat", 12, "bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(Search_frame, text="Search By :", font=("montserrat", 15, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)   

        search_combo = ttk.Combobox(Search_frame, font=("montserrat", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "Roll_no", "Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=15, font=("montserrat", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search", width=12, font=("montserrat", 12, "bold"), bg="lightskyblue", fg="black")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(Search_frame, text="Show All", width=12, font=("montserrat", 12, "bold"), bg="lightskyblue", fg="black")
        showAll_btn.grid(row=0, column=4, padx=4)

        #=========table frame===================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")

        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")

        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")

        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll_No")
        self.student_table.heading("gender", text="Gender")

        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")

        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")

        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)

        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)

        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)

        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)

        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)

        self.student_table.column("email", width=100)   
        self.student_table.column("phone", width=100)

        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)

        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def play_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (720, 130))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.label.config(image=img)
            self.label.image = img
            self.root.after(20, self.play_video)  # Adjust timing for smooth playback
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Loop video
            self.play_video()


    def get_db_connection(self):
        try:
            return mysql.connector.connect(
                user="root",
                password="praful",
                host="localhost",
                database="face_recognizer",
                port=3305
            )
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Connection failed: {str(e)}", parent=self.root)
            return None


    #+==========function declaration====================
    def update_animation(self):
        self.label.config(image=self.frames[self.frame_idx])
        self.frame_idx = (self.frame_idx + 1) % len(self.frames)
        self.root.after(100, self.update_animation)  # Adjust speed


    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent = self.root)
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, self.var_email.get()):
            messagebox.showerror("Error", "Invalid email format", parent=self.root)
            return
        elif not self.var_phone.get().isdigit() or len(self.var_phone.get()) != 10:
            messagebox.showerror("Error", "Phone number must be exactly 10 digits", parent=self.root)
            return
        else:
            try:
                conn = self.get_db_connection()
                if conn is None: 
                    return
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student(dep,course,year,semester,student_id,name,division,roll,gender,dob,email,phone,address,teacher,photosample) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
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
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent =self.root)
            

    #==============fetch data====================
    def fetch_data(self):
        conn = self.get_db_connection()
        if conn is None: 
            return
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if(len(data)!=0):
            self.student_table.delete(*self.student_table.get_children() )
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        elif(len(data)==0):
            self.student_table.delete(*self.student_table.get_children() )
            empty=["","","","","","","","","","","","","","",""]
            self.student_table.insert("",END,values=empty)
        conn.close()


    #===============get cursor===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
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


    #====update func=======
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent = self.root)
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, self.var_email.get()):
            messagebox.showerror("Error", "Invalid email format", parent=self.root)
            return
        elif not self.var_phone.get().isdigit() or len(self.var_phone.get()) != 10:
            messagebox.showerror("Error", "Phone number must be exactly 10 digits", parent=self.root)
            return
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn = self.get_db_connection()
                    if conn is None: 
                        return
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
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
                messagebox.showinfo("Success","Student details successfully update ",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent =self.root)


    # ==========delete function=============
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = self.get_db_connection()
                    if conn is None: 
                        return
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id = %s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student details successfully Deleted ",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent =self.root)


    #======reset function=========
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


    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return  # Stop execution if fields are empty
            
        
        try:
            # ✅ Connect to MySQL database
            conn = self.get_db_connection()
            if conn is None: 
                return
            my_cursor = conn.cursor()
            student_id1=self.var_std_id.get()
            # ✅ Fetch correct student ID
            my_cursor.execute("SELECT MAX(student_id) FROM student")  
            result = my_cursor.fetchone()
            id = result[0] if result[0] else 1  # If table is empty, start with ID 1

            # ✅ Update student details
            my_cursor.execute("""
                UPDATE student 
                SET dep=%s, course=%s, year=%s, semester=%s, name=%s, division=%s, roll=%s, gender=%s, dob=%s, 
                    email=%s, phone=%s, address=%s, teacher=%s, photosample=%s 
                WHERE student_id=%s
            """, (
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

            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            # ✅ Load OpenCV face classifier
            face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                
                for (x, y, w, h) in faces:
                    return img[y:y+h, x:x+w]  # Return cropped face
                return None  # If no face detected, return None

            cap = cv2.VideoCapture(1)
            img_id = 0
            
              # ✅ Use correct student ID


            capturing = False  # ✅ Start capturing only when user presses "S"

            while True:
                ret, my_frame = cap.read()
                if not ret:
                    continue  # Skip if frame is not captured
                
                cv2.putText(my_frame, "Press 'S' to Start Capture", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.imshow("Camera Window", my_frame)

                key = cv2.waitKey(1) & 0xFF
                
                if key == ord('s') or ord('S'):  
                    capturing = True  # ✅ Start capturing when "S" key is pressed

                if capturing:  
                    cropped_face = face_cropped(my_frame)  # Call once
                    
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        file_name_path = "data/user." + student_id1 + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)

                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if img_id == 300:  # Stop after 100 images
                        break

                if key == 13:  # Stop if Enter key is pressed
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating data set successful!!!")

        except Exception as es:
            messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)



if __name__ == "__main__":  # Main function
    root = Tk()
    obj = Student(root)
    root.mainloop()

