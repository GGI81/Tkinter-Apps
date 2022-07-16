from tkinter import *
from PIL import Image, ImageFilter, ImageTk

# TODO: Enter your image HERE
BOOK_IMAGE = 'book.jpg'
# --------------------

def contour():
    top = Toplevel()
    top.geometry('800x700')
    top.title('Contour')
    out = book.filter(ImageFilter.CONTOUR)
    result = ImageTk.PhotoImage(out)

    ll = Label(top, image=result)
    ll.image = result
    ll.pack()

    button_close = Button(top, text='Close Window', command=top.destroy)
    button_close.pack()


def detail():
    top = Toplevel()
    top.geometry('800x700')
    top.title('Detail')
    out = book.filter(ImageFilter.DETAIL)
    result = ImageTk.PhotoImage(out)

    ll = Label(top, image=result)
    ll.image = result
    ll.pack()

    button_close = Button(top, text='Close Window', command=top.destroy)
    button_close.pack()


def edge_enhance():
    top = Toplevel()
    top.geometry('800x700')
    top.title('Edge Enhance')
    out = book.filter(ImageFilter.EDGE_ENHANCE)
    result = ImageTk.PhotoImage(out)

    ll = Label(top, image=result)
    ll.image = result
    ll.pack()

    button_close = Button(top, text='Close Window', command=top.destroy)
    button_close.pack()


def edge_enhance_more():
    top = Toplevel()
    top.geometry('800x700')
    top.title('Contour')
    out = book.filter(ImageFilter.EDGE_ENHANCE_MORE)
    result = ImageTk.PhotoImage(out)

    ll = Label(top, image=result)
    ll.image = result
    ll.pack()

    button_close = Button(top, text='Close Window', command=top.destroy)
    button_close.pack()


def find_edges():
    top = Toplevel()
    top.geometry('800x700')
    top.title('Find Edges')
    out = book.filter(ImageFilter.FIND_EDGES)
    result = ImageTk.PhotoImage(out)

    ll = Label(top, image=result)
    ll.image = result
    ll.pack()

    button_close = Button(top, text='Close Window', command=top.destroy)
    button_close.pack()


def smooth_more():
    top = Toplevel()
    top.geometry('800x700')
    top.title('Smooth More')
    out = book.filter(ImageFilter.SMOOTH_MORE)
    result = ImageTk.PhotoImage(out)

    ll = Label(top, image=result)
    ll.image = result
    ll.pack()

    button_close = Button(top, text='Close Window', command=top.destroy)
    button_close.pack()


def sharpen():
    top = Toplevel()
    top.geometry('800x700')
    top.title('Sharpen')
    out = book.filter(ImageFilter.SHARPEN)
    result = ImageTk.PhotoImage(out)

    ll = Label(top, image=result)
    ll.image = result
    ll.pack()

    button_close = Button(top, text='Close Window', command=top.destroy)
    button_close.pack()


def blur():
    top = Toplevel()
    top.geometry('800x700')
    top.title('Blur')
    out = book.filter(ImageFilter.BLUR)
    result = ImageTk.PhotoImage(out)

    ll = Label(top, image=result)
    ll.image = result
    ll.pack()

    button_close = Button(top, text='Close Window', command=top.destroy)
    button_close.pack()


def smooth():
    top = Toplevel()
    top.geometry('800x700')
    top.title('Blur')
    out = book.filter(ImageFilter.SMOOTH)
    result = ImageTk.PhotoImage(out)

    ll = Label(top, image=result)
    ll.image = result
    ll.pack()

    button_close = Button(top, text='Close Window', command=top.destroy)
    button_close.pack()


def emboss():
    top = Toplevel()
    top.geometry('800x700')
    top.title('Blur')
    out = book.filter(ImageFilter.EMBOSS)
    result = ImageTk.PhotoImage(out)

    ll = Label(top, image=result)
    ll.image = result
    ll.pack()

    button_close = Button(top, text='Close Window', command=top.destroy)
    button_close.pack()


root = Tk()
root.geometry('800x650')
root.title('Filter Changer')

book = Image.open(BOOK_IMAGE)
out_filter = book.filter(ImageFilter.DETAIL)
result_image = ImageTk.PhotoImage(out_filter)

label = Label(image=result_image)
label.image = result_image
label.place(x=0, y=0)

button1 = Button(root, text='Change to BLUR', command=blur)
button1.grid(row=1, column=1)

button2 = Button(root, text='Change to Smooth', command=smooth)
button2.grid(row=1, column=2)

button3 = Button(root, text='Change to Emboss', command=emboss)
button3.grid(row=1, column=3)

button4 = Button(root, text='Change to Contour', command=contour)
button4.grid(row=1, column=4)

button5 = Button(root, text='Change to Detail', command=detail)
button5.grid(row=1, column=5)

button6 = Button(root, text='Change to Edge Enhance', command=edge_enhance)
button6.grid(row=2, column=1)

button7 = Button(root, text='Change to Edge Enhance More', command=edge_enhance_more)
button7.grid(row=2, column=2)

button8 = Button(root, text='Change to Find Edges', command=find_edges)
button8.grid(row=2, column=3)

button9 = Button(root, text='Change to Smooth More', command=smooth_more)
button9.grid(row=2, column=4)

button10 = Button(root, text='Change to Sharpen', command=sharpen)
button10.grid(row=2, column=5)

root.mainloop()
