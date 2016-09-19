import os
import time
from PIL import Image

while True:
	os.system("screencapture -x img.png")

	im = Image.open("img.png")
	colors = im.getcolors(im.size[0] * im.size[1])

	red = 0
	blue = 0
	green = 0
	yellow = 0

	for color in colors:
		#check for red
			#red (178)				  						#green (29)		   								#blue (59)
		if (color[1][0] >= 160 and color[1][0] <= 180) and (color[1][1] >= 20 and color[1][1] <= 40) and (color[1][2] >= 40 and color[1][2] <= 70): 
			red = 1

		#check for blue
			#red (54)				  						#green (90)		   								#blue (200)
		if (color[1][0] >= 40 and color[1][0] <= 70) and (color[1][1] >= 80 and color[1][1] <= 100) and (color[1][2] >= 190 and color[1][2] <= 210): 
			blue = 1

		#check for green
			#red (49)				  						#green (151)		   								#blue (49)
		if (color[1][0] >= 40 and color[1][0] <= 80) and (color[1][1] >= 140 and color[1][1] <= 160) and (color[1][2] >= 40 and color[1][2] <= 60): 
			green = 1

		#check for yellow
			#red (237)				  						#green (160)		   								#blue (72)
		if (color[1][0] >= 230 and color[1][0] <= 250) and (color[1][1] >= 150 and color[1][1] <= 170) and (color[1][2] >= 60 and color[1][2] <= 80): 
			yellow = 1

	score = red + blue + green + yellow

	flag = False
	if score == 4:
		flag = True

	if flag == False:
		os.system("osascript -e 'set volume 0'")
		print 'muted'
	else:
		os.system("osascript -e 'set volume 5'")
		print 'unmuted'
	time.sleep(.5)

