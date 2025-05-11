from customtkinter import *
from PIL import Image,ImageFilter

my_image= Image.open('img.png')
img = CTkImage(light_image=my_image, size=(350, 200))

window = CTk()
label = CTkLabel(window, image=img, text="")
label.pack()


def rotate_func():
    global my_image
    my_image = my_image.rotate(90)
    img.configure(light_image=my_image)
    label.configure(image=img)

rotate_btn = CTkButton(window, text="повернути", command=rotate_func)
rotate_btn.pack()
def rotate_func():
    global my_image
    my_image = my_image.convert('L')
    img.configure(light_image=my_image)
    label.configure(image=img)

color_btn = CTkButton(window, text="змінити колір на сірий", command=rotate_func)
color_btn.pack()

def rotate_func():
    global my_image
    my_image = my_image.filter(ImageFilter.BLUR)
    img.configure(light_image=my_image)
    label.configure(image=img)

fliter_btn = CTkButton(window, text="розмитя", command=rotate_func)
fliter_btn.pack()

def rotate_func():
    global my_image
    my_image = my_image.filter(ImageFilter.SHARPEN)
    img.configure(light_image=my_image)
    label.configure(image=img)

rizrt_btn = CTkButton(window, text="різке", command=rotate_func)
rizrt_btn.pack()

def rotate_func():
    global my_image
    my_image = my_image.filter(ImageFilter.DETAIL)
    img.configure(light_image=my_image)
    label.configure(image=img)

VUDILENZ_btn = CTkButton(window, text="ВИДІЛЯНЯ", command=rotate_func)
VUDILENZ_btn.pack()
def rotate_func():
    global my_image
    my_image = my_image.filter(ImageFilter.EDGE_ENHANCE)
    img.configure(light_image=my_image)
    label.configure(image=img)

contur_btn = CTkButton(window, text="підсилити контури", command=rotate_func)
contur_btn.pack()

def rotate_func():
    global my_image
    my_image = my_image.filter(ImageFilter.EMBOSS)
    img.configure(light_image=my_image)
    label.configure(image=img)

rel_btn = CTkButton(window, text="релєф", command=rotate_func)
rel_btn.pack()

window.mainloop()