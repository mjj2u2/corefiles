import tkinter as tk
from tkinter import ttk
from tkinter import font

from tkinter.ttk import *


class EmailGui:
    def __init__(self):
        self.padx = 10
        self.pady = 6

        self.root = tk.Tk()
        self.root.title("Email Tools")
        self.root.geometry("800x600")

        self.icon = tk.PhotoImage(file="mail.png")
        self.root.iconphoto(False, self.icon)

        # main frames
        self.frame_title = tk.Frame(self.root)
        self.frame_message = ttk.LabelFrame(self.root, text="Information:")
        self.frame_options = ttk.LabelFrame(self.root, text='Column To Export:')
        self.frame_options_center = tk.Frame(self.frame_options)
        self.frame_export = tk.Frame(self.root)
        self.frame_progress = tk.Frame(self.root)
        self.frame_folder_chooser = ttk.LabelFrame(self.frame_export, text='Folder Selection:')
        self.frame_folder_execute = ttk.LabelFrame(self.frame_export, text='Program Control:')
        self.fill_default = tk.BOTH

        # add frames
        self.frame_title.pack(fill=self.fill_default, side='top', padx=self.pady, pady=0, anchor='w')
        self.frame_message.pack(fill=self.fill_default, side='top', padx=self.padx * 2, pady=self.pady * 2)
        self.frame_options.pack(fill=self.fill_default, side='top', padx=self.padx * 2, pady=self.pady * 2)
        self.frame_export.pack(fill=self.fill_default, expand=True, side='top', padx=self.padx, pady=self.pady)
        self.frame_progress.pack(fill=self.fill_default, side='top', padx=self.padx, pady=3)
        self.frame_folder_chooser.pack(fill=self.fill_default, expand=True, side='left', padx=self.padx, pady=self.pady)
        self.frame_folder_execute.pack(fill=self.fill_default, expand=True, side='right', padx=self.padx, pady=self.pady)
        self.frame_options_center.pack(side='top')
        self.font_title = font.Font(family="Arial", size=36, weight="bold")
        self.label_title = tk.Label(self.frame_title, text="Email to Excal Toolkit", font=self.font_title)
        self.label_title.pack(fill=self.fill_default, expand=True, padx=0, pady=0)

        # Add column explort options
        checkbutton_var = []
        columns = ['Date', 'From', 'To', 'Subject', 'Message']
        for choice in columns:
            checkbutton_var.append(tk.StringVar())
            self.checkbutton_columns = tk.Checkbutton(self.frame_options_center, text=choice, justify='center',
                                                      variable=checkbutton_var[-1], onvalue=choice, offvalue="")
            self.checkbutton_columns.pack(side='left')

        # Add folder choices
        checkbutton_var = []
        choices = self.get_folder_choices()
        for choice in choices:
            checkbutton_var.append(tk.StringVar())
            self.checkbutton_folders = tk.Checkbutton(self.frame_folder_chooser, text=choice, justify='left',
                                                      variable=checkbutton_var[-1], onvalue=choice, offvalue="")
            self.checkbutton_folders.pack(side='top', anchor='w')

        self.myfonts = list(font.families())

        # Add message box
        self.label_message = tk.Label(self.frame_message,
                                      text="Please Wait. \nGetting a list of all email folders under Inbox.",
                                      font=("Ariel", 15))
        self.label_message.pack(fill=tk.BOTH)

        # Add progress bar
        self.label_progress_bar = tk.Label(self.frame_progress, text="Progress:")
        self.label_progress_bar.pack(side='left', padx=self.padx, pady=self.pady)
        self.progress_bar = ttk.Progressbar(self.frame_progress, orient='horizontal', length=0, mode='indeterminate')
        self.progress_bar.pack(fill=tk.BOTH, expand=True, side='left', padx=0, pady=self.pady)
        # self.progress_bar.start(25)

        self.root.mainloop()

    def change_font(self, val):
        print(self.choice.get())
        self.font_title = font.Font(family=self.choice.get(), size=36, weight="bold")
        self.label_title.config(font=self.font_title)

    def get_folder_choices(self):
        choices = ["Green", "Yellow", "Blue", "Inbox", "Old"]
        return choices


if __name__ == "__main__":
    gui = EmailGui
    gui()
