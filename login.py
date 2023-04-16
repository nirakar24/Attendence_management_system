import customtkinter as ctk
from tkinter import messagebox
import sqlite3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('green')

def close():
    root.destroy()

def data():
    db=sqlite3.connect("students.db")

    cur_sor = db.cursor()
    cur_sor.execute("INSERT INTO Attendence VALUES (:name, :roll_no , :department, :password,:present,:absent)",
                    {
                        'name':name.get(),
                        'roll_no':roll_no.get(),
                        'department':depart.get(),
                        'password':passwrd.get(),
                        'present':0,
                        'absent':0
                    }
                    
                    )

    db.commit()

    db.close()

    messagebox.showinfo("Authentication","You have successfully Signed up")
    root.deiconify()

    sign_window.destroy()


    # name.delete(0,END)
    # roll_no.delete(0,END)
    # passwrd.delete(0,END)
    # conf.delete(0,END)  

def sign_up():
    global name,roll_no,depart,passwrd,conf,sign_window

    sign_window=ctk.CTkToplevel()
    sign_window.geometry("500x400")

    frame=ctk.CTkFrame(sign_window)
    frame.pack(pady=20,padx=60,fill="both",expand=True)

    label=ctk.CTkLabel(frame,text="Sign Up",font=("Roboto", 24))
    label.pack(pady=12,padx=10)

    name=ctk.CTkEntry(frame,placeholder_text="Your name")
    name.pack(pady=12,padx=10)

    roll_no=ctk.CTkEntry(frame, placeholder_text="Roll no")
    roll_no.pack(pady=12,padx=10)

    depart=ctk.CTkEntry(frame, placeholder_text="Department")
    depart.pack(pady=12,padx=10)

    passwrd=ctk.CTkEntry(frame,placeholder_text="Password",show="*")
    passwrd.pack(pady=12,padx=10)

    conf=ctk.CTkEntry(frame,placeholder_text="Confirm Password")
    conf.pack(pady=12,padx=10)

    button=ctk.CTkButton(frame,text="Proceed",command=data)
    button.pack(pady=12,padx=10)
    root.withdraw()
    

def login():
    def disable_event():
        pass
    def present():
        db=sqlite3.connect("students.db")

        cur_sor = db.cursor()
        cur_sor.execute(f"UPDATE Attendence SET present=present+1 WHERE name='{user.get()}'")
        db.commit()

        db.close()   
        messagebox.showinfo("Info","Your attendence have been recorded\nChanges will be applied after restart")

    def absent():
        db=sqlite3.connect("students.db")

        cur_sor = db.cursor()
        cur_sor.execute(f"UPDATE Attendence SET absent=absent+1 WHERE name='{user.get()}'")
        db.commit()

        db.close()   
        messagebox.showinfo("Info","You have missed a class\nChanges will be applied after restart")
    # global frame
    db=sqlite3.connect("students.db")

    cur_sor = db.cursor()
    cur_sor.execute(f"SELECT * FROM Attendence WHERE name='{user.get()}'")

    student = cur_sor.fetchall()
    details=student[0]

    key=""
    
    for i in student:
        print(i)
        key=i[3]

    print(key)
    db.commit()

    db.close() 

    given_key=passwd.get()

    if given_key==key:
        window=ctk.CTkToplevel()
        window.geometry("400x600+0+0")
        window.title("User Profile")
        # usr=user.get()
        frame=ctk.CTkFrame(window)
        frame.pack(pady=20,padx=60,fill="both",expand=True)
        label=ctk.CTkLabel(frame,text="Profile",font=("Roboto", 24))
        label.pack(pady=12,padx=10)
        label2=ctk.CTkLabel(frame,text=f"Name : {details[0]} ")
        label2.pack(pady=12,padx=10)
        label3=ctk.CTkLabel(frame,text=f"Roll no : {details[1]} ")
        label3.pack(pady=12,padx=10)
        label4=ctk.CTkLabel(frame,text=f"Department : {details[2]} ")
        label4.pack(pady=12,padx=10)
        label5=ctk.CTkLabel(frame,text=f"Classes Attended : {details[4]} ")
        label5.pack(pady=12,padx=10)
        label6=ctk.CTkLabel(frame,text=f"Not attended : {details[5]} ")
        label6.pack(pady=12,padx=10)
        total=details[4]+details[5]
        try:
            label7=ctk.CTkLabel(frame,text=f"Overall Percentage : {round(((details[4]/(total))*100),2)} %")
            label7.pack(pady=12,padx=10)

            slider_1 = ctk.CTkSlider(master=frame, from_=0, to=100,state='disabled')
            slider_1.pack(pady=12, padx=10)
            slider_1.set(round(((details[4]/(total))*100),2))

        except(ZeroDivisionError):
            label7=ctk.CTkLabel(frame,text=f"Overall Percentage : 0 %")
            label7.pack(pady=12,padx=10)

            slider_1 = ctk.CTkSlider(master=frame, from_=0, to=100,state='disabled')
            slider_1.pack(pady=12, padx=10)
            slider_1.set(0)


        button2=ctk.CTkButton(frame,text="Present",command=present)
        button2.pack(pady=12,padx=10)
        button3=ctk.CTkButton(frame,text="Absent",command=absent)
        button3.pack(pady=12,padx=10)
        button1=ctk.CTkButton(frame,text="close",command=close)
        button1.pack(pady=12,padx=10)
        root.withdraw()

        window.protocol("WM_DELETE_WINDOW", disable_event)
        window.mainloop()

        window.mainloop()

    else:
        root.destroy()

root=ctk.CTk()
root.geometry("500x350")
root.title("Authentication")

frame=ctk.CTkFrame(root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label=ctk.CTkLabel(frame,text="Login",font=("Roboto", 24))
label.pack(pady=12,padx=10)

user=ctk.CTkEntry(frame,placeholder_text="Student name")
user.pack(pady=12,padx=10)

passwd=ctk.CTkEntry(frame,placeholder_text="Password",show="*")
passwd.pack(pady=12,padx=10)

button=ctk.CTkButton(frame,command=login,text="Login")
button.pack(pady=12,padx=10)
button2=ctk.CTkButton(frame,command=sign_up,text="Sign up")
button2.pack(pady=12,padx=10)
root.mainloop()


