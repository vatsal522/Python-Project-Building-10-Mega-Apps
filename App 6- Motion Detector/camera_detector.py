# -*- coding: utf-8 -*-
"""
Created on Sun May  3 01:33:48 2020

@author: 91771
"""


import cv2
import time
from datetime import datetime
import pandas



first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])



video=cv2.VideoCapture(0) #can also take a video file as an input.

while True:
    check,frame=video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    #we apply GaussianBlur to smooth it to remove noise and increase accuracy.
    #21 21 is the parameters of gaussianblur, 0 is the standard deviation.
    
    
    
    
    if first_frame is None:
        first_frame=gray
        continue
        #basically what this does is, first_frame is getting the first image and that image is stored.
        #that image is stored to create the difference image 
        #we advance the loop to start of the loop to begin capturing the second frame.
        #first frame is kept static to pickup the background only and acts as a BASE IMAGE.
        
    
    
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1] #image to be thresholded,at what value it should be thresholded,color to values > threshold value
    #threshold method returns a tuple with 2 values
    #first item is value, used for other items
    #we use only second item for THRESH_BINARY
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)#this is to make the diff between black and white area more proper.
    
    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for obj in cnts:
        if cv2.contourArea(obj)<10000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(obj)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    
    
    status_list.append(status)
    
    
    status_list=status_list[-2:]
    
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
        
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
        
    
    cv2.imshow("WEB CAM FOOTAGE",gray)
    cv2.imshow("DELTA CALC",delta_frame)
    cv2.imshow("THRESHOLD CALC",thresh_frame)
    cv2.imshow("COLOR FRAME",frame)

   
    key=cv2.waitKey(1)
    if key==ord('q'): #stops working when keyboard interrupt Q is pressed.
        if status==1:
            times.append(datetime.now())
        break
    
    
print(status_list)
print(times)


for i in range(0,len(times),2):
    df=df.append({'Start':times[i],'End':times[i+1]},ignore_index=True)

df.to_csv('Times.csv')
video.release()    
cv2.destroyAllWindows()