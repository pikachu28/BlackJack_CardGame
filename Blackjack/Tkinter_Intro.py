#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:29:13 2020

@author: anjalisingh
"""

try:
    import tkinter 

except ImportError:      # Python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)


# To test if tkinter is installed correctly or not
# tkinter._test()

# Creating Tkinter Window
mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
# Window Size: 640x480
mainWindow.geometry('640x480')

# Adding to more pixel to any direction you want for shift the frame, here it is 640x480+ x axis + y axis
# 800 shift in X axis and 400 shift in Y axis
mainWindow.geometry('640x480+800+400')
# label = tkinter.Label(mainWindow, text="Hello World!")
# # side = to choose the direction of the title
# label.pack(side = 'top')

# # CANVAS
# canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth= 1)
# canvas.pack(side='left')
# # to cover the whole left frame
# canvas.pack(side='left', fill=tkinter.Y)
# # To cover whole X axis
# canvas.pack(side='left', fill=tkinter.X, expand=True)

# canvas.pack(side='top', fill=tkinter.Y)

# canvas.pack(fill=tkinter.BOTH, expand=True)

# # BUTTONS

# canvas.pack(side='left')
# button1 = tkinter.Button(mainWindow, text='Button1')
# button2 = tkinter.Button(mainWindow, text="Button2")
# button3 = tkinter.Button(mainWindow, text='Button3')

# button1.pack(side='left')
# button2.pack(side='left')
# button3.pack(side='left')
# # Anchor Attributes: to align text/button
#     # NW
#     # N
#     # NE
#     # W
#     # CENTER
#     # E
#     # SW
#     # S
#     # SE
# button1.pack(side='left', anchor='n')
# button2.pack(side='left', anchor='s')
# button3.pack(side='left', anchor='e')

# COMMENT the above from line 30
# Dividing Window into LeftFrame and RightFrame

label = tkinter.Label(mainWindow, text='Hello Window')
# label.pack(side='top')
leftFrame = tkinter.Frame(mainWindow)
#leftFrame.pack(side='left',anchor='n', fill=tkinter.Y, expand=False)
# The relief style of a widget refers to certain simulated 3-D effects around the outside of the widget.
# # Widget in this case is canvas
# Here is list of possible constants which can be used for relief attribute.
    # FLAT
    # RAISED
    # SUNKEN
    # GROOVE
    # RIDGE
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='right', anchor='n', expand=True)

# Arranging the buttons in right Frame
button1 = tkinter.Button(rightFrame, text="button1")
button1 = tkinter.Button(rightFrame, text="button2")
button1 = tkinter.Button(rightFrame, text="button3")

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
# button1.pack(side='top')
# button2.pack(side='top')
# button3.pack(side='top')


# Changing every pack to grid:
# Output will be same
# Note:
    # Comment all the pack before using grid
label.grid(row=0, column = 0)
leftFrame.grid(row=1, column=0)
canvas.grid(row=1, column=0)
rightFrame.grid(row=1, column=2)
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# Configure the column
mainWindow.columnconfigure(0, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
rightFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')




# To see the output
mainWindow.mainloop()


