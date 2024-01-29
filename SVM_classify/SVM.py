import cv2
import numpy as np
from sklearn import svm
import os
import time
from flask import Flask, render_template, Response, jsonify, request
import pygame
import sys
import threading
import joblib

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

app = Flask(__name__)

eye_open_dir = r'E:\SVM_classify\data\data\normal'
eye_closed_dir = r'E:\SVM_classify\data\data\sleep'

clf = svm.SVC(C=0.1, kernel='linear')

def flip_horizontal(image):
    return cv2.flip(image, 1)

X_eye_open, y_eye_open = [], []
for filename in os.listdir(eye_open_dir):
    img = cv2.imread(os.path.join(eye_open_dir, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (80, 80))
    img_1d = img.flatten() / 255
    X_eye_open.append(img_1d)
    y_eye_open.append(1)

X_eye_closed, y_eye_closed = [], []
for filename in os.listdir(eye_closed_dir):
    img = cv2.imread(os.path.join(eye_closed_dir, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (80, 80))
    img_1d = img.flatten() / 255
    X_eye_closed.append(img_1d)
    y_eye_closed.append(0)

X = np.array(X_eye_open + X_eye_closed)
y = np.array(y_eye_open + y_eye_closed)
clf.fit(X, y)

# Save the model
joblib.dump(clf, 'svm_model125.plk')