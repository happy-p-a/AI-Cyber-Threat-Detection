# 🛡️ AI Cyber Threat Detection System

## IBM Virtual Internship Project

An AI-based Cyber Threat Detection System that uses **Machine Learning and Generative AI** to analyze network-flow data, identify different types of network traffic and cyber attacks, and provide human-readable analysis of the detected threats.

The project uses the **CIC-IDS-2017 dataset**, a **Random Forest classification model**, **Generative AI through the Groq API**, and a **Streamlit web application** for testing network-flow CSV files.

The Random Forest model performs the actual cyber-threat classification, while the Generative AI component explains the Machine Learning results and provides defensive recommendations.

---

## 📌 Project Overview

Cybersecurity systems need to identify suspicious network activity quickly and accurately. Machine Learning can help analyze large amounts of network traffic and classify different types of attacks.

In this project, network-flow data is processed and used to train a Machine Learning model.

The system can:

- Analyze network-flow data.
- Classify network traffic.
- Detect different types of cyber attacks.
- Display the number of benign and malicious flows.
- Show the distribution of detected threats.
- Display prediction results through a web interface.
- Calculate model prediction confidence.
- Generate human-readable threat analysis using Generative AI.
- Assess the potential risk level of detected threats.
- Provide defensive cybersecurity recommendations.
- Explain limitations of the Machine Learning results.

The project was developed as part of my **Project-Based Experiential Learning / Virtual Internship project**.

---

## 🎯 Project Objectives

The main objectives of this project are:

- To understand the application of Artificial Intelligence in cybersecurity.
- To understand how Machine Learning can be used for threat detection.
- To preprocess and analyze network traffic data.
- To classify benign and malicious network traffic.
- To train and evaluate a Machine Learning classification model.
- To save and reuse a trained Machine Learning model.
- To develop a web interface for cyber threat detection.
- To understand how Generative AI can assist cybersecurity analysis.
- To convert Machine Learning predictions into human-readable security analysis.
- To provide defensive recommendations based on detected threats.
- To present detection and analysis results in an understandable format.

---

# 🔄 Project Workflow

The complete workflow of the project is:

```text
                 CIC-IDS-2017 Dataset
                          │
                          ▼
                 Data Preprocessing
                          │
                          ▼
                    Data Cleaning
                          │
                          ▼
              Training Dataset Creation
                          │
                          ▼
              Feature / Label Separation
                          │
                          ▼
                   Label Encoding
                          │
                          ▼
                  Train/Test Split
                          │
                          ▼
                Random Forest Model
                          │
                          ▼
                  Model Evaluation
                          │
                          ▼
                   Save ML Model
                          │
                          ▼
               Streamlit Web Application
                          │
                          ▼
              Network Traffic Prediction
                          │
                          ▼
                 Threat Detection Results
                          │
                          ▼
              Detection Statistics & Confidence
                          │
                          ▼
                 Generative AI Analysis
                          │
                          ▼
        ┌───────────────────────────────────┐
        │ Threat Assessment                 │
        │ Evidence From Model Results       │
        │ Risk Level                        │
        │ Defensive Recommendations         │
        │ Model Limitations                 │
        └───────────────────────────────────┘
