import cv2

''' Giving so many face datas of different 
	faces and storing it in a variable.'''
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)

while True:
	_, image_webcam = capture.read()
	
	# Converting Image to grayscale.
	grayscale = cv2.cvtColor(image_webcam, cv2.COLOR_BGR2GRAY)

	# Detecting Faces.
	faces = face_cascade.detectMultiScale(grayscale, 1.1, 4)

	# Drawing A Rectangle Around the face.
	for (x, y, w, h) in faces:
		cv2.rectangle(image_webcam, (x, y), (x + w, y + h), (255, 0, 0), 2)

	# Showing the image to the screen and closing the image on a keypress.
	cv2.imshow('FACE DETECTION(Press escape key if you want to quit)', 
		image_webcam)
	
	# Breaking the loop on pressing the escape(esc) key.
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

# Releasing the video capture option.
capture.release()
