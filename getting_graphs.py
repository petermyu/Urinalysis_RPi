#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:34:19 2018

@author: frederikbelz
"""

#Import all relevant libraries
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import colorsys
import os
from PIL import Image
import pandas as pd

#Import relevant image filtering packages
from skimage import io
from skimage.data import camera
from skimage.filters import roberts, sobel, scharr, prewitt

def image_analysis():

	# (1) Import the file to be analyzed!
	Directory = '/home/pi/Urinalysis_Rpi/data/'
	Test_Name = 'test.png'

	Path = Directory + Test_Name
	print('path is ' + Path)
	#Collects average values from all the 
	Data = pd.DataFrame(columns=['Red Avg','Green Avg', 'Blue Avg'])
	Data1 = pd.DataFrame()
		
	img_file = Image.open(Path)


	#Creates grayscale image
	im = io.imread(Path, as_grey=True)

	#Find edges of image
	edge_roberts = roberts(im)

	#Create empty copy of image
	lines = np.zeros(shape = edge_roberts.shape)

	for y in range(0,edge_roberts.shape[0]): 
		for x in range(0,edge_roberts.shape[1]):
			if edge_roberts[y,x] > .030:
				lines[y,x] = 1
			else:
				lines[y,x] = 0


	### DETERMINE STRIP HORIZONAL LINES ###
	edges = list()
	for y in range(0,lines.shape[0]):
		for x in range(0,lines.shape[1]):
			if lines[y,x]==1 and lines[y,(x+1)]==1 and lines[y,(x-1)]==1:
				edges.append(y)
	 
	x_lines = list()           
	for y in range(0,len(edges)):
		if y not in x_lines and edges.count(y) > 50:
			x_lines.append([y,edges.count(y)])

	borders = list()      
	for x in range(0,len(x_lines)):
		if (x+1) == len(x_lines):
			break
		if x_lines[x][1] > x_lines[x+1][1]:
			borders.append(x_lines[x][0])

	if len(borders)> 2:
		for x in range(0,len(borders)):
			if borders[x+1] - borders [x] > 20:
				xborders = list([borders[x],borders[x+1]])
				break

	### DETERMINE TILE EDGES ###
	edges = list()
	for x in range(0,lines.shape[1]):
		for y in range(0,lines.shape[0]):
			if lines[y,x]==1 and lines[y+1,x]==1 and lines[y-1,x]==1:
				edges.append(x)
	 
	y_lines = list()           
	for x in range(0,len(edges)):
		if x not in y_lines and edges.count(x) > 20:
			y_lines.append([x,edges.count(x)])

	borders = list()      
	for x in range(0,len(y_lines)):
		if (x+1) == len(y_lines):
			break
		if y_lines[x][1] > y_lines[x+1][1] or (y_lines[x+1][0]-y_lines[x][0])>20:
			borders.append(y_lines[x][0])

	yborders = list()
	if len(borders)> 2:
		for x in range(0,len(borders)):
			if x+1==len(borders):
				break
			if borders[x+1] - borders [x] > 20:
				yborders.append([borders[x],borders[x+1]])

		red_avg = list()
		green_avg = list() 
		blue_avg = list()     
		for x in yborders:
			
			

				  
			#Isolates green tiles and gets their full average
			cropped = img_file.crop((x[0],xborders[0],x[1],xborders[1]))
			img = cropped.load()
			[xs,ys] = cropped.size
			red   = list()
			green = list()  
			blue  = list()    
			for xt in range(0, xs): #Uses xt & yt to avoid resetting x & y
			  for yt in range(0, ys):
				 red.append(img[xt,yt][0])
				 green.append(img[xt,yt][1])
				 blue.append(img[xt,yt][2])
			red_avg.append(np.mean(red))
			green_avg.append(np.mean(green))
			blue_avg.append(np.mean(blue))
			
			
			if np.mean(blue)<45 and np.mean(green)>135:
				#cropped.show()
				print('yes')
				a = pd.DataFrame([['No Cut',np.mean(red),np.mean(green),np.mean(blue)]],columns=['Name','Red Avg','Green Avg','Blue Avg'])
				Data = Data.append(a, ignore_index = True)
				
				
				#Increasingly isolates center of tile
				for z in range(int(min(cropped.size)/2)):
					cropped1 = img_file.crop((x[0]+z,xborders[0]+z,x[1]-z,xborders[1]-z))
					img1 = cropped1.load()
					#Isolating the center image
				
					[xs,ys] = cropped1.size
					red   = list()
					green = list()  
					blue  = list()    
					for x1 in range(0, xs):
					  for y1 in range(0, ys):
						 red.append(img1[x1,y1][0])
						 green.append(img1[x1,y1][1])
						 blue.append(img1[x1,y1][2])
					red_avg.append(np.mean(red))
					green_avg.append(np.mean(green))
					blue_avg.append(np.mean(blue))
					
					if np.mean(red)<130 and np.mean(blue)<45 and np.mean(green)>135:
						#cropped1.show()
						a = pd.DataFrame([[[xs,ys],np.mean(red),np.mean(green),np.mean(blue)]],columns=['Name','Red Avg','Green Avg','Blue Avg'])
						Data1 = Data1.append(a, ignore_index = True)


	#a = pd.DataFrame([red_avg,green_avg,blue_avg]).T
	#a.columns = ['Red Avg','Green Avg', 'Blue Avg']

	#Data = Data.append(a, ignore_index = True)
	print('Data:' )
	print(Data)
		#save = Folder + str(path)[58:]
		#img_file.save(save)

#	gs = gridspec.GridSpec(3,1)
#	plt.figure(figsize=(12,12))
#	ax = plt.subplot(gs[0,0])
#	plt.plot([x[1] for x in Data1['Name']],Data1['Red Avg'], color='red')
#	plt.xlabel('Smallest Dimesion (pixel)')
#	plt.ylabel('Red Intensity')
#	plt.title('Trial ' + Test_Name[5] + ' - ' + Test_Name[9:-4] + ' mg/L - Red Avg')


#	ax = plt.subplot(gs[1,0])
#	plt.plot([x[1] for x in Data1['Name']],Data1['Blue Avg'], color='blue')
#	plt.xlabel('Smallest Dimesion (pixel)')
#	plt.ylabel('Blue Intensity')
#	plt.title('Trial ' + Test_Name[5] + ' - ' + Test_Name[9:-4] + ' mg/L - Blue Avg')


#	ax = plt.subplot(gs[2,0])
#	plt.plot([x[1] for x in Data1['Name']],Data1['Green Avg'], color='green')
#	plt.xlabel('Smallest Dimesion (pixel)')
#	plt.ylabel('Green Intensity')
#	plt.title('Trial ' + Test_Name[5] + ' - ' + Test_Name[9:-4] + ' mg/L - Green Avg')
#
#	plt.tight_layout()
#	plt.savefig(Path[:-4] + 'Graph.png')

#	plt.clf()

	#Red Pixel Average
	Red    = Data

	#Albumin & Red Channel Output
	Red  = round(Data['Red Avg'][0],2)
	Albu = round(Data['Red Avg'][0]*(-.0666) + 153.73, 2)

	return Red;


	##From previously relevant code ###
	#edge_roberts = roberts(im)

	#fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True,
	#                       figsize=(8, 4))

	#ax[0].imshow(edge_roberts, cmap=plt.cm.gray)
	#ax[0].set_title('Roberts Edge Detection')

	#for a in ax:
	#    a.axis('off')

	#plt.show()


