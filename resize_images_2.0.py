from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image

def Resize(path):
    FILTER = {var}
    SIZE = {var}
    DESTINATION_DIR = [var]

    if Resize_Type == "Stretch":
        Image_Orig = Image.open(path)
        Image_Mod = Image_Orig.resize(SIZE, getattr(Image, FILTER))
        Filename = os.path.basename(path)
        Save_Path = os.path.join(DESTINATION_DIR, Filename)
        Image_Mod.save(Save_Path)

    if Resize_Type == "Crop":
        Image_Orig = Image.open(path)
        Image_Mod = ImageOps.fit(ImageOrig, SIZE, getattr(Image, FILTER))
        Filename = os.path.basename(path)
        Save_Path = os.path.join(DESTINATION_DIR, Filename)
        Image_Mod.save(Save_Path)

def SourceButtonDef():
    global Source_Path
    Filename = filedialog.askdirectory()
    Source_Path.set(Filename)

def DestinationPathDef():
    global Destination_Path
    Filename = filedialog.askdirectory()
    Destination_Path.set(Filename)

def CloseWindow():
    Window.destroy()
    exit()

Window = Tk()
Window.title("Image Resizer 2.0")

Source_Path = StringVar()
Destination_Path = StringVar()
Dim_X = IntVar()
Dim_Y = IntVar()
Mode = IntVar()
Filter = StringVar()

#Source Row -- Row 0
Label(Window, text="Source:").grid(row=0, column=0)
Source = Label(Window, textvariable=Source_Path, width=30, bg="White")
Source.grid(row=0, column=1)
Button(Window, text="Browse", width=6, command=SourceButtonDef).grid(row=0, column=2)

#Destination Row -- Row 1
Label(Window, text="Destination").grid(row=1, column=0)
Destination = Label(Window, textvariable=Destination_Path, width=30, bg="White")
Destination.grid(row=1, column=1)
Button(Window, text="Browse", width=6, command=DestinationPathDef).grid(row=1, column=2)

#Frame_Frame -- Encapsulates the others -- Row 2
Frame_Frame = Frame(Window)
Frame_Frame.grid(row=2, column=0, columnspan=3, sticky=W)

#XYFrame Row -- Row 2
XY_Frame = Frame(Frame_Frame)
XY_Frame.grid(row=0, column=0, columnspan=3)

#Mode_Frame Row -- Row 3
Mode_Frame = Frame(Frame_Frame)
Mode_Frame.grid(row=1, column=1, columnspan=3)

#Resampling_Frame Row -- Row 4
Resampling_Frame = Frame(Frame_Frame)
Resampling_Frame.grid(row=2, column=2, columnspan=3)

#Close_Frame Row
Close_Frame = Frame(Window)
Close_Frame.grid(row=4, column=0, columnspan=3)

Label(XY_Frame, text="X").grid(row=0, column=0)
Dim_X = Entry(XY_Frame, width=4)
Dim_X.grid(row=0, column=1)

Label(XY_Frame, text="Y").grid(row=0, column=2)
Dim_Y = Entry(XY_Frame, width=4)
Dim_Y.grid(row=0, column=3)

Crop = Radiobutton(Mode_Frame, text="Crop", variable=Mode, value="Crop")
Crop.grid(row=0, column=0)
Stretch = Radiobutton(Mode_Frame, text="Stretch", variable=Mode, value="Stretch")
Stretch.grid(row=0, column=1)

Dropdown = ttk.Combobox(Resampling_Frame, textvariable=Filter)
Dropdown.grid(row=0, column=0)
Dropdown['values'] = ('NEAREST', 'BILINEAR', 'BICUBIC', 'LANCZOS')


Button(Close_Frame, text="Quit", width=14, command=CloseWindow).grid(row=0, column=0)
Button(Close_Frame, text="Resize", width=14).grid(row=0, column=1)


Window.mainloop()

