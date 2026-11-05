import cv2

def main():
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(cascade_path)
    if detector.empty():
        raise RuntimeError("Could not load OpenCV Haar cascade.")
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise RuntimeError("Could not open webcam. Check permissions or camera index.")
    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                print("Could not read from webcam.")
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (40, 220, 100), 2)
                cv2.putText(frame, "Face", (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (40, 220, 100), 2)
            cv2.imshow("OpenCV Face Detection - press q to quit", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()