from PIL import Image
import os
import glob
import PySimpleGUI as sg

count = 0

layout = [[sg.Text('Source      '), sg.InputText(), sg.FolderBrowse()],
            [sg.Text('Destination'), sg.InputText(), sg.FolderBrowse()],
            [sg.Text('X'), sg.InputText(size=(25, 1)), sg.Text('Y'), sg.InputText(size=(25, 3))],
            [sg.Ok()]]

window = sg.Window('Image Resizer').Layout(layout)

event, values = window.Read()

total_files = len(glob.glob(values[0] + '/*.*'))
source = values[1]

print(total_files)

print(values[2])

def resize(location):
    try:
        img_orig = Image.open(location)
        img_mod = img_orig.resize(tuple([int(values[2]), int(values[3])]), Image.LANCZOS)
        file_list = location.split('.')
        x = len(file_list) - 1
        img_mod.save(str(source) + '/{}.'.format(count) + str(file_list[x]))
    except:
        print("Error " + filepath)


for filepath in glob.iglob(values[0] + '/*.*'):
    sg.OneLineProgressMeter('Resizing', count, total_files, 'key')  
    count = count + 1
    resize(filepath)