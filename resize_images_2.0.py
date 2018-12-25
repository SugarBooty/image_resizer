from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image


# is called from resize button
def Resize(path):
    FILTER = Filter.get()
    DIM_X = Dim_X.get()
    DIM_Y = Dim_Y.get()
    SIZE = tuple(DIM_X, DIM_Y)
    DESTINATION_DIR = Destination_Path.get()
    Resize_Type = Mode.get()

    print(FILTER, SIZE, DESTINATION_DIR)

# Uses resize, which stretches the picture to fit the new dimensions
    if Resize_Type == "Stretch":
        Image_Orig = Image.open(path)
        Image_Mod = Image_Orig.resize(SIZE, getattr(Image, FILTER))
        Filename = os.path.basename(path)
        Save_Path = os.path.join(DESTINATION_DIR, Filename)
        Image_Mod.save(Save_Path)

# Uses fit, which fits the image and maintains its aspect ratio, cropping the middle
# This can be set to crop from other locations, the middle works for what I need it for
    if Resize_Type == "Crop":
        Image_Orig = Image.open(path)
        Image_Mod = ImageOps.fit(ImageOrig, SIZE, getattr(Image, FILTER))
        Filename = os.path.basename(path)
        Save_Path = os.path.join(DESTINATION_DIR, Filename)
        Image_Mod.save(Save_Path)

# Opens a file browser to pick the source dir
def SourceButtonDef():
    global Source_Path
    Filename = filedialog.askdirectory()
    Source_Path.set(Filename)
    Source.set(Filename)

# Opens a file browser to pick the destination dir
def DestinationPathDef():
    global Destination_Path
    Filename = filedialog.askdirectory()
    Destination_Path.set(Filename)

# Closes the window and quits the program
def CloseWindow():
    Window.destroy()
    exit()

# Initializes the window and gives it a title
Window = Tk()
Window.title("Image Resizer 2.0")

#Variable setup for TKinter
Source_Path = StringVar()
Destination_Path = StringVar()
Dim_X = IntVar()
Dim_Y = IntVar()
Mode = IntVar()
Filter = StringVar()

# Source Row -- Row 0
Label(Window, text="Source:").grid(row=0, column=0)
Source = Entry(Window, width=30, bg="White")
Source.grid(row=0, column=1)
Button(Window, text="Browse", width=6, command=SourceButtonDef).grid(row=0, column=2)

# Destination Row -- Row 1
Label(Window, text="Destination").grid(row=1, column=0)
Destination = Label(Window, textvariable=Destination_Path, width=30, bg="White")
Destination.grid(row=1, column=1)
Button(Window, text="Browse", width=6, command=DestinationPathDef).grid(row=1, column=2)

# Frame_Frame -- Encapsulates XYFrame, Mode_Frame, Resampling Frame -- Row 2
Frame_Frame = Frame(Window)
Frame_Frame.grid(row=2, column=0, columnspan=3, sticky=W)

# XYFrame 
XY_Frame = Frame(Frame_Frame)
XY_Frame.grid(row=0, column=0, columnspan=3)

# Mode_Frame
Mode_Frame = Frame(Frame_Frame)
Mode_Frame.grid(row=1, column=1, columnspan=3)

# Resampling_Frame
Resampling_Frame = Frame(Frame_Frame)
Resampling_Frame.grid(row=2, column=2, columnspan=3)

# Close_Frame Row -- Row 4
Close_Frame = Frame(Window)
Close_Frame.grid(row=4, column=0, columnspan=3)

# X Entry
Label(XY_Frame, text="X").grid(row=0, column=0)
Dim_X = Entry(XY_Frame, width=4)
Dim_X.grid(row=0, column=1)

# Y Entry
Label(XY_Frame, text="Y").grid(row=0, column=2)
Dim_Y = Entry(XY_Frame, width=4)
Dim_Y.grid(row=0, column=3)

# Mode Selection Radiobutton
Crop = Radiobutton(Mode_Frame, text="Crop", variable=Mode, value="Crop")
Crop.grid(row=0, column=0)
Stretch = Radiobutton(Mode_Frame, text="Stretch", variable=Mode, value="Stretch")
Stretch.grid(row=0, column=1)

# Resampling Filter Dropdown
Dropdown = ttk.Combobox(Resampling_Frame, textvariable=Filter)
Dropdown.grid(row=0, column=0)
Dropdown['values'] = ('NEAREST', 'BILINEAR', 'BICUBIC', 'LANCZOS')

# Quit and Resize Buttons
Button(Close_Frame, text="Quit", width=14, command=CloseWindow).grid(row=0, column=0)
Button(Close_Frame, text="Resize", width=14, command=Run).grid(row=0, column=1)

# Runs the Window
Window.mainloop()
