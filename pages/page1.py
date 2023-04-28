import pygame
from pygame.locals import *

import sys
import  asyncio
sys.path.append('./')
import numpy as np
import objects




def page1(screen,screenlengthx,screenlengthy): 
    
    voxelsize=40
    
    voxel=objects.computation.voxel( voxelsize)
    
    
    toolbar=objects.components.toolbar(screen,(0,0),screenlengthx,35,color=(241, 246, 249))
    viewbar=objects.components.viewbar(screen,(0,35),screenlengthx,95,color=(250, 205, 248),sliderval=voxelsize)
    drawingbox=objects.components.drawingboard(screen,(50,129),size=600,axis_density= voxelsize,color=( 255,255,255)) 
    
    sidebar=objects.components.sidebar(screen,(650,129),150,600,color=(253, 244, 245))
     
    sidetext=objects.components.textbox(screen,(0,129,50,600),color=(255, 238, 179),text_size=40,text_color=(158, 111, 33),rotation=90)
    
    #value texts will appear here
    widthValueText=objects.components.textbox(screen,(660,490,130,40),color=(228, 220, 207),text_size=30,text_color=(158, 111, 33))
    widthValue=objects.components.textbox(screen,(660,530,130,40),color=(249, 245, 235),text_size=30,text_color=(158, 111, 33))
    
    depthValueText=objects.components.textbox(screen,(660,590,130,40),color=(228, 220, 207),text_size=30,text_color=(158, 111, 33))
    depthValue=objects.components.textbox(screen,(660,630,130,40),color=(249, 245, 235),text_size=30,text_color=(158, 111, 33))
    
    drawingbox.set_array(voxel.get_top_view())
    previous_view="Top"
    isSaved=False
    
    toolbar_state=dict()
    
    
    running=True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            objects.components.updater.update(event)
        objects.components.updater.draw()
        sidetext.draw(sidebar.get_selected()+" view")
        
        widthValueText.draw("WIDTH")
        widthValue.draw(str(viewbar.get_value(slider=1)))
        depthValueText.draw("DEPTH")
        depthValue.draw(str(viewbar.get_value(slider=2)))
        
        drawingbox.set_width(viewbar.get_value(slider=1)) 
        drawingbox.set_state(viewbar.get_operation())  
        drawingbox.set_depth(viewbar.get_value(slider=2))
        drawingbox.set_grid(viewbar.get_grid())
        pygame.draw.line(screen,(61, 18, 18),(50,129),(50,screenlengthy),1)
        
        if(previous_view!=sidebar.get_selected()):
            #print("true",previous_view,sidebar.get_selected())
            viewarr=voxel.change_view(previous_view,sidebar.get_selected(),drawingbox.get_array())
            drawingbox.set_array(viewarr)
            previous_view=sidebar.get_selected()
            
        if(toolbar.get_state("save")):
            isSaved=True
            viewarr=voxel.change_view(sidebar.get_selected(),sidebar.get_selected(),drawingbox.get_array())
            voxel.save()
        elif(toolbar.get_state("open")):
            opended_voxel=objects.computation.openSTL(voxelsize)
            if  isinstance(opended_voxel, np.ndarray):
                voxel.set_voxel_array(opended_voxel)
                drawingbox.set_array(voxel.get_top_view())
                previous_view="Top"
                sidebar.set_selected("Top")
                sidetext.draw(sidebar.get_selected()+" view")
        elif(toolbar.get_state("show")):
            viewarr=voxel.change_view(sidebar.get_selected(),sidebar.get_selected(),drawingbox.get_array())
            voxel.showvoxel()    
        elif(toolbar.get_state("new")):
            voxel.set_voxel_array(np.ones((voxelsize,voxelsize,voxelsize), dtype=bool))
            drawingbox.set_array(voxel.get_top_view())
            previous_view="Top"
            sidebar.set_selected("Top")
            sidetext.draw(sidebar.get_selected()+" view")
        pygame.display.update()
                        
