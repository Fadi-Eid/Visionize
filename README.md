# Visionize
Face tracking systems for Cameras

Hardware: 
ESP32-Cam (A Thinker ESP32-Cam) -> CameraWebServer
Arduino Uno R3 -> Control_serial
28BYJ-48 Stepper Motor and Driver

Code: 
CameraWebServer is the folder containing the code to set up the ESP32-Cam as a web server that sends the camera data.
Vision.py is a python script that uses OpenCV and Mediapipe BlazeFace to detect the faces in the video strem of the ESP32-Cam,
the position of the face is than sent to the Arduino which is auto detected.
The Arduino Uno connected to the serial port of the PC is running the code Control_serial which is responsble of
moving the stepper motor to keep the face at the center of the frame.

