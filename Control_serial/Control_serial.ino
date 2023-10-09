#include <Stepper.h>  //Stepper by arduino
#define STEPS 2038

Stepper stepper(STEPS, 8, 10, 9, 11);

void setup() {
  Serial.begin(9600);  // Set the baud rate to match your Python program
  stepper.setSpeed(20);
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\r');  // Read the string until '\r' is encountered

    // Convert the received string to a float
    float receivedFloat = input.toFloat();

    // Check if the conversion was successful
    if (!isnan(receivedFloat)) {
      // Print the received float value
      if(receivedFloat > 0.6) stepper.step(-3);
      else if(receivedFloat < 0.4) stepper.step(3);
    }
  }
  
}
