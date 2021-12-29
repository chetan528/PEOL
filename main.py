import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

import cv2  # importing cv
import imutils
import zoom
import tkinter as tk

root = Tk()

class PClass(object):
    angle = 0
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.WelcomeLabel = Label(root, text = "PEOL PROJECT", bg = "Black", fg = "White")
        self.WelcomeLabel.pack()

        self.AButton = Button(root, text = "click 1", command = self.CharClick)
        self.AButton.pack(side = LEFT)

        self.BButton = Button(root, text = "click 2",command = self.CharClick1)
        self.BButton.pack(side = LEFT)

        self.zoom1 = Button(root, text="zoom1", command=self.zoomOUTIN1)
        # self.zoom1.grid(row = 1, column = 1)
        self.zoom1.pack(side=LEFT)

        self.zoom2 = Button(root, text="zoom2", command=self.zoomOUTIN2)
        self.zoom2.pack(side=LEFT)

        self.rotate = Button(root, text="rotate", command=self.rotate)
        self.rotate.pack(side=LEFT)

        main_frame = Frame(root)
        main_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        self.second_frame = Frame(my_canvas)

        my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        print("In init constructor")

    # def scrollOnClick(self):


    def CharClick(self):
        canvas = Canvas(self.second_frame,width = 1000, height = 1000)
        canvas.pack()
        # img = ImageTk.PhotoImage(Image.open("0001.jpg"))
        img = (Image.open("0001.jpg"))
        resized_image = img.resize((500, 800), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)

        canvas.create_image(0, 0, image=new_image, anchor=NW)

        mainloop()


    def CharClick1(self):

        canvas = Canvas(self.second_frame,width = 1000, height = 1000)
        canvas.pack()
        img = (Image.open("0003.jpg"))
        resized_image = img.resize((500, 800), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)

        canvas.create_image(0, 0, image=new_image, anchor=NW)
        # Tilt image
        # inputtxt = tk.Text(self.frame,
        #                    height=5,
        #                    width=20)
        # inputtxt.pack()

        self.tilt=Entry(self.frame, width=10, borderwidth=5)
        self.tilt.grid(row=0, column=0, columnspan=1, padx=10, pady=10)
        self.tiltLeftButton = Button(self.frame, text="-", padx=5, pady=5, command=self.tiltLeft).grid(row=2, column=1)
        self.tiltRightButton = Button(self.frame, text="+", padx=5, pady=5,command = self.tiltRight).grid(row=2, column=10)
        # tilt.pack()


        mainloop()

    def zoomOUTIN1(self):

        path = '0001.jpg'  # place path to your image here
        root = tkinter.Toplevel()
        app = zoom.Zoom(root, path=path)
        root.mainloop()

    def zoomOUTIN2(self):
        path = '0003.jpg'  # place path to your image here
        root = tkinter.Toplevel()
        app = zoom.Zoom(root, path=path)
        root.mainloop()

    def rotate(self):
        # read an image as input using OpenCV
        image = cv2.imread(r"0001.jpg")
        resized_image = cv2.resize(image, (900, 900))
        # new_image = ImageTk.PhotoImage(resized_image)
        self.angle += 90
        self.angle %= 360
        Rotated_image = imutils.rotate(resized_image, angle=self.angle)

        # display the image using OpenCV library of angle 90
        cv2.imshow("Rotated", Rotated_image)

    def tiltLeft(self):
        tilted_img = imutils.rotate(img, angle=10)
        cv2.imshow("Rotated", tilted_img)

    def tiltRight(self):
        tilted_img = imutils.rotate(img, angle=10)
        cv2.imshow("Rotated", tilted_img)


k = PClass(root)
root.mainloop()