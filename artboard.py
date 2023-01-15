import time
import pygame,sys,random
from pygame.locals import *
import math
from numpy import ones,vstack
from numpy.linalg import lstsq




class artboard:
    def __init__(self,screen,positionx,positiony,width,colour):
        self.screen=screen
        self.positionx=positionx
        self.positiony=positiony
        self.width=width
        self.colour=colour
        self.box=self.width/100
        self.state=False
        self.mouseQueue=[]


    def QueueInsert(self,pos):
        if(len(self.mouseQueue)==0):
            self.mouseQueue.append(pos)
        else:
            if(pos!=self.mouseQueue[-1]):
                self.mouseQueue.append(pos)

    def QueuePop(self):
        if(len(self.mouseQueue)>0):
            return self.mouseQueue.pop(0)
        else:
            return None
        
    def drawLine(self,start,end,width):
        coordinates=[]
        start=(start[0],start[1]-(self.box*width/2))
        end=(end[0],end[1]+(self.box*width/2))
        for i in range(width):
            start=(start[0],start[1]+self.box)
            end=(end[0],end[1]+self.box)
            points = [start,end]
            x_coords, y_coords = zip(*points)
            A = vstack([x_coords,ones(len(x_coords))]).T
            m, c = lstsq(A, y_coords,rcond=None)[0]
            # print(start,end)
            # print("Line Solution is y = {m}x + {c}".format(m=m,c=c))
            
            for x in range(start[0],end[0]):
                y=m*x+c
                coordinates.append((x,y))
            #print(coordinates)
        return coordinates


    def update(self,arr):
        if(len(self.mouseQueue)==2):
            coordinates=self.drawLine(self.mouseQueue[0],self.mouseQueue[1],2)
            for i in range(len(coordinates)):
                arr[int(coordinates[i][0]/self.box)][int(coordinates[i][1]/self.box)]=True
            self.QueuePop()
            # self.QueuePop()



        # coordinates=self.drawLine((50,50),(300,300),12)
        # for i in range(len(coordinates)):
        #         arr[int(coordinates[i][0]/self.box)][int(coordinates[i][1]/self.box)]=True
        mouseX,mouseY=pygame.mouse.get_pos()



        if(mouseX>=self.positionx and mouseX<=self.positionx+self.width and mouseY>=self.positiony and mouseY<=self.positiony+self.width):
            if(pygame.mouse.get_pressed()[0]):
                #arr[int((mouseX-self.positionx)/self.box)][int((mouseY-self.positiony)/self.box)]=True
                # print("hello",int((mouseX-self.positionx)/self.box),int((mouseY-self.positiony)/self.box))
                self.QueueInsert((mouseX-self.positionx,mouseY-self.positiony))
                print(self.mouseQueue)
            elif(pygame.mouse.get_pressed()[2]):
                print("hello",int((mouseX-self.positionx)/self.box),int((mouseY-self.positiony)/self.box))
                #arr[int((mouseX-self.positionx)/self.box)][int((mouseY-self.positiony)/self.box)]=False


        #pygame.draw.rect(self.screen,self.colour,(self.positionx,self.positiony,self.width,self.width))
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if(arr[i][j]):
                    pygame.draw.rect(self.screen,(0,0,0),(self.positionx+i*self.box,self.positiony+j*self.box,self.box,self.box))
                else:
                    pygame.draw.rect(self.screen,(255,255,255),(self.positionx+i*self.box,self.positiony+j*self.box,self.box,self.box))
        

