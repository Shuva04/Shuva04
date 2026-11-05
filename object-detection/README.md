# Real-Time Face Detection with OpenCV

A beginner-friendly webcam face-detection demo using OpenCV's pre-trained Haar cascade classifier.

## Requirements
Python 3.9+ and a webcam.

## Setup
```bash
python -m venv .venv
# Activate the environment, then:
pip install -r requirements.txt
python face_detection.py
```
Press **q** to quit. If the camera does not open, try changing camera index 0 to 1.

## Limitations
This detects face-like patterns; it does not identify people or determine identity. Accuracy depends on lighting, camera quality and pose.

## Suggested caption
Built a real-time face-detection demo using Python and OpenCV, applying a Haar cascade classifier to webcam frames with live bounding boxes.