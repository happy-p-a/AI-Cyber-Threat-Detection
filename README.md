# 🛡️ AI Cyber Threat Detection System

## IBM Virtual Internship Project

An AI-based Cyber Threat Detection System that uses Machine Learning to analyze network-flow data and identify different types of network traffic and cyber attacks.

The project uses the **CIC-IDS-2017 dataset**, a Random Forest classification model, and a **Streamlit web application** for testing network-flow CSV files.

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
- Provide prediction results through a web interface.

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
- To develop a simple web interface for cyber threat detection.
- To present detection results in an understandable format.

---

## 🔄 Project Workflow

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


🔍 How the System Works

The project works in the following steps:

1. Dataset Collection

The project uses the CIC-IDS-2017 network traffic dataset.

The dataset contains network-flow information representing both normal and malicious network activity.

2. Data Preprocessing

The raw CSV files are processed using Python and Pandas.

The preprocessing stage includes:

Reading the CSV files.
Combining the required data.
Cleaning the data.
Handling invalid values.
Handling missing values.
Preparing the dataset for Machine Learning.
3. Training Dataset Creation

A training dataset is created from the processed network-flow data.

The current training dataset contains approximately:

299,991 rows and 79 columns

The 79 columns consist of:

78 network-flow features
1 target label
4. Feature and Label Separation

The Label column is separated from the network-flow features.

The Machine Learning model uses:

78 features

to predict the traffic category.

5. Label Encoding

The textual attack labels are converted into numerical values using LabelEncoder.

6. Train/Test Split

The dataset is divided into training and testing data.

The current project uses:

80% Training Data
20% Testing Data
7. Random Forest Training

A Random Forest Classifier is trained using the prepared network-flow data.

Random Forest was selected because it works well with tabular datasets and can handle a large number of numerical features.

8. Model Evaluation

The trained model is evaluated using:

Accuracy
Precision
Recall
F1-score
Classification Report
9. Model Saving

The trained model and label encoder are saved using Joblib.

models/
├── cyber_threat_model.pkl
└── label_encoder.pkl
10. Streamlit Application

The saved model is loaded by the Streamlit web application.

The user can upload a network-flow CSV file.

The application then:

Reads the uploaded CSV.
Removes the Label column if it is present.
Checks the required 78 features.
Sends the data to the trained Random Forest model.
Generates predictions.
Counts benign and threat flows.
Displays the detected threat distribution.
Displays prediction results.
🧠 Machine Learning Model
Model Used

Random Forest Classifier

The model uses:

78 network-flow features
14 traffic/attack classes

The original training data contained 15 labels. However, Heartbleed had only 1 sample in the selected training dataset.

Because at least two samples are required for the stratified train/test split, the Heartbleed class was removed during model training.

Therefore, the final model contains 14 classes.

🏷️ Supported Classes

The current trained model can classify the following 14 classes:

BENIGN
Bot
DDoS
DoS GoldenEye
DoS Hulk
DoS Slowhttptest
DoS slowloris
FTP-Patator
Infiltration
PortScan
SSH-Patator
Web Attack - Brute Force
Web Attack - Sql Injection
Web Attack - XSS
📊 Model Performance

On the current train/test split, the Random Forest model achieved:

Accuracy

99.68%

The model performed particularly well on several classes such as:

BENIGN
DDoS
DoS Hulk
PortScan
FTP-Patator
DoS GoldenEye

However, some attack categories contain very few training examples.

For example:

Infiltration had only a few samples.
Web Attack - Sql Injection had very few samples.
Some other attack classes were also highly imbalanced.

Because of this class imbalance, the model does not perform equally well on every individual class.

Therefore, the 99.68% accuracy is specific to the current dataset and train/test split and should not be interpreted as a guarantee of real-world cybersecurity detection performance.

🖥️ Web Application

The project includes a Streamlit-based web application.

The application provides a simple interface for uploading network-flow CSV files and running threat detection.

Main Features
📂 Upload network-flow CSV files
📊 Display dataset information
🔍 Check the number of features
🤖 Run the trained Random Forest model
🟢 Count benign network flows
🚨 Count detected threats
📈 Display threat distribution
📋 Display prediction results
⚡ Process large network-flow datasets
Example

After uploading a dataset, the application displays information such as:

Total Flows: 225,745


Benign: 97,672


Threats: 128,073

It also provides a distribution of the predicted traffic categories and prediction results.

🛠️ Technologies Used
Programming Language
Python
Machine Learning
Scikit-learn
Random Forest Classifier
Label Encoding
Train/Test Split
Classification Report
Data Processing
Pandas
NumPy
Model Storage
Joblib
Web Application
Streamlit
Visualization
Matplotlib
Plotly
Dataset
CIC-IDS-2017
📁 Project Structure
AI-Cyber-Threat-Detection/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── preprocess.py
│   ├── create_training_data.py
│   ├── train_model.py
│   └── test_environment.py
│
├── models/
│   ├── cyber_threat_model.pkl
│   └── label_encoder.pkl
│
└── data/
    └── README.md

📄 Important Files
app.py

The main Streamlit web application.

It loads the trained model and provides the user interface for uploading network-flow CSV files and detecting threats.

src/preprocess.py

Processes and cleans the original CIC-IDS-2017 CSV files.

src/create_training_data.py

Creates the smaller training dataset used for Machine Learning.

This was done to make model training more practical on a system with limited RAM.

src/train_model.py

Trains the Random Forest model and evaluates its performance.

It also saves the trained model and label encoder.

models/cyber_threat_model.pkl

The trained Random Forest Machine Learning model.

models/label_encoder.pkl

The label encoder used to convert between numerical class values and attack names.

requirements.txt

Contains the Python packages required to run the project.

