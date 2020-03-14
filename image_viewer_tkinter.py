from tkinter import *
from PIL import ImageTk,Image #pillow



root= Tk()
root.title("image viewer")
root.iconbitmap('C:/Users/hp/Downloads/sun.ico')

my_img1=ImageTk.PhotoImage(Image.open('C:/xtra/sunflo.jpg'))
my_img2=ImageTk.PhotoImage(Image.open('C:/xtra/daisy.jpg'))
my_img3=ImageTk.PhotoImage(Image.open('C:/xtra/lotus.jpg'))
my_img4=ImageTk.PhotoImage(Image.open('C:/xtra/beau.jpg'))
my_img5=ImageTk.PhotoImage(Image.open('C:/xtra/yellow.jpg'))


image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]




my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_num):
    global my_label
    global button_forw
    global buton_back

    my_label.grid_forget() # current pic and next pic should not overlap
    my_label=Label(image=image_list[image_num-1])
    button_forw=Button(root,text=">>",command=lambda : forward(image_num+1))
    button_back=Button(root,text="<<",command=lambda: back(image_num-1))

    if image_num==5:
        button_forw=Button(root,text=">>",state=DISABLED)
        
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forw.grid(row=1,column=2)

    
def back(image_num):
    global my_label
    global button_forw
    global buton_back

    my_label.grid_forget() # current pic and next pic should not overlap
    my_label=Label(image=image_list[image_num-1])
    button_forw=Button(root,text=">>",command=lambda : forward(image_num+1))
    button_back=Button(root,text="<<",command=lambda: back(image_num-1))

    if image_num==1:
        button_back=Button(root,text="<<",state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forw.grid(row=1,column=2)


#creating buttons

button_back=Button(root,text="<<",command=back)
button_exit=Button(root,text="exit",command=root.destroy)
button_forw=Button(root,text=">>",command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forw.grid(row=1,column=2)




button_quit=Button(root,text="exit",command=root.destroy)
button_quit.pack()


root.mainloop() 
