from django.conf import settings
import numpy as np
import cv2

def detect_face(path):
   img = cv2.imread(path, 1)
   if (type(img) is np.ndarray):
       print(img.shape)
       resize_needed = False
       if img.shape[1] > 640:
            resize_needed = True
            new_w = img.shape[1] * (640.0 / img.shape[1]) # 1280 * (640/1280) = 1280 * 0.5
            new_h = img.shape[0] * (640.0 / img.shape[1])
       elif img.shape[0] > 480:
            resize_needed = True
            new_w = img.shape[1] * (480.0 / img.shape[0])
            new_h = img.shape[0] * (480.0 / img.shape[0])

       if resize_needed == True:
            img = cv2.resize(img, (int(new_w), int(new_h)))

       # Haar Cascade Classifier
       baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
       face_cascade = cv2.CascadeClassifier(baseUrl+'haarcascade_frontalface_default.xml')
       eye_cascade = cv2.CascadeClassifier(baseUrl+'haarcascade_eye.xml')
       gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray, 1.3, 5)
       for (x, y, w, h) in faces:
           cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = img[y:y+h, x:x+w]
           eyes = eye_cascade.detectMultiScale(roi_gray)
           for (ex, ey, ew, eh) in eyes:
               cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
       cv2.imwrite(path, img)
   else:
       print('Error occurred during face detection')
       print(path) 