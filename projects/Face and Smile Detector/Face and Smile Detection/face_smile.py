import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# Capturing Video
capture = cv2.VideoCapture(0)

while True:
	ret, image_webcam = capture.read()
	grayscale = cv2.cvtColor(image_webcam, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
		grayscale,
		scaleFactor = 1.3,
		minNeighbors = 5,
		minSize =(30, 30)
		)

	for (x, y, w, h) in faces:
		cv2.rectangle(image_webcam, (x,y), (x + w, y + h), (0, 255, 0), 2)
		roi_gray = grayscale[y:y + h, x:x + w]

		smile = smileCascade.detectMultiScale(
		roi_gray,
		scaleFactor = 1.5,
		minNeighbors = 15,
		minSize =(25, 25)
		)

		for i in smile:
			if len(smile) > 1:
				cv2.putText(image_webcam, "SMILING", (x, y - 30),
					cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 250), 3, cv2.LINE_AA)

	cv2.imshow('FACE AND SMILE(press ESC to quit)', image_webcam)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

capture.release()
