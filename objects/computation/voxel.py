import pygame
import sys
import numpy as np
import tkinter as tk
from tkinter import filedialog
from voxelfuse.voxel_model import VoxelModel
from voxelfuse.mesh import Mesh
from voxelfuse.primitives import generateMaterials
import asyncio
import vtkplotlib as vpl
from stl.mesh import Mesh as stlMesh
import os
sys.path.append('./')

class voxel():
    def __init__(self,shape=100) -> None:
        self.shape=shape
        self.voxel_array = np.ones((self.shape, self.shape, self.shape), dtype=bool)
        
        
    def set_voxel_array(self,array):
        self.voxel_array=array
        
    def change_view(self,fromview,toview,arr):
        print(fromview+" to "+toview)
        if(fromview=="Top"):self.set_top_view(arr)
        elif(fromview=="Front"):self.set_front_view(arr)
        elif(fromview=="Bottom"):self.set_bottom_view(arr)
        elif(fromview=="Left"):self.set_left_view(arr)
        elif(fromview=="Right"):self.set_right_view(arr)
        elif(fromview=="Back"):self.set_back_view(arr)
        
        if(toview=="Top"):return self.get_top_view()
        elif(toview=="Front"):return self.get_front_view()
        elif(toview=="Bottom"):return self.get_bottom_view()  
        elif(toview=="Left"):return self.get_left_view()
        elif(toview=="Right"):return self.get_right_view()
        elif(toview=="Back"):return self.get_back_view()
                   
        
    #top view voxel oprations
    def get_top_view(self):
        arr=np.zeros((self.shape, self.shape), dtype='uint8')
        for j in range(self.shape):
            for k in range(self.shape):
                count=0
                while(count<self.shape and self.voxel_array[count][j][k]==False):
                    count+=1
                arr[j][k]=count 
        return arr            
            
    def set_top_view(self,view):
        for j in range(self.shape):
            for k in range(self.shape):
                for i in range(view[j][k]):         
                    self.voxel_array[i][j][k]=False
                for i in range(view[j][k],self.shape): 
                    if(self.voxel_array[i][j][k]==True):break;     
                    self.voxel_array[i][j][k]=True
                    
    
         
    #bottom view voxel oprations
    def get_bottom_view(self):
        arr=np.zeros((self.shape, self.shape), dtype='uint8')
        for j in range(self.shape):
            for k in range(self.shape):
                count=0
                while(count<self.shape and self.voxel_array[self.shape-count-1][j][k]==False):
                    count+=1
                
                arr[j][k]=count 
        return arr            
            
    def set_bottom_view(self,view):
        for j in range(self.shape):
            for k in range(self.shape):
                for i in range(view[j][k]):
                    self.voxel_array[self.shape-i-1][j][k]=False
                for i in range(view[j][k],self.shape): 
                    if(self.voxel_array[self.shape-i-1][j][k]==True):break;     
                    self.voxel_array[self.shape-i-1][j][k]=True
     
    #front view voxel oprations
    def get_front_view(self):
        arr=np.zeros((self.shape, self.shape), dtype='uint8')
        for i in range(self.shape):
            for k in range(self.shape):
                count=0
                while(count<self.shape and self.voxel_array[i][count][k]==False):
                    count+=1
                arr[i][k]=count
                    
        return arr
    
    def set_front_view(self,view):
        for i in range(self.shape):
            for k in range(self.shape):
                for j in range(view[i][k]):
                    self.voxel_array[i][j][k]=False
                for j in range(view[i][k],self.shape): 
                    if(self.voxel_array[i][j][k]==True):break;     
                    self.voxel_array[i][j][k]=True
        
        
    #back view voxel oprations 
    def get_back_view(self):
        print("getting back view")
        arr=np.zeros((self.shape, self.shape), dtype='uint8')
        for i in range(self.shape):
            for k in range(self.shape):
                count=0
                while(count<self.shape and self.voxel_array[i][self.shape-count-1][k]==False):
                    count+=1
                arr[i][k]=count
                    
        return arr
    
    def set_back_view(self,view):
        print("getting back view")
        for i in range(self.shape):
            for k in range(self.shape):
                for j in range(view[i][k]):
                    self.voxel_array[i][self.shape-j-1][k]=False
                for j in range(view[i][k],self.shape): 
                    if(self.voxel_array[i][self.shape-j-1][k]==True):break;     
                    self.voxel_array[i][self.shape-j-1][k]=True
                
                
    #right view voxel oprations
    def get_right_view(self):
        arr=np.zeros((self.shape, self.shape), dtype='uint8')
        for i in range(self.shape):
            for j in range(self.shape):
                count=0
                while(count<self.shape and self.voxel_array[i][j][count]==False):
                    count+=1
                arr[i][j]=count
                    
        return arr
    
    def set_right_view(self,view):
        for i in range(self.shape):
            for j in range(self.shape):
                for k in range(view[i][j]):
                    self.voxel_array[i][j][k]=False
                for k in range(view[i][j],self.shape): 
                    if(self.voxel_array[i][j][k]==True):break;     
                    self.voxel_array[i][j][k]=True
        
    #left view voxel oprations
    def get_left_view(self):
        arr=np.zeros((self.shape, self.shape), dtype='uint8')
        for i in range(self.shape):
            for j in range(self.shape):
                count=0
                while(count<self.shape and self.voxel_array[i][j][self.shape-1-count]==False):
                    count+=1
                arr[i][j]=count
                    
        return arr
    
    def set_left_view(self,view):
        for i in range(self.shape):
            for j in range(self.shape):
                for k in range(view[i][j]):
                    self.voxel_array[i][j][self.shape-1-k]=False
                for k in range(view[i][j],self.shape): 
                    if(self.voxel_array[i][j][self.shape-1-k]==True):break;     
                    self.voxel_array[i][j][self.shape-1-k]=True
        
    def filesave(self,file_path):   
        print("inside file save")    
        model = VoxelModel(self.voxel_array, generateMaterials(4))  #4 is aluminium.
        mesh = Mesh.fromVoxelModel(model)
        mesh.export(file_path+'.stl')
            
            
    def save(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        print(file_path)
        if(file_path==''):return
        self.filesave(file_path)
        
    def showvoxel(self):
        model = VoxelModel(self.voxel_array, generateMaterials(4))  #4 is aluminium.
        mesh = Mesh.fromVoxelModel(model)
        mesh.export('temp.stl')
        m = stlMesh.from_file('temp.stl')
        vpl.mesh_plot(m)
        vpl.show()
        os.remove('temp.stl')
                            
                    
    
        
        