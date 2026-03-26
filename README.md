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
- Computer Vision (MediaPipe)
- Eye Aspect Ratio (EAR)
- Real-time video processing

to detect whether a person’s eyes are open or closed. If the eyes remain closed for a certain duration, the system triggers an alert.

---

## ⚙️ Features
- Real-time face and eye detection  
- Eye Aspect Ratio (EAR) calculation  
- Drowsiness detection based on eye closure  
- Visual alert on screen  
- Audio alert using alarm sound  
- Works with both webcam and video input  
- Streamlit-based user interface  

---

## 🛠️ Technologies Used
- Python  
- OpenCV  
- MediaPipe  
- NumPy  
- SciPy  
- Pygame  
- Streamlit  

---

## 📁 Project Structure

```
Drowsiness_Detection_AI/
│
├── main.py            # Webcam-based detection
├── video_demo.py      # Video-based detection
├── app.py             # Streamlit UI
├── alarm.wav          # Alert sound
│
├── videos/
│   └── demo.mp4       # Sample video
│
├── test.ipynb         # Development notebook
├── README.md
```


---

## 🚀 Installation & Setup

1. Clone the repository  
git clone https://github.com/your-username/drowsiness-detection.git  
cd drowsiness-detection  

2. Create virtual environment  
python -m venv venv  

3. Activate environment  

Windows:  
venv\Scripts\activate  

Mac/Linux:  
source venv/bin/activate  

4. Install dependencies  
pip install opencv-python mediapipe numpy scipy pygame streamlit  

---

## ▶️ How to Run

### Webcam Detection
python main.py  

### Video Detection
python video_demo.py  

Make sure your video is placed in:  
videos/demo.mp4  

### Streamlit UI (Recommended)
streamlit run app.py  

Then:  
- Select Webcam or Video  
- Click Start Detection  

---

## ⚙️ Implementation Method

The system captures video input from a webcam or video file and processes it frame by frame. MediaPipe Face Mesh is used to detect facial landmarks, from which eye regions are extracted. The Eye Aspect Ratio (EAR) is calculated using eye landmark coordinates to determine whether the eyes are open or closed.

If the EAR falls below a predefined threshold for a number of consecutive frames, the system identifies drowsiness. A visual alert is displayed on the screen, and an alarm sound is triggered using pygame. The system continues monitoring and resets once normal eye activity resumes.

A Streamlit-based user interface is integrated to provide an interactive platform for selecting input modes and viewing real-time results.

---

## 🧠 How It Works
1. Capture video input  
2. Detect face using MediaPipe  
3. Extract eye landmarks  
4. Calculate EAR  
5. Compare with threshold  
6. Trigger alert if drowsiness detected  

---

## 📊 Key Concept: Eye Aspect Ratio (EAR)
- High EAR → Eyes open  
- Low EAR → Eyes closed  

---

## ⚠️ Challenges Faced
- Selecting proper EAR threshold  
- Handling lighting variations  
- Real-time processing performance  
- Audio alert integration  

---

## 🚀 Future Improvements
- Add yawning detection  
- Use deep learning models  
- Mobile app deployment  
- Multi-sensor integration  

---

## 🎯 Conclusion
This project demonstrates how computer vision can be applied to detect drowsiness in real-time. It provides a simple, efficient, and practical solution for improving safety and reducing fatigue-related risks.

---

## 👨‍💻 Author
Sharika P K  
BTech CSE (AI & ML)  
VIT Bhopal University
