# 🔬 IC Verification System 

A multi-layer intelligent system for detecting counterfeit ICs using electrical testing, image-based analysis, and supply chain trust scoring with a final fusion decision engine.


## 🚀 Overview

Counterfeit ICs pose major risks in electronics systems including failure, security breaches, and performance degradation.  
This project demonstrates a **prototype-level automated IC verification pipeline** that combines multiple validation layers into a single decision system.


## 🧠 System Architecture

The system is divided into three core modules:

### ⚡ 1. Electrical Testing Layer
- Tests IC logic behavior (e.g., NAND, LM324)
- Computes a **Test Score (/100)** based on passed vs total test vectors
- Provides hardware-level validation of IC correctness

### 📷 2. Image Analysis Layer (IMAGINE)
- Simulated / OCR-based visual inspection
- Evaluates IC marking consistency and visual features
- Produces image confidence score

### 🚚 3. Supply Chain AI Layer
- Trust scoring based on known IC reliability database
- Estimates counterfeit probability using heuristic model
- Simulates supplier authenticity verification


## 🔗 Fusion Engine

All three scores are combined using a weighted model:

- Electrical Score → 45%
- Image Score → 25%
- Supply Score → 30%

Final output:

- 🧮 Fusion Score (/100)
- ✅ Verdict: AUTHENTIC / SUSPECT / FAKE
- 📊 Contribution breakdown
- 📄 Auto-generated verification report


## ⚙️ Tech Stack

- Python
- Flask (Backend API)
- HTML, CSS, JavaScript (Frontend Dashboard)
- Chart.js (Data Visualization)
- OpenCV (planned / optional for vision layer)


