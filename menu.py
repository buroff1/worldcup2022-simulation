import tkinter as tk
from itertools import count
from sys import exit

from PIL import Image, ImageTk


def menu():
    class ImageLabel(tk.Label):
        """a label that displays images, and plays them if they are gifs"""

        def load(self, im):
            if isinstance(im, str):
                im = Image.open("pics/loading.gif")
            self.loc = 0
            self.frames = []

            try:
                for i in count(1):
                    self.frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass

            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(self.frames) == 1:
                self.config(image=self.frames[0])
            else:
                self.next_frame()

        def unload(self):
            self.config(image="")
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.loc += 1
                self.loc %= len(self.frames)
                self.config(image=self.frames[self.loc])
                self.after(self.delay, self.next_frame)

    root = tk.Tk()
    root.title("World Cup 2022 Simulation")
    # root.eval('tk::PlaceWindow . center')
    root.columnconfigure(0, minsize=1)
    root.columnconfigure(1, minsize=1)
    root.rowconfigure(0, minsize=20)
    root.configure(bg='#3B061F')
    width = 500  # Width
    height = 650  # Height

    screen_width = root.winfo_screenwidth()  # Width of the screen
    screen_height = root.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    lbl = ImageLabel(root, highlightthickness=0, highlightbackground="#3B061F", background="#3B061F")
    lbl.grid(row=0, column=0, columnspan=2, padx=4, pady=4, sticky='nsew')
    lbl.load('pics/loading.gif')

    def exit_program():
        exit()

    def close_window():
        root.destroy()

    button1 = tk.Button(root, text="Start simulation", command=close_window, height=1, width=25,
                        font=("Helvetica", 14, 'bold'), highlightthickness=0, highlightbackground='#3B061F', bd=0)
    button2 = tk.Button(root, text="Exit", command=exit_program, height=1, width=25, font=("Helvetica", 14, 'bold'),
                        highlightthickness=0, highlightbackground='#3B061F', bd=0, anchor="center")

    button1.grid(row=1, column=1, padx=130, pady=1, sticky='s', )
    button2.grid(row=2, column=1, padx=1, pady=4, sticky='s')
    root.mainloop()


if __name__ == "__main__":
    menu()