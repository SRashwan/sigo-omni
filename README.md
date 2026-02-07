# 📡 Sigo Omni: The Scientific Signal Processor

**Sigo Omni** is a state-of-the-art, web-based Digital Signal Processing (DSP) workstation. It visualizes the mathematics of radio frequency (RF) transmission in real-time, bridging the gap between abstract equations and physical waves using modern web technologies.

![Sigo Omni Dashboard](https://via.placeholder.com/800x400?text=Sigo+Omni+Dashboard+Preview)
*(Replace this link with a real screenshot of your app once hosted!)*

## 🚀 Features

### 1. Multi-Modal Input System
* **Text-to-Signal:** Converts ASCII text into binary FSK (Frequency Shift Keying) streams instantly.
* **Audio Processing:** Captures live microphone input or processes uploaded audio files (`.mp3`, `.wav`) for modulation.
* **Video Scanning:** Simulates SSTV (Slow Scan Television) by reading camera input and converting pixel luminance into signal voltage.
* **Hardware Interface (Web Serial):** Connects directly to an Arduino to read physical sensors or control external LEDs.

### 2. Advanced Modulation Engine
Visualizes three distinct modulation techniques with mathematically accurate equations:
* **FM (Frequency Modulation):** $s(t) = A_c \cos(2\pi f_c t + 2\pi k_f \int m(\tau) d\tau)$
* **AM (Amplitude Modulation):** $s(t) = [1 + k_a m(t)] \cos(2\pi f_c t)$
* **QAM (Quadrature Amplitude Modulation):** Displays a real-time I/Q Constellation diagram.

### 3. Scientific Visualization
* **Real-Time Scopes:** Three synchronized oscilloscopes for Input (Baseband), Output (RF Carrier), and Recovery (Demodulation).
* **RGB Oscilloscope:** Splits video signals into separate Red, Green, and Blue voltage traces.
* **Dynamic Equation Rendering:** Uses LaTeX (MathJax) to render the exact physics formula being simulated, with animated callouts explaining each term.

### 4. Data Analysis
* **CSV Recorder:** Exports the Time, Input Voltage, and Output Voltage data to a `.csv` file for further analysis in Excel, MATLAB, or Python.
* **Sonification:** "Hear" the data using a built-in audio synthesizer that converts the signal voltage into audible frequencies.

---

## 🛠️ Installation & Usage

### Option 1: Live Demo (GitHub Pages)
1.  Go to `Settings` > `Pages` in your GitHub repository.
2.  Select the `main` branch as the source.
3.  Visit the generated URL.

### Option 2: Local Deployment
Simply download the `index.html` file and open it in any modern web browser (Chrome, Edge, Firefox). No server installation required!

### Option 3: Arduino Setup (Optional)
To use the Hardware Mode:
1.  Open the Arduino IDE.
2.  Copy the code from the `Hardware Integration` section below.
3.  Upload it to your Arduino Uno/Nano/ESP32.
4.  Connect the Arduino via USB and click **"Connect Arduino"** in the web interface.

---

## 📐 The Mathematics
Sigo Omni relies on the analytic signal representation of waves.
* **Instantaneous Phase:** $\theta(t) = 2\pi f_c t + \phi(t)$
* **Instantaneous Frequency:** $f_i(t) = \frac{1}{2\pi} \frac{d\theta}{dt}$

The application solves these differential equations approx. 60 times per second to generate the visual graph.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
[MIT](https://choosealicense.com/licenses/mit/)
