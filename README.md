# Visionize
Face tracking system for Video Streaming and self-recording

![Visionize](https://github.com/Fadi-Eid/Visionize/assets/113466842/0a03a130-b511-49ce-b492-fc05307a56b6)


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

![image](https://github.com/Fadi-Eid/Visionize/assets/113466842/a0541b37-f395-4332-97a1-6618b427089e)

![image](https://github.com/Fadi-Eid/Visionize/assets/113466842/1c1451a7-fecb-40a4-bf84-6283d3c4bb3a)


Remove the jumper wire between GPIO0 and GND After fashing the code.
Reset the ESP32-Cam with the serial monitor open in order to get the assigned IP-Address.

To configure the video stream (Quality, resolution, contrast...) from any device connecteed to the same local network, enter on a browser the IP-Address of the ESP32-Cam (192.168.x.x)
To view the stream only type in 192.168.x.x:81/stream

Make sure to edit the SSID and Password of you local wifi in the code Control.ino and to change the IP Address of the ESP32-Cam in the Vision.py code.
