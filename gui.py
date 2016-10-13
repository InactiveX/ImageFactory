#!/usr/bin/python
# -*- coding: utf-8 -*-


import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os
import string
import sys
import settings as s

import tkinter

master = tkinter.Tk()
master.title="Image copper"
tkinter.Label(master, text="Input:").grid(row=1, column=0)
tkinter.Entry(master, width =50).grid(row=0, column=1)

frame = tkinter.Frame()

frame.grid(row=15, column=0, columnspan=2, sticky='w')

frame.row=5, column=0, columnspan=2)
tkinter.Button(frame, text='Confirm').grid(row=0, column=1, sticky='w')
master.mainloop()

