from tkinter import *
from PIL import Image
from tkinter.font import Font
from tkinter import filedialog

#creat window
window = Tk()
window.title('Image Watermarking')
window.config(padx=20, pady=20)
window.geometry("600x400")
main_font = Font(family='Helvetica', size=32)
img_font = Font(family='Helvetica', size=24)


def watermark():
    path = entry.get()
    with Image.open(path) as im:
        im.show()

    entry.delete(0, END)


def find_file():
    file = filedialog.askopenfilename(title='Select Image', filetypes=(('Image files', '*.jpg *.png *.bmp *.gif'), ("All files", "*.*")))
    entry.insert(0, file)



main_lbl = Label(text="Drag and drop photo to add watermark.", font=main_font)
main_lbl.grid(row=0, column =0, columnspan=5)


entry_lbl = Label(text="Image: ", font=img_font)
entry_lbl.grid(row=1, column=1)
entry_lbl.grid(pady=(60, 25))

entry = Entry()
entry.grid(row=2, column=1, columnspan=2)
entry.grid(pady=(0, 20))

open_file = Button(text='Search File', command=find_file)
open_file.grid(column=0, row=2)

submit = Button(text='Watermark!', command=watermark)
submit.grid(column=1, row=4)



# canvas = Canvas(width=500, height = 500)
# canvas.create_image(500, 500)
# canvas.grid(column=1, row=1)




window.mainloop()