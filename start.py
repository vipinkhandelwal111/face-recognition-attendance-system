from tkinter import *
from playsound import playsound
import os
from datetime import datetime;
root=Tk()

root.configure(background="black")
root.geometry("575x750")

def fun1():
    os.system("py dataset_capture.py")
    
def fun2():
    os.system("py training_dataset.py")

def fun3():
    os.system("py recognizer.py")
    playsound('sound.mp3')

def fun4():    
   os.startfile(os.getcwd()+"/help/about_us.pdf");
   
def fun5():
    root.destroy()

def fun6():
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')
    
img1 = PhotoImage(file="/attendance/icon/create.gif")
img2 = PhotoImage(file="/attendance/icon/train.gif")
img3 = PhotoImage(file="/attendance/icon/recognize.gif")
img4 = PhotoImage(file="/attendance/icon/sheet.gif")
img5 = PhotoImage(file="/attendance/icon/developer.gif")
img6 = PhotoImage(file="/attendance/icon/exit.gif")

root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20)
      ,fg="white",bg="black",height=2).grid(row=0,column=0,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=5)

Button(root,anchor=N,compound=TOP, text="create Dataset",image=img1,font=("times new roman",20),bg="#000000"
       ,fg='white',command=fun1).grid(row=3,column=0,columnspan=2,padx=5,pady=5)

Button(root,anchor=N,compound=TOP,image=img2,text="Train Dataset",font=("times new roman",20),bg="#000000",
       fg='white',command=fun2).grid(row=4,column=0,columnspan=2,padx=5,pady=5)

Button(root,anchor=N,compound=TOP,image=img3,text="Recognize",font=('times new roman',20),bg="#000000",
       fg="white",command=fun3).grid(row=3,column=3,columnspan=2,padx=5,pady=5)

Button(root,anchor=N,compound=TOP,image=img4,text="Attend. Sheet",font=('times new roman',20),bg="#000000",
       fg="white",command=fun6).grid(row=4,column=3,columnspan=2,padx=5,pady=5)

Button(root,anchor=N,compound=TOP,image=img5,text="About Us",font=('times new roman',20),bg="#000000",
       fg="white",command=fun4).grid(row=6,column=0,columnspan=2,padx=5,pady=5)

Button(root,anchor=N,compound=TOP,image=img6,text="Exit",font=('times new roman',20),bg="#000000",
       fg="white",command=fun5).grid(row=6,column=3,columnspan=2,padx=5,pady=5)


root.mainloop()
