import face_recognition
import cv2
import numpy as np
import csv 
import os
from datatime import datatime

video_capture = cv2.VideoCapture(0)

jobs_image = face_recognition.load_image_file("photos\job.jpeg")
jobs_encoding = face_recognition.face_encoding(jobs_image)[0]

ratan_tata_image = face_recognition.load_image_file("photos\ratan tata.jpeg")
jobs_encoding = face_recognition.face_encoding(ratan_tata_image)[0]

sadmona_image = face_recognition.load_image_file("photos\sadmona.jpeg")
jobs_encoding = face_recognition.face_encoding(jobs_image)[0]

tesla_image = face_recognition.load_image_file("photos\tesla.jpeg")
jobs_encoding = face_recognition.face_encoding(tesla_image)[0]

known_faces_names = [
    "jobs",
    "ratan tata",
    "sadmona",
    "tesla"
]

student = known_faces_names.copy()
