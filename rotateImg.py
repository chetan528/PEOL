# Here is an example which rotates an image using Python3:

import tkinter as tk
from PIL import ImageTk
from PIL import Image

class SimpleApp(object):
    angle = 0
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.update = self.draw().__next__
        master.after(100, self.update)

    def draw(self):
        image = Image.open(self.filename)
        resized_image = image.resize((500, 800), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)


        while(1):
            tkimage = ImageTk.PhotoImage(resized_image.rotate(self.angle))
            canvas_obj = self.canvas.create_image(
                250, 250, image=tkimage)
            self.master.after_idle(self.update)
            yield
            self.canvas.bind(canvas_obj)
            print("rotating")
            self.angle += 10
            self.angle %= 360

root = tk.Tk()
app = SimpleApp(root, '0001.jpg')
root.mainloop()