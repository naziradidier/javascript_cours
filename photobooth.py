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
  
 
 
