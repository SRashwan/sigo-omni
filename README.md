# 📡 Sigo Omni: Hybrid Signal Processing Workstation

**Sigo Omni** is a professional-grade, web-based Digital Signal Processing (DSP) laboratory. It visualizes the physics of Radio Frequency (RF) modulation in real-time and bridges the gap between the browser and the physical world using a hybrid architecture.


## 🚀 Key Features

### 1. Hybrid Input System
* **Text-to-Signal:** Converts ASCII text into binary FSK streams instantly.
* **Audio Intelligence:** Processes live microphone input or uploaded `.mp3`/`.wav` files.
* **Computer Vision:** Simulates SSTV (Slow Scan TV) by converting camera video into RGB voltage signals.
* **Hardware Connectivity:**
    * **Web Serial API:** Direct USB connection to Arduino (Chrome/Edge).
    * **Python Bridge:** A standalone `.exe` bridge for universal browser support (Firefox/Safari) and legacy support.

### 2. Multi-Modulation Engine
Visualizes complex modulation schemes with dynamic, scientifically accurate equations:
* **FM (Frequency Modulation):** $s(t) = A_c \cos(2\pi f_c t + 2\pi k_f \int m(\tau) d\tau)$
* **AM (Amplitude Modulation):** $s(t) = [1 + k_a m(t)] \cos(2\pi f_c t)$
* **QAM (Quadrature Amplitude Modulation):** Renders a real-time I/Q Constellation diagram.

### 3. Scientific Visualization & Analysis
* **Real-Time Oscilloscopes:** Three synchronized scopes for Baseband, RF Carrier, and Demodulated output.
* **RGB Vector Scope:** Splits video signals into separate Red, Green, and Blue voltage traces.
* **Data Recorder:** Exports high-resolution time-series data to `.csv` for analysis in MATLAB, Python, or Excel.
* **Dynamic Math:** Renders LaTeX equations in real-time with animated callouts explaining physical terms.

---

## 🛠️ Installation & Usage

### Option 1: The Web App (Standard)
1.  Download `index.html`.
2.  Open it in any modern browser (Chrome, Edge, Firefox).
3.  Start modulating text, audio, or video immediately.

### Option 2: Hardware Integration (Arduino)
To use real-world sensors as signal inputs:

1.  **Flash the Arduino:**
    * Open `sigo_arduino.ino` (code provided below).
    * Upload it to your Arduino Uno, Nano, or ESP32.
2.  **Connect:**
    * **Method A (Chrome/Edge):** Click "Web Serial" in the app and select your COM port.
    * **Method B (Universal):** Run the `sigo_bridge.exe` (instructions below) and click "EXE Bridge" in the app.

---

## 🔌 Hardware Setup

### Arduino Code (`sigo_arduino.ino`)
Upload this to your board to enable communication.
```cpp
const int PIN_SENSOR = A0; 
void setup() { Serial.begin(115200); }
void loop() {
  int val = map(analogRead(PIN_SENSOR), 0, 1023, 0, 100);
  Serial.print("D:"); Serial.println(val);
  delay(16);
}
