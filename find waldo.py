"""
By Fleserig
This is game where you can find waldo and check if you're right.
"""

from tkinter import *
from tkinter import messagebox
import os
import random
from PIL import Image, ImageTk
import time

# setting screen appearance
root = Tk()
root.state("zoomed")
root.config(cursor="tcross")
root['bg'] = "white"

# start time
start = time.time()
# get random picture
files = os.listdir('./images')
rfile = random.choice(files)
# get waldo location
f_x, f_y = map(int, ((rfile.split(".")[0]).split("-")[0]).split("x"))
l_x, l_y = map(int, ((rfile.split(".")[0]).split("-")[1]).split("x"))

# resize image to screen size
def resize_image(e):
    global img, img2
    # if the width of image is too low then we resize it
    # and if the image is too high we resize it, but we check whether height distance or width distance is bigger
    if e.width-img.width() > e.height-img.height():
        height = e.height
        k = height/img.height()
        width = k*img.width()
        resize_waldo(k)
    else:
        width = e.width
        k = width/img.width()
        height = k*img.height()
        resize_waldo(k)
    # sets new width and height to image
    new_img = img2.resize((int(width), int(height)), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(new_img)
    label.configure(image=img)

# resize waldo with given k which is the same as in resize_image function
def resize_waldo(k):
    global f_x, f_y, l_x, l_y
    f_x = k * f_x
    f_y = k * f_y
    l_x = k * l_x
    l_y = k * l_y

# check if your position of mouse is in the field of waldo, whose location is saved in picture
def check_guess(e):
    x = e.x
    y = e.y
    if x-f_x > 0 and x-l_x < 0 and y-f_y > 0 and y-l_y < 0:
        alert("You found Waldo", "Time taken:" + str(time.time()-start))
    else:
        alert("Try again ", "There is no Waldo")

# display info dialog
def alert(title, message):
    show_method = getattr(messagebox, 'show{}'.format("info"))
    show_method(title, message)

# display image in tkinter
img2 = Image.open("images/"+rfile)
img = ImageTk.PhotoImage(img2)
label = Label(root,image=img)
label.pack()

# there was some bugs after minimize the window so i must to put this here
root.geometry(f"{int(img.width())}x{int(img.height())}")

# when click on screen
root.bind('<Button>', check_guess)
# after change screen size
root.bind('<Configure>', resize_image)

root.mainloop()
