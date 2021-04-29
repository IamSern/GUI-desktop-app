#include <Arduino.h>

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print("halo\n");
  Serial.print("dang test serial python\n");
  delay(1000);
}