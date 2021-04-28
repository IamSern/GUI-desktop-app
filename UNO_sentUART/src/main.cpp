#include <Arduino.h>

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print("halo\n");
  delay(1000);
}