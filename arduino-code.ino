/*
 * SIGO OMNI - Hardware Interface Node
 * Upload this to your Arduino.
 * * 1. INPUT: Reads potentiometer/sensor on Pin A0 -> Sends to Web App.
 * 2. OUTPUT: Reads data from Web App -> Sets Brightness on Pin 3 (LED).
 */

const int PIN_SENSOR = A0; // Potentiometer or Photoresistor
const int PIN_LED = 3;     // PWM LED output

void setup() {
  Serial.begin(115200); // High speed serial
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_SENSOR, INPUT);
}

void loop() {
  // --- 1. SEND DATA TO WEB (Input Mode) ---
  // Read sensor (0-1023), map to 0-100 for stability
  int val = analogRead(PIN_SENSOR);
  int outputVal = map(val, 0, 1023, 0, 100);
  
  // Print formatted: "D:<value>"
  Serial.print("D:");
  Serial.println(outputVal);

  // --- 2. RECEIVE DATA FROM WEB (Output Mode) ---
  // If web app sends byte (0-255), set LED brightness
  if (Serial.available() > 0) {
    int incoming = Serial.read();
    analogWrite(PIN_LED, incoming);
  }

  delay(16); // ~60 FPS
}
