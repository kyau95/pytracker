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
        for F in (MainMenuPage, AddItemsPage, ViewItemsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(MainMenuPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class TemplatePage:
    """Template class for widgets that all Page class objects will have
    
    Widgets include:
        Title Label (tkinter.Label)
        Return Button (tkinter.Button)
    """
    def __init__(self):
        pass


class MainMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        title_lbl = tk.Label(self, text='PyTracker', font=TITLE_FONT)
        title_lbl.pack()
        buttons = [
                    tk.Button(self, text='Add/Track Item', font=DEFAULT_BTN_FONT,
                        command=lambda: controller.show_frame(AddItemsPage)),
                    tk.Button(self, text='View Tracked Items', font=DEFAULT_BTN_FONT,
                        command=lambda: controller.show_frame(ViewItemsPage)),
                    tk.Button(self, text='Quit Program', font=DEFAULT_BTN_FONT,
                        command=lambda: controller.destroy()),
                  ]
        # Customizing button look and layout
        for btn in buttons:
            btn['padx'] = 10
            btn['pady'] = 10
            btn['relief'] = tk.RIDGE
            btn.pack(pady=5)


class AddItemsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title_lbl = tk.Label(self, text='Page One!!!', font=TITLE_FONT)
        title_lbl.grid(row=0, column=0, pady=10,padx=10)
        buttons = [
                    tk.Button(self, text='Submit', font=DEFAULT_BTN_FONT,
                        command=lambda: print('Submitting')),
                    tk.Button(self, text='Return to Main Menu',
                        font=DEFAULT_BTN_FONT,
                        command=lambda: controller.show_frame(MainMenuPage))
                  ]
        for btn in buttons:
            btn.grid(pady=5)


class ViewItemsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title_lbl = tk.Label(self, text='Tracked Items', font=TITLE_FONT)
        title_lbl.grid(row=0, column=0)
        buttons = [
                    tk.Button(self, text='Submit', font=DEFAULT_BTN_FONT,
                        command=lambda: print('Submitting')),
                    tk.Button(self, text='Return to Main Menu',
                        font=DEFAULT_BTN_FONT,
                        command=lambda: controller.show_frame(MainMenuPage))
                  ]
        for btn in buttons:
            btn.grid(pady=5)


window = TrackerGUI()
window.minsize(640, 480)
window.mainloop()
