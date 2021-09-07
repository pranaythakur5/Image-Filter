from tkinter import *
import tkinter.messagebox
import cv2
import numpy as np
import os
from tkinter import filedialog



def fileselector():

    main_win = tkinter.Tk()
    main_win.withdraw()

    main_win.sourceFile = filedialog.askopenfilename(
        filetypes=(("Image Files", ("*.jpg", "*.png", "*.jpeg")), ("All Files", "*")), parent=main_win, initialdir="/",
        title='Please select an image file')
    main_win.destroy()

    img_path = main_win.sourceFile
    print(type(img_path))
    name1 = (os.path.basename(img_path))
    n = len(name1)
    name = name1[:n - 4]
    print(name)
    image = cv2.imread(img_path)
    width = 1000
    height = 600  # keep original height
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    os.mkdir(name)
    cv2.imwrite("image.png", image)
    cv2.imwrite('./' + name + '/' + name + '.png', image)


def showimage():

    image = cv2.imread("./image.png")
    cv2.imwrite('./image.jpg', image)
    cv2.imshow("./image", image)
    cv2.waitKey(0)


# Converting the image into grayscale
def grayscale():

    image = cv2.imread("./image.png")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('blackand#ffffff.png', image)
    cv2.imshow("black and #ffffff", image)
    cv2.waitKey(0)


# Converting the image into inverted form
def invert():

    img = cv2.imread("./image.png")
    invert = cv2.bitwise_not(img)
    cv2.imwrite('./' + name + '/invert.png', invert)
    cv2.imshow("invert", invert)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Making Sepia Filter
def apply_sepia():

    image = cv2.imread("./image.png")
    frame = np.array(image, dtype=np.float64)  # converting to float to prevent loss
    frame = cv2.transform(frame, np.matrix([[0.272, 0.534, 0.131],
                                            [0.349, 0.686, 0.168],
                                            [0.393, 0.769, 0.189]]))  # multipying image with special sepia matrix
    frame[np.where(frame > 255)] = 255  # normalizing values greater than 255 to 255
    frame = np.array(frame, dtype=np.uint8)  # converting back to int
    cv2.imshow("sepia", frame)
    cv2.waitKey(0)


#########################


img = cv2.imread("./sample.png")
name = ""
counter = 0
click = False
flag = 0
root = Tk()
root.title("GUI : Image Filters")

root.geometry("873x450")

root.configure(background='#ffffff')
Tops = Frame(root, bg='#ffffff', pady=1, width=450, height=50, relief="ridge")
Tops.grid(row=0, column=0)

Title_Label = Label(Tops, font=('Comic Sans MS', 19, 'bold'), text="     Image  Filters  with  Python OpenCV\t\t",
                    bg='black', fg='#ffffff', justify="center")
Title_Label.grid(row=0, column=0)
MainFrame = Frame(root, bg='#ffffff', pady=2, padx=2, width=1350, height=100, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, width=200, height=200, pady=2, bg='#ffffff', relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=5, width=200, height=200, padx=1, pady=2, bg='#f2ccff', relief=RIDGE)
RightFrame.pack(side=RIGHT)

Label_1 = Label(RightFrame, font=('lato black', 37, 'bold'), text=" Image Filters ", padx=2, pady=2, bg="#65a4fc",
                fg="black")
Label_1.grid(row=0, column=0)

Label_2 = Label(RightFrame, font=('arial', 30, 'bold'), text="", padx=2, pady=2, bg="#f2ccff", fg="black")
Label_2.grid(row=1, column=0, sticky=W)

Label_9 = Button(RightFrame, font=('arial', 19, 'bold'), text="  Invert ", padx=2, pady=2, bg="#9c1ae8", fg="#ffffff",
                 command=invert)
Label_9.grid(row=2, column=0, sticky=N)

Label_2 = Label(RightFrame, font=('arial', 13, 'bold'), text="", padx=2, pady=2, bg="#f2ccff", fg="black")
Label_2.grid(row=3, column=0, sticky=W)

Label_9 = Button(RightFrame, font=('arial', 19, 'bold'), text="  Sepia ", padx=2, pady=2, bg="#9c1ae8", fg="#ffffff",
                 command=apply_sepia)
Label_9.grid(row=4, column=0, sticky=N)

Label_2 = Label(RightFrame, font=('arial', 13, 'bold'), text="", padx=2, pady=2, bg="#f2ccff", fg="black")
Label_2.grid(row=5, column=0, sticky=W)

Label_9 = Button(RightFrame, font=('arial', 19, 'bold'), text="Grayscale", padx=2, pady=2, bg="#9c1ae8", fg="#ffffff",
                 command=grayscale)
Label_9.grid(row=6, column=0, sticky=N)

Label_7 = Label(RightFrame, font=('arial', 30, 'bold'), text="      ", padx=2, pady=2, bg="#f2ccff", fg="black")
Label_7.grid(row=7, column=1, sticky=W)

######################################################
Label_1 = Label(LeftFrame, font=('lato black', 37, 'bold'), text=" Select Image ", padx=2, pady=2, bg="#65a4fc",
                fg="black")
Label_1.grid(row=0, column=0, sticky=W)

Label_2 = Label(LeftFrame, font=('arial', 20, 'bold'), text="", padx=2, pady=2, bg="#ffffff", fg="black")
Label_2.grid(row=1, column=0, sticky=W)

Label_7 = Label(LeftFrame, font=('arial', 7, 'bold'), text="", padx=2, pady=2, bg="#ffffff", fg="black")
Label_7.grid(row=3, column=0, sticky=W)

Label_8 = Button(LeftFrame, font=('Arial', 18, 'bold'), text="  Choose From File  ", padx=2, pady=2, bg="#65a4fc",
                 fg="black", command=fileselector)
Label_8.grid(row=4, column=0)

Label_7 = Label(LeftFrame, font=('arial', 30, 'bold'), text="", padx=2, pady=2, bg="#ffffff", fg="black")
Label_7.grid(row=5, column=0, sticky=W)

Label_4 = Button(LeftFrame, font=('arial', 23, 'bold'), text="Show Image", padx=2, pady=2, bg="#ffffff", fg="#65a4fc",
                 command=showimage)
Label_4.grid(row=6, column=0)

Label_7 = Label(LeftFrame, font=('arial', 30, 'bold'), text="      ", padx=2, pady=2, bg="#ffffff", fg="black")
Label_7.grid(row=7, column=1, sticky=W)

root.mainloop()

