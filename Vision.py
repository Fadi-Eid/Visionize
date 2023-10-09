import mediapipe as mp
import cv2
import serial as ser
import serial.tools.list_ports
import warnings

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description  # may need tweaking to match new arduinos
]
if not arduino_ports:
    raise IOError("No Arduino found")
if len(arduino_ports) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

ser = serial.Serial(arduino_ports[0], 9600)

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


# ESP32 URL
URL = "http://192.168.1.6"
AWB = True

# Face recognition and opencv setup
cap = cv2.VideoCapture(URL + ":81/stream")
prevTime = 0
new_x = 0.5

with mp_face_detection.FaceDetection( model_selection=1,
    min_detection_confidence=0.70) as face_detection:
  while True:
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      break


    #Convert the BGR image to RGB.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = face_detection.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)
        new_x = results.detections[0].location_data.relative_keypoints[2].x # the keypoint of the nose


    else:
        new_x = 0.50

    print(str(new_x))
    ser.write((str(new_x) + '\r').encode())

    # Uncomment to see face detection
    cv2.imshow('BlazeFace Face Detection', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()