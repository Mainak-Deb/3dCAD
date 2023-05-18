import stltovoxel
import numpy as np
import os
import cv2
import shutil
import tkinter as tk
from tkinter import filedialog


def loadvoxel(path,resolution=20):     
    input=path
    folder_path = os.path.dirname(path)+r"/mainaktestingfolder"
    os.mkdir(folder_path)
    output=folder_path+"/output.png"
 
    binary_array = np.zeros((resolution,resolution,resolution), dtype=bool)

    stltovoxel.convert_file(input, output, resolution-3)
    
    image_names = os.listdir(folder_path)[0:resolution]

    for i, name in enumerate(image_names):
        image = cv2.imread(os.path.join(folder_path, name), cv2.IMREAD_GRAYSCALE)
        image=cv2.resize(image,(resolution,resolution))
        binary_array[i,:,:] = (image > 0)
        # assume that white pixels represent "true"
    print(binary_array)
    shutil.rmtree(folder_path)
    return binary_array
    

def openSTL(vsize):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    print(file_path)   
    if(file_path==""):
        return None
    return loadvoxel(file_path,vsize)
 
 
def popup():
    def open_popup():
        popup = tk.Toplevel()
        popup.title("Error")
        popup.geometry("200x100")
        popup_label = tk.Label(popup, text="Are you sure you want to exit?")
        popup_label.pack(padx=20, pady=20)
    root = tk.Tk()
    root.geometry("300x200")
    popup_button = tk.Button(root, text="Open Popup", command=open_popup)
    popup_button.pack(padx=20, pady=20)
    root.mainloop()
    

 
if __name__ == '__main__':
    popup()
    #openSTL()