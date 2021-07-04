import datetime
import os
import tkinter
import numpy as np

from PIL import Image as Img
from PIL import ImageTk
import pytesseract
import cv2
from tkinter import *

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

specs_ori = cv2.imread('img/glass.png', -1)
cigar_ori = cv2.imread('img/cigar.png', -1)
mus_ori = cv2.imread('img/mustache.png', -1)

width, height = 800, 450
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cv2image = None
frame = None
gallery = None
filter = 0

def save():
 global cv2image, frame
 time = "img-saved/" + str(datetime.datetime.now().today()).replace(":", "-") +
".png"
 frame.save(time)
 print()
 
 def cancel():
     print()
 
 def filtering(i):
     global filter
     if filter != i:
         filter = i
         else:
         filter = 0
 
 def mail():
     import smtplib
     from email.mime.multipart import MIMEMultipart
     from email.mime.text import MIMEText
     from email.mime.base import MIMEBase
     from email import encoders
   
     fromaddr = ‘sender@email.com’
     toaddr = [‘sender@email.com’, ‘receiver@email.com’, ‘receiver2@email.com’]
     
     # instance of MIMEMultipart
     msg = MIMEMultipart()
     
     # storing the senders email address
     msg['From'] = fromaddr
     
     # storing the receivers email address
     msg['To'] = ','.join(toaddr) 
  
      storing the subject
      msg['Subject'] = "Your Magic Photo"
    
      # string to store the body of the mail
      body = "Hello,\n\nHere's your awesome magic photo from The PhotoBooth."
      
      # attach the body with the msg instance
      msg.attach(MIMEText(body, 'plain'))
      
      # open the file to be sent
      filename = 'D1G1TALArtboard4.jpg'
      attachment = open('D1G1TALArtboard4.jpg', "rb")
      
      # instance of MIMEBase and named as p
      p = MIMEBase('application', 'octet-stream')
      
      # To change the payload into encoded form
      p.set_payload((attachment).read())
      
      # encode into base64
      encoders.encode_base64(p)
      p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
      
      # attach the instance 'p' to instance 'msg'
      msg.attach(p)
      
      # creates SMTP session
      s = smtplib.SMTP('smtp.gmail.com', 587)
      
      # start TLS for security
      s.starttls()
      
      # Authentication
      s.login(fromaddr, "password")
      
      # Converts the Multipart msg into a string
      text = msg.as_string()
      
      # sending the mail
      s.sendmail(fromaddr, toaddr, text)
      
      # terminating the session
      s.quit()
    
def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
      overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
      h, w, _ = overlay.shape # Size of foreground
      rows, cols, _ = src.shape # Size of background Image
      y, x = pos[0], pos[1] # Position of foreground/overlay image
      
      for i in range(h):
          for j in range(w):
              if x + i >= rows or y + j >= cols:
                  continue
              alpha = float(overlay[i][j][3] / 255.0) # read the alpha channel
              src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
              return src
  
def load_images():
 pass

def open_gallery():
