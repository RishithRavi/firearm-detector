# Agression classification & firearm detection models for Live AI Hackathon

### Real-Time Threat detection using YOLO architecture w/ millisecond processing/inference speeds.

## Run this to test out locally

```
python ./live.py
```

# 💡 Inspiration

With the rise in school safety concerns, I recognized the urgent need for a **proactive, AI-powered security solution**. Traditional security measures rely on delayed responses, but **real-time detection and tracking** could significantly improve crisis response.

As someone passionate about **computer vision and AI**, I wanted to explore how existing CCTV infrastructure could be **enhanced with intelligence**, rather than just recording events passively. Schools already have cameras, but they don’t **analyze behaviors, detect threats, or trigger alerts**—which leaves a huge gap in security.

**SSS (Stopping School Shootings)** was built to close that gap. Using **computer vision**, SSS transforms ordinary surveillance cameras into an **active security system that detects potential threats and alerts authorities before an incident escalates**.

# 🔍 What it does

SSS is an **AI-powered security system** that uses **computer vision** to enhance school safety. It can:

- **Detect Unusual Movements** – Identifies erratic behavior, such as sudden running, group formations, or loitering in restricted areas.
- **Track Suspicious Activity** – Monitors individuals lingering in unusual places or carrying objects in a concerning manner.
- **Identify Threat Indicators** – Uses **object detection** to recognize potential weapons or dangerous items.
- **Identify Aggressive Actions** – Uses **object classification** to classify people as aggressive or non-aggressive based on cues such as raised fists and shoving.

By turning **passive CCTV into an active security solution**, SSS **enhances school safety without requiring costly new infrastructure**.

# 🔧 How I built it

I experimented with different **computer vision models** to determine the best approach for detecting potential threats.

### **Pose Estimation vs. Object Detection**

Initially, I explored **pose estimation** to identify aggressive stances, raised arms, or threatening postures. However:

- Pose estimation models struggled with **crowded environments** and **occlusions** (e.g., multiple students in a hallway).
- Accuracy varied depending on **camera angles and lighting conditions**.
- False positives occurred frequently, as **non-threatening gestures** (e.g., raising a hand in class) were sometimes misclassified.

After testing, I decided to **go with object detection** instead because:

- It **performs better in varied environments** and detects weapons or suspicious items directly.
- Object detection models like **YOLO and Faster R-CNN** provided **higher accuracy** in real-world settings.
- It allowed for **bounding box tracking**, making it easier to **pinpoint threats in a crowd**.

### **Development Process**

**Day 1:**

- Defined problem scope and researched school security vulnerabilities.
- Brainstormed key technologies (**Raspberry Pi, OpenCV, FastAPI, Azure**).
- Designed the initial **ML architecture**, focusing on **real-time object detection**.

**Day 2:**

- Trained an **object detection model** to recognize specific threats.
- Integrated webcam feeds to **process live video**.
- Developed a prototype for **real-time aggression classification**.

**Day 3:**

- Optimized video processing for **low-latency detection**.
- Built a user interface that shows the **live annotated threat footage**.

# ⚠️ Challenges I ran into

- **Reducing False Positives:** Ensuring that normal student activity (e.g., running in hallways) isn’t mistakenly flagged as a threat.
- **Latency Optimization:** Processing **real-time video feeds** while maintaining fast inference speeds.
- **Camera Compatibility:** Adapting the model to work across **different camera angles, resolutions, and lighting conditions**.

# 🍰 Accomplishments that I'm proud of

- Built a **working prototype** that detects, tracks, and alerts **in real-time**.
- Optimized **object detection** to work efficiently on **low-cost hardware (Raspberry Pi)**.
- Successfully integrated **live footage processing** with AI-based threat detection.

# 🧠 What I learned

- How to **compare and evaluate different AI models** for real-world security applications.
- The trade-offs between **pose estimation and object detection** for threat detection.
- How to fine-tune **computer vision models** to minimize **false positives**.
- The importance of **seamless integration** with existing security infrastructure.

# 🚀 What's next for SSS

- **Pilot Program:** Deploying SSS in select schools to **test real-world performance**.
- **Advanced AI Features:** Improving detection models to identify a broader range of **threats and objects**.
- **Law Enforcement Partnerships:** Enhancing emergency response integration for **automated dispatch**.
- **Scalability:** Expanding the system beyond schools to **public spaces, businesses, and other high-risk environments**.

### SSS isn’t just about security—it’s about **peace of mind** for students, parents, and educators.
