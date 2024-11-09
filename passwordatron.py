import json
import sys
import os

from pathlib import Path

import tkinter as tk
from tkinter import font, messagebox
from tkinter import ttk

class App(tk.Frame):
  def __init__(self, start_app, password=None, **apps):
    self.start_app = start_app
    self.password = password
    self.apps = apps
    self.root = tk.Tk()
    self.defaultFont = font.nametofont("TkDefaultFont")
    self.defaultFont.configure(size=14)

    super().__init__(self.root)
    self.pack()

    ttk.Label(self, text=f"Enter Password for {self.start_app}").pack(pady=10, padx=10, side="top")

    self.pw = tk.Entry(self, show="*")
    self.pw.pack(pady=10, padx=10, side="top")

    self.contents = tk.StringVar()
    self.pw["textvariable"] = self.contents
    self.pw.bind('<Key-Return>', self.pw_contents)
    self.pw.focus()

    bframe = tk.Frame(self)
    bframe.pack(side="top")
    ttk.Button(bframe, text="OK", command=self.pw_contents).pack(side="left", anchor="w", pady=10, padx=10)
    ttk.Button(bframe, text="Quit", command=self.root.destroy).pack(side="left", anchor="w", pady=10, padx=10)

  def pw_contents(self, *args):
    if self.contents.get() == self.password:
      self.root.destroy()
      os.system(self.apps[self.start_app])

    else:
      self.contents.set('')
      messagebox.showerror(title="Error", message='Password is Incorrect')
      self.pw.focus()

def run():
  config_path = Path(__file__).parent / 'config.json'
  with config_path.open('r') as fh:
    options = json.load(fh)

  pwapp = App(sys.argv[1], **options)
  pwapp.master.title("Passwordatron")
  pwapp.master.maxsize(800, 400)
  pwapp.root.mainloop()


if __name__ == "__main__":
  run()
