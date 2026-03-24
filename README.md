# 🚗 AI-Based Drowsiness Detection System

## 📌 Overview

This project is an AI-powered drowsiness detection system that monitors a person's eye activity in real-time using computer vision. It detects signs of fatigue such as prolonged eye closure and alerts the user with visual and audio warnings.

The system is designed to help prevent accidents caused by driver drowsiness and can also be used for general fatigue monitoring during long working hours.

---

## ❗ Problem Statement

Drowsiness is a major cause of road accidents and reduced productivity. Drivers and individuals often fail to recognize early signs of fatigue, which can lead to dangerous situations.

There is a need for a real-time, low-cost system that can monitor alertness and provide immediate feedback.

---

## 💡 Proposed Solution

This project uses:

* Computer Vision (MediaPipe)
* Eye Aspect Ratio (EAR)
* Real-time video processing

to detect whether a person’s eyes are open or closed. If the eyes remain closed for a certain duration, the system triggers an alert.

---

## ⚙️ Features

* ✅ Real-time face and eye detection
* ✅ Eye Aspect Ratio (EAR) calculation
* ✅ Drowsiness detection based on eye closure
* ✅ Visual alert on screen
* ✅ Audio alert using alarm sound
* ✅ Works with both webcam and video input
* ✅ Streamlit-based user interface

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* SciPy
* Pygame
* Streamlit

---

## 📁 Project Structure

```
Drowsiness_Detection_AI/
│── main.py              # Webcam-based detection
│── video_demo.py        # Video-based detection
│── app.py               # Streamlit UI
│── alarm.wav            # Alert sound
│── videos/
│     └── demo.mp4       # Sample video
│── test.ipynb           # Development notebook
│── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/drowsiness-detection.git
cd drowsiness-detection
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate environment

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

### 4. Install dependencies

```
pip install opencv-python mediapipe numpy scipy pygame streamlit
```

---

## ▶️ How to Run

### 🔹 Option 1: Webcam Detection

```
python main.py
```

---

### 🔹 Option 2: Video Detection

```
python video_demo.py
```

Make sure your video is placed in:

```
videos/demo.mp4
```

---

### 🔹 Option 3: Streamlit UI (Recommended)

```
streamlit run app.py
```

Then open the browser and:

* Select Webcam or Video
* Click **Start Detection**

---

## 🧠 How It Works

1. Video input is captured (webcam or file)
2. MediaPipe detects facial landmarks
3. Eye coordinates are extracted
4. Eye Aspect Ratio (EAR) is computed
5. If EAR < threshold for several frames:

   * Drowsiness is detected
   * Alert message + sound is triggered

---

## 📊 Key Concept: Eye Aspect Ratio (EAR)

EAR is calculated using distances between eye landmarks.

* High EAR → Eyes open
* Low EAR → Eyes closed

---

## ⚠️ Challenges Faced

* Selecting proper EAR threshold for accuracy
* Handling different lighting conditions
* Integrating real-time video with UI
* Ensuring smooth audio alert

---

## 🚀 Future Improvements

* Add yawning detection
* Use deep learning (CNN) for eye classification
* Mobile app integration
* Driver monitoring system with multiple sensors

---

## 🎯 Conclusion

This project demonstrates how computer vision can be applied to solve a real-world safety problem. It provides a simple yet effective solution for detecting drowsiness and preventing potential accidents.

---

## 👨‍💻 Author

* Sharika P k
  BTech CSE (AI & ML)
  VIT Bhopal University

---


---
