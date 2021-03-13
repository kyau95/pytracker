"""
File:       app.py
Author:     ykevin1
Info:       File contains the GUI information for the tracker program. Aims to
            be user-friendly and intuitive to the user so that they can
            navigate the various screens easily and perform the tasks that they
            want to accomplish with ease.
"""


import tkinter as tk


TITLE_FONT = ('CaskaydiaCove Nerd Font Mono', 48)
DEFAULT_BTN_FONT = ('FiraCode Nerd Font Mono', 18)


class TrackerGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='PyTracker', font=TITLE_FONT)
        label.pack(pady=10,padx=10)

        buttons = [
                    tk.Button(self, text='Visit Page 1', font=DEFAULT_BTN_FONT,
                        command=lambda: controller.show_frame(PageOne)),
                    tk.Button(self, text='Visit Page 2', font=DEFAULT_BTN_FONT,
                        command=lambda: controller.show_frame(PageTwo))
                  ]
        # Customizing button look and layout
        for btn in buttons:
            btn['padx'] = 10
            btn['pady'] = 10
            btn['relief'] = tk.RIDGE
            btn.pack(pady=5)



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page One!!!', font=TITLE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text='Return', font=DEFAULT_BTN_FONT,
                            command=lambda: controller.show_frame(MainMenu))
        button1.pack()
        button2 = tk.Button(self, text='Page Two', font=DEFAULT_BTN_FONT,
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page Two!!!', font=TITLE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text='Return', font=DEFAULT_BTN_FONT,
                            command=lambda: controller.show_frame(MainMenu))
        button1.pack()
        button2 = tk.Button(self, text='Page One', font=DEFAULT_BTN_FONT,
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


window = TrackerGUI()
window.minsize(640, 480)
window.mainloop()
