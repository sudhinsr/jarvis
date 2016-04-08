import cv2
import datetime
import imutils
import time

class VideoCamera(object):
	def __init__(self):
		self.camera = cv2.VideoCapture(0)
		self.firstFrame = None
		self.grabbed, self.frame = self.camera.read()
		text = "Unoccupied"

		self.frame = imutils.resize(self.frame, width=500)
		self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
		self.gray = cv2.GaussianBlur(self.gray, (21, 21), 0)
		self.firstFrame=self.gray
 
    
	def __del__(self):
		self.video.release()
    
	def get_frame(self):
		self.grabbed, self.frame = self.camera.read()
		text = "Unoccupied"
 
		self.frame = imutils.resize(self.frame, width=500)
		self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
		self.gray = cv2.GaussianBlur(self.gray, (21, 21), 0)


		frameDelta = cv2.absdiff(self.firstFrame, self.gray)
		thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	 
		# dilate the thresholded image to fill in holes, then find contours
		# on thresholded image
		thresh = cv2.dilate(thresh, None, iterations=2)
		(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
	 
		# loop over the contours
		for c in cnts:
			# if the contour is too small, ignore it
			if cv2.contourArea(c) < 500:
				continue
	 
			# compute the bounding box for the contour, draw it on the frame,
			# and update the text
			(x, y, w, h) = cv2.boundingRect(c)
			cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			text = "Occupied"
			# draw the text and timestamp on the frame
		cv2.putText(self.frame, "Room Status: {}".format(text), (10, 20),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		cv2.putText(self.frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
			(10, self.frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
 



		ret, jpeg = cv2.imencode('.jpg', self.frame)
		return jpeg.tobytes()
