from tkinter import *
from PIL import Image
from tkinter.font import Font
from tkinter import filedialog
from tkinter import messagebox

#create window
window = Tk()
window.title('Image Watermarking')
window.config(padx=20, pady=50)
window.geometry("500x400")
main_font = Font(family='Helvetica', size=32)
img_font = Font(family='Helvetica', size=24)


def watermark():
    path = entry.get()
    if len(path) == 0:
        messagebox.showinfo(message="Please select path to image!")
    else:
        base_image = Image.open(path)
        watermark = Image.open("./watermark image/watermark_test.png")
        size = (300, 300)
        watermark = watermark.resize(size)

        x = base_image.width - watermark.width
        y = base_image.height - watermark.height
        base_image.paste(watermark, (x, y), watermark)

        desktop_path = "/Users/joshrhodes/Desktop/"
        base_image.save(desktop_path + "watermarked_img.png")

        entry.delete(0, END)
        window.destroy()


def find_file():
    file = filedialog.askopenfilename(title='Select Image', filetypes=(('Image files', '*.jpg *.png *.bmp *.gif'), ("All files", "*.*")))
    entry.insert(0, file)



main_lbl = Label(text="Click Search File to find image.", font=main_font)
main_lbl.grid(row=0, column =0, columnspan=3)
main_lbl.grid( pady=(0, 60))

entry = Entry()
entry.grid(row=2, column=1, columnspan=2)
entry.config(width=35)


open_file = Button(text='Search File', command=find_file)
open_file.grid(column=0, row=2)


submit = Button(text='Watermark!', command=watermark)
submit.grid(column=1, row=3)
submit.grid(pady=(50, 0))


window.mainloop()