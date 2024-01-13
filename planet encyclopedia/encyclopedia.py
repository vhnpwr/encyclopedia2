from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
root=Tk()

root.title("planet encyclopedia")
root.geometry("700x700")
root.configure(bg="lightblue")

venus_img=ImageTk.PhotoImage(Image.open("venus.jpg"))
earth_img=ImageTk.PhotoImage(Image.open("earth.jpg"))
mercury_img=ImageTk.PhotoImage(Image.open("mercury.jpg"))

encyclopedia=Label(root,text="planet encyclopedia",font=("arial",18,"bold"))
encyclopedia.place(relx=0.5,rely=0.1,anchor=CENTER)

planet=Label(root,text="planet",font=("arial",16))
planet.place(relx=0.3,rely=0.2,anchor=CENTER)

list1=["Mercury","Venus","Earth"]
value=StringVar()
dropdown=ttk.Combobox(root,values=list1,textvariable=value)
dropdown.place(relx=0.5,rely=0.2,anchor=CENTER)

picture=Label(root)
picture.place(relx=0.5,rely=0.6,anchor=CENTER)



lbl3=Label(root)
lbl3.place(relx=0.5,rely=0.8,anchor=CENTER)

info=Label(root)
info.place(relx=0.5,rely=0.9,anchor=CENTER)


def planetInfo():
    print("this is a function")
    planet_name=value.get()
    if planet_name=="Mercury":
        picture["image"]=mercury_img
        lbl3["text"]="Mercury"
        info["text"]="Mercury is the smallest planet in our solar sysytem,It's just little bigger than Earth's moon "
    elif planet_name=="Venus":
        picture["image"]=venus_img
        lbl3["text"]="Venus"
        info["text"]="Venus is the brightest object in the sky after the sun and the moon,and sometimes looks like a bright star in the morning or evening sky"
    elif planet_name=="Earth":
        picture["image"]=earth_img
        lbl3["text"]="Earth"
        info["text"]="Earth is the only place in the known universe confirmed to host life and liquid water on it's surface"
    
    
showInfo=Button(root,text="show Information",command=planetInfo)
showInfo.place(relx=0.5,rely=0.3,anchor=CENTER)


root.mainloop()