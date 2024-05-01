from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
import mysql.connector
from tkinter import messagebox
import os

class Tuition:
    def __init__(self,root,host,username,password):
       self.root=root
       self.host=host
       self.username=username
       self.password=password
       
       self.root.geometry("1534x1134")
       self.root.wm_iconbitmap(r"images\jj.jpeg")
       self.root.title("Tuition Management-2024")
       Title_label=Label(self.root,text="TUITION FEE MANAGEMENT-2024",font="arial 30 bold",bg="yellow",fg="purple")
       Title_label.place(x=0,y=0,width=1534,height=50)

       self.var_sl=StringVar()
       self.var_name=StringVar()
       self.var_father=StringVar()
       self.var_mother=StringVar()
       self.var_class=StringVar()
       self.var_gender=StringVar()
       self.var_date=StringVar()
       self.var_mob=StringVar()
       self.var_sub=StringVar()
       self.var_month=StringVar()
       self.var_fee=StringVar()
       self.var_jan=StringVar()
       self.var_feb=StringVar()      
       self.var_mar=StringVar()
       self.var_apr=StringVar()
       self.var_may=StringVar()
       self.var_jun=StringVar()
       self.var_jul=StringVar()
       self.var_aug=StringVar()
       self.var_sep=StringVar()
       self.var_oct=StringVar()
       self.var_nov=StringVar()
       self.var_dec=StringVar()
     
       
       img_logot=Image.open(r"images/tu_logo.jpg")
       logot_resize=img_logot.resize((50,50))
       self.photo_logot=ImageTk.PhotoImage(logot_resize)
       self.logot=Label(self.root,image=self.photo_logot)
       self.logot.place(x=390,y=3,width=50,height=45)

       image_frame=Frame(self.root,bd=4,relief="groove",bg="green")
       image_frame.place(x=0,y=50,width=1534,height=200)

       img1=Image.open(r"images/tui1.jpg")
       logo_resize1=img1.resize((510,180))
       self.photo1=ImageTk.PhotoImage(logo_resize1)
       self.p1=Label(self.root,image=self.photo1)
       self.p1.place(x=5,y=57,width=510,height=185)

       
       img2=Image.open(r"images/tuit.jpeg")
       logo_resize2=img2.resize((510,180))
       self.photo2=ImageTk.PhotoImage(logo_resize2)
       self.p2=Label(self.root,image=self.photo2)
       self.p2.place(x=520,y=57,width=510,height=185)

       img3=Image.open(r"images/tui1.jpg")
       logo_resize3=img3.resize((510,180))
       self.photo3=ImageTk.PhotoImage(logo_resize3)
       self.p3=Label(self.root,image=self.photo3)
       self.p3.place(x=1035,y=57,width=510,height=185)

       image_frame=Frame(self.root,bd=4,relief="groove",bg="orange")
       image_frame.place(x=2,y=252,width=1525,height=532)
    #    upper frame
       upp_frame=LabelFrame(image_frame,text="Student Details",relief="sunken",font="arial 16 bold",bg="yellow",fg="red")
       upp_frame.place(x=3,y=3,width=1510,height=200)

       roll_no=Label(upp_frame,text="Roll no.:",font="arial 14 bold",bg="yellow",fg="blue")
       roll_no.grid(row=0,column=0,padx=3,pady=2,sticky=W)
       txt_roll=ttk.Entry(upp_frame,textvariable=self.var_sl,width=22,font="arial 14 bold")
       txt_roll.grid(row=0,column=1,padx=3,pady=2,sticky="w")

       name=Label(upp_frame,text="Name:",font="arial 14 bold",bg="yellow",fg="blue")
       name.grid(row=1,column=0,padx=3,pady=2,sticky=W)
       txt_name=ttk.Entry(upp_frame,textvariable=self.var_name,width=22,font="arial 14 bold")
       txt_name.grid(row=1,column=1,padx=3,pady=2,sticky="w")

       fath_name=Label(upp_frame,text="Father's Name :",font="arial 14 bold",bg="yellow",fg="blue")
       fath_name.grid(row=2,column=0,padx=3,pady=2,sticky=W)
       txt_fath_name=ttk.Entry(upp_frame,textvariable=self.var_father,width=22,font="arial 14 bold")
       txt_fath_name.grid(row=2,column=1,padx=3,pady=2,sticky="w")

       mot_name=Label(upp_frame,text="Mother's Name :",font="arial 14 bold",bg="yellow",fg="blue")
       mot_name.grid(row=3,column=0,padx=3,pady=2,sticky=W)
       txt_mot_name=ttk.Entry(upp_frame,width=22,textvariable=self.var_mother,font="arial 14 bold")
       txt_mot_name.grid(row=3,column=1,padx=3,pady=2,sticky="w")

       class_name=Label(upp_frame,text="Class :",bg="yellow",fg="blue",font="arial 14 bold")
       class_name.grid(row=0,column=2,padx=3,pady=2,sticky=W)
       class_combo=ttk.Combobox(upp_frame,textvariable=self.var_class,font="arial 14 bold",width=16,state="readonly")
       class_combo["value"]=("Select Class","Class I","Class II","Class III","Class IV",
                             "Class V","Class VI","Class VII","Class VIII"
                             ,"Class IX","Class X","Class XI","Class XII")
       class_combo.current(0)
       class_combo.grid(row=0,column=3,padx=3,pady=2,sticky=W)

       gender=Label(upp_frame,text="Gender :",bg="yellow",fg="blue",font="arial 14 bold")
       gender.grid(row=1,column=2,padx=3,pady=2,sticky=W)
       gender_combo=ttk.Combobox(upp_frame,textvariable=self.var_gender,font="arial 14 bold",width=16,state="readonly")
       gender_combo["value"]=("Select Gender","Female","Male")
       gender_combo.current(0)
       gender_combo.grid(row=1,column=3,padx=3,pady=2,sticky=W)

       mob=Label(upp_frame,text="Mobile number :",bg="yellow",font="arial 14 bold",fg="blue")
       mob.grid(row=2,column=2,padx=3,pady=2,sticky=W)
       mob_entry=ttk.Entry(upp_frame,textvariable=self.var_mob,font="arial 14 bold",width=18)
       mob_entry.grid(row=2,column=3,padx=3,pady=2,sticky=W)

       subject=Label(upp_frame,text="Subject:",bg="yellow",fg="blue",font="arial 14 bold")
       subject.grid(row=0,column=4,padx=3,pady=2,sticky=W)
       subject_combo=ttk.Combobox(upp_frame,textvariable=self.var_sub,font="arial 14 bold",width=16,state="readonly")
       subject_combo["value"]=("Select Subject","Math","Science","Math and Science","All Subject")
       subject_combo.current(0)
       subject_combo.grid(row=0,column=5,padx=3,pady=2,sticky=W)

       admission_date=Label(upp_frame,text="DOA(yyyy-mm-dd):",font="arial 14 bold",bg="yellow",fg="blue")
       admission_date.grid(row=3,column=2,padx=3,pady=2,sticky=W)
       txt_admission_date=ttk.Entry(upp_frame,textvariable=self.var_date,width=18,font="arial 14 bold")
       txt_admission_date.grid(row=3,column=3,padx=2,pady=2,sticky="w")


       month=Label(upp_frame,text="Month :",bg="yellow",fg="blue",font="arial 14 bold")
       month.grid(row=1,column=4,padx=3,pady=2,sticky=W)
       month_combo=ttk.Combobox(upp_frame,textvariable=self.var_month,font="arial 14 bold",width=16,state="readonly")
       month_combo["value"]=("Select Month","January","February","March","April","May","June","July",
                             "August","September","October","November","December")
       month_combo.current(0)
       month_combo.grid(row=1,column=5,padx=3,pady=2,sticky=W)

       amount=Label(upp_frame,text="Fee Paid :",font="arial 16 bold",bg="yellow",fg="blue")
       amount.grid(row=2,column=4,padx=3,pady=2,sticky=W)
       amount_entry=ttk.Entry(upp_frame,textvariable=self.var_fee,font="arial 16 bold",width=16)
       amount_entry.grid(row=2,column=5,padx=3,pady=2,sticky=W)

       
       clear_button=Button(upp_frame,command=self.clear_data,text="Clear",font="arial 10 bold"
                      ,fg="white",bg="blue",width=20)
       clear_button.grid(row=3,column=5,padx=3,pady=2)

       button_frame=Frame(upp_frame,bd=7,relief="sunken",bg="yellow")
       button_frame.place(x=1170,y=0,width=300,height=130)


       button1=Button(button_frame,text="Save  Student  Data",command=self.add_data,font="arial 12 bold"
                      ,fg="white",bg="red",width=26)
       button1.grid(row=0,column=0,padx=10,pady=2)

       button2=Button(button_frame,command=self.update_data,text="Update  Student  Data",font="arial 12 bold"
                      ,fg="white",bg="red",width=26)
       button2.grid(row=1,column=0,padx=10,pady=2)

       button3=Button(button_frame,text="Delete  Student  Data ",command=self.delete_data,font="arial 12 bold"
                      ,fg="white",bg="red",width=26)
       button3.grid(row=2,column=0,padx=10,pady=2)


    # lower frame
       lower_frame=LabelFrame(image_frame,text="Student Information Table",font="arial 16 bold", relief="sunken",bg="green",fg="pink")
       lower_frame.place(x=3,y=160,width=1510,height=365)
       
    #    search
       search_frame=Frame(lower_frame,bd=0,bg="yellow")
       search_frame.place(x=4,y=2,width=170,height=333)

       search_label=Label(search_frame,text="Search Here...",font="arial 14 bold",bg="red",fg="white")
       search_label.place(x=33,y=3,width=130,height=32)

       frame_inside_search=Frame(search_frame,bd=6,relief="sunken",bg="yellow")
       frame_inside_search.place(x=5,y=160,width=160,height=170)
       
       
       img_logo=Image.open(r"images\search_logo.png")
       logo_resize=img_logo.resize((25,30))
       self.photo_logo=ImageTk.PhotoImage(logo_resize)
       self.logo=Label(search_frame,image=self.photo_logo)
       self.logo.place(x=5,y=3,width=28,height=28)

       img_logoo=Image.open(r"images/sear.jpeg")
       logoo_resize=img_logoo.resize((155,120))
       self.photo_logoo=ImageTk.PhotoImage(logoo_resize)
       self.logoo=Label(search_frame,image=self.photo_logoo)
       self.logoo.place(x=5,y=40,width=160,height=118)

       self.var_combo_search=StringVar()
       self.var_entry_search=StringVar()

       search_combo=ttk.Combobox(frame_inside_search,textvariable=self.var_combo_search,font="arial 14 bold",state="readonly")
       search_combo["value"]=("Roll_no","Name")
       search_combo.current(0)
       search_combo.place(x=5,y=5,width=140,height=35)

       search_entry=ttk.Entry(frame_inside_search,textvariable=self.var_entry_search,font="arial 14 bold")
       search_entry.place(x=5,y=44,width=140,height=35)

       search_button=Button(frame_inside_search,command=self.search_data,text="Click Here",font="arial 14 bold",bg="orange",fg="red")
       search_button.place(x=5,y=82,width=140,height=35)

       show_button=Button(frame_inside_search,command=self.showall_data,text="Show All",font="arial 14 bold",bg="green",fg="black")
       show_button.place(x=5,y=120,width=140,height=35)


    #    table
       table_frame=Frame(lower_frame,bg="yellow")
       table_frame.place(x=177,y=2,width=1325,height=333)
       
       table_scrollh=Scrollbar(table_frame,orient="horizontal")
       table_scrollv=Scrollbar(table_frame,orient="vertical")

       self.tui_table=ttk.Treeview(table_frame,
                                 column=("sl","Name","Father","Mother","Class","Gender","mobile_number","DOA","sub","jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"),
                                 xscrollcommand=table_scrollh.set,yscrollcommand=table_scrollv.set)
       
       table_scrollh.pack(side="bottom",fill=X)
       table_scrollv.pack(side="right",fill="y")
       table_scrollh.config(command=self.tui_table.xview)
       table_scrollv.config(command=self.tui_table.yview)
      
       self.tui_table.heading("sl",text="Roll No.")
       self.tui_table.heading("Name",text="Name")
       self.tui_table.heading("Father",text="Father's Name")
       self.tui_table.heading("Mother",text="Mother's Name")
       self.tui_table.heading("Class",text="Class")
       self.tui_table.heading("Gender",text="Gender")
       self.tui_table.heading("mobile_number",text="Mobile Number")
       self.tui_table.heading("DOA",text="Date of Admission")
       self.tui_table.heading("sub",text="Subject")
       self.tui_table.heading("jan",text="January")
       self.tui_table.heading("feb",text="February")
       self.tui_table.heading("mar",text="March")
       self.tui_table.heading("apr",text="April")
       self.tui_table.heading("may",text="May")
       self.tui_table.heading("jun",text="June")
       self.tui_table.heading("jul",text="July")
       self.tui_table.heading("aug",text="August")
       self.tui_table.heading("sep",text="September")
       self.tui_table.heading("oct",text="October")
       self.tui_table.heading("nov",text="November")
       self.tui_table.heading("dec",text="December")
   
       
       self.tui_table["show"]="headings"
       self.tui_table.column("sl",width=50)
       self.tui_table.column("Name",width=150)
       self.tui_table.column("Father",width=150)
       self.tui_table.column("Mother",width=150)
       self.tui_table.column("Class",width=100)
       self.tui_table.column("Gender",width=150)
       self.tui_table.column("mobile_number",width=150)
       self.tui_table.column("DOA",width=150)
       self.tui_table.column("sub",width=150)
       self.tui_table.column("jan",width=70)
       self.tui_table.column("feb",width=70)
       self.tui_table.column("mar",width=70)
       self.tui_table.column("apr",width=70)
       self.tui_table.column("may",width=70)
       self.tui_table.column("jun",width=70)
       self.tui_table.column("jul",width=70)
       self.tui_table.column("aug",width=70)
       self.tui_table.column("sep",width=70)
       self.tui_table.column("oct",width=70)
       self.tui_table.column("nov",width=70)
       self.tui_table.column("dec",width=70)

       self.tui_table.pack(fill="both",expand=1)
       self.tui_table.bind("<ButtonRelease>",self.fill_details)
       self.fetch_data()
        

    def change(self):
       if self.var_month.get() == "January":
         self.var_jan.set(self.var_fee.get())
       elif self.var_month.get() == "February":
         self.var_feb.set(self.var_fee.get())
       elif self.var_month.get() == "March":
         self.var_mar.set(self.var_fee.get())
       elif self.var_month.get() == "April":
         self.var_apr.set(self.var_fee.get())
       elif self.var_month.get() == "May":
         self.var_may.set(self.var_fee.get())
       elif self.var_month.get() == "June":
         self.var_jun.set(self.var_fee.get())
       elif self.var_month.get() == "July":
          self.var_jul.set(self.var_fee.get())
       elif self.var_month.get() == "August":
          self.var_aug.set(self.var_fee.get())
       elif self.var_month.get() == "September":
          self.var_sep.set(self.var_fee.get())
       elif self.var_month.get() == "October":
          self.var_oct.set(self.var_fee.get())
       elif self.var_month.get() == "November":
          self.var_nov.set(self.var_fee.get())
       else:
          self.var_dec.set(self.var_fee.get())
  
    def fetch_data(self):
       conn=mysql.connector.connect(host=self.host,username=self.username,password=self.password,database="student_data")
       my_cursor=conn.cursor()
       my_cursor.execute("select * from tuition_fee")
       data=my_cursor.fetchall()
     
       self.tui_table.delete(*self.tui_table.get_children())
       for i in data:
         self.tui_table.insert("","end",value=i)
         conn.commit()
       conn.close()
    def check_condition(self):
          conn=mysql.connector.connect(host=self.host,username=self.username,
                                             password=self.password,database="student_data")
          my_cursor = conn.cursor()
          output=my_cursor.execute("SELECT * FROM tuition_fee WHERE Roll_no=%s", (self.var_sl.get(),))
          output=my_cursor.fetchone()
          conn.close()
          return output
    
    def add_data(self):
           if self.var_name.get()=="":
               messagebox.showerror("Error","Roll no. field is necessary")
           else:
               try:
                   if not self.check_condition():
                      
                      self.change()
                      conn=mysql.connector.connect(host=self.host,username=self.username,
                                             password=self.password,database="student_data")
                      my_cursor=conn.cursor()
                     
                      my_cursor.execute("INSERT INTO tuition_fee (Roll_no,Name,Father_Name,Mother_Name,Class,Gender,Mobile_number,Admission_Date,Subject,January,February,March,april,May,June,July,August,September,October,November,December) VALUES (%s,%s,%s, %s, %s, %s, %s, %s,%s,%s,%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)",
                              (self.var_sl.get(),
                               self.var_name.get(),
                               self.var_father.get(),
                               self.var_mother.get(),
                               self.var_class.get(),
                               self.var_gender.get(),
                               self.var_mob.get(),
                               self.var_date.get(),
                               self.var_sub.get(),
                               self.var_jan.get(),
                               self.var_feb.get(),
                               self.var_mar.get(),
                               self.var_apr.get(),
                               self.var_may.get(),
                               self.var_jun.get(),
                               self.var_jul.get(),
                               self.var_aug.get(),
                               self.var_sep.get(),
                               self.var_oct.get(),
                               self.var_nov.get(),
                               self.var_dec.get()

                                 
                                 ))
                      conn.commit()
                      self.fetch_data()
      

                      conn.close()
                    
                      messagebox.showinfo("Success","Student has been successfully added.")
                      self.var_sl.set("")
                      self.var_name.set(""),
                      self.var_father.set("")
                      self.var_mother.set("")
                      self.var_class.set("Select Class")
                      self.var_gender.set("Select Gender")
                      self.var_month.set("Select Month")
                      self.var_mob.set("")
                      self.var_date.set("")
                      self.var_sub.set("Select Subject")
                      self.var_fee.set("")
                      self.var_jan.set("")
                      self.var_feb.set("")
                      self.var_mar.set("")
                      self.var_apr.set("")
                      self.var_may.set("")
                      self.var_jun.set("")
                      self.var_jul.set("")
                      self.var_aug.set("")
                      self.var_sep.set("")
                      self.var_oct.set("")
                      self.var_dec.set("")
                      self.var_nov.set("")
                   else:                
                      messagebox.showerror("Error","You have already entered this student details.")

                   
                   

                                    
               except Exception as e:
                   messagebox.showerror("Error",f"Problem:{str(e)}",parent=self.root)

    def check_month(self):
       month_update=""
       l=["January","February","March","April","May","June","July",
         "August","September","October","November","December"]
       for i in range(12):
          if self.var_month.get()==l[i]:
             month_update=l[i]
       return month_update
       
    def update_data(self):
       if self.var_sl.get()=="":
          messagebox.showerror("Error",'Roll no.field is mendatory.')
       else:
          try:
             update=messagebox.askyesno("Update","Are you sure to update student details..?")
             if update>0:
                conn=mysql.connector.connect(host=self.host,username=self.username,
                                             password=self.password,database="student_data")
                my_cursor=conn.cursor()

                my_cursor.execute(f"update tuition_fee set {self.check_month()} = %s,Name=%s,Father_Name=%s,Mother_Name=%s,Class=%s,Gender=%s,Mobile_number=%s,Admission_Date=%s,Subject=%s where Roll_no=%s",
                   (self.var_fee.get(),self.var_name.get(),self.var_father.get(),self.var_mother.get(),self.var_class.get(),self.var_gender.get(),self.var_mob.get(),self.var_date.get(),self.var_sub.get(),self.var_sl.get()))

                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("success","Detail has been successfully updated")
             else:
                pass
          except Exception as e:
             messagebox.showerror("Error",f"Problem: {str(e)}",parent=self.root)

    def search_data(self):
       if self.var_combo_search.get() == "" or self.var_entry_search.get() == "":
          messagebox.showerror("Error", "Please enter details ")
       else:
          try:
            C=str(self.var_combo_search.get())
            E=str(self.var_entry_search.get())
            conn = mysql.connector.connect(host=self.host,username=self.username,
                                             password=self.password, database="student_data")
            my_cursor = conn.cursor()
            my_cursor.execute(f"SELECT * FROM tuition_fee WHERE {C} LIKE '%{E}%'")
            row = my_cursor.fetchall()
            if len(row) != 0:
                self.tui_table.delete(*self.tui_table.get_children())
                for i in row:
                    self.tui_table.insert("", END, values=i)
                conn.commit()
            conn.close()
          
          
          except Exception as e:
            messagebox.showerror("Error", f"Problem: {str(e)}", parent=self.root)

    
                   
    def showall_data(self):
       self.fetch_data()
       
    def fill_details(self,event=""):
       #
       cursor_row=self.tui_table.focus()
       content=self.tui_table.item(cursor_row)
       data=content["values"]
       self.var_sl.set(data[0])
       self.var_name.set(data[1])
       self.var_father.set(data[2])
       self.var_mother.set(data[3])
       self.var_class.set(data[4])
       self.var_gender.set(data[5])
       self.var_mob.set(data[6])
       self.var_date.set(data[7])
       self.var_sub.set(data[8])
       i=0
       l=["January","February","March","April","May","June","July",
            "August","September","October","November","December"]
       while i<12:
          if  not str(data[i+9])=="":
            #  print(data[i+8])
             self.var_month.set(l[i])
             self.var_fee.set(data[i+9])
             break
          i+=1
    def delete_data(self):
       if self.var_sl.get()=="":
          messagebox.showerror("Error","You have not selected any data.")
       else:
          try:
             clear=messagebox.askyesno("Remove","Are you sure to remove entered student details..?",parent=self.root)
             if clear>0:
                conn=mysql.connector.connect(host=self.host,username=self.username,
                                             password=self.password,database="student_data")
                my_cursor=conn.cursor()
                my_cursor.execute("delete from tuition_fee where Roll_no=%s",(self.var_sl.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_data()
               
                messagebox.showinfo("sucess","entered student data has been successfully removed.")
          except Exception as e:
             messagebox.showerror("Error",f"Problem: {str(e)}",parent=self.root)

    def clear_data(self):
      self.var_sl.set("")
      self.var_name.set(""),
      self.var_father.set("")
      self.var_mother.set("")
      self.var_class.set("Select Class")
      self.var_gender.set("Select Gender")
      self.var_month.set("Select Month")
      self.var_mob.set("")
      self.var_date.set("")
      self.var_sub.set("Select Subject")
      self.var_fee.set("")
      self.var_jan.set("")
      self.var_feb.set("")
      self.var_mar.set("")
      self.var_apr.set("")
      self.var_may.set("")
      self.var_jun.set("")
      self.var_jul.set("")
      self.var_aug.set("")
      self.var_sep.set("")
      self.var_oct.set("")
      self.var_dec.set("")
      self.var_nov.set("")  
          
     
if __name__=="__main__":
     workbench_host=input("Enter your workbench host name:")
     workbench_username=input("Enter your workbench username:")
     workbench_password=input("Enter your workbench password:")
     root=Tk()
     obj=Tuition(root,workbench_host,workbench_username,workbench_password)
     root.mainloop()

