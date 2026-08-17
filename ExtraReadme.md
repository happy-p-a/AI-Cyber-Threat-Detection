📂 Dataset

This project uses the:

CIC-IDS-2017 Dataset

The original dataset contains network traffic collected for different types of normal and malicious activity.
Due to the large size of the original dataset and the limited hardware used during development, a smaller training dataset was created for model training.
The original dataset files are not included in this GitHub repository.
Users should obtain the dataset from its official source and place the required CSV files in the appropriate data/ directory.

⚠️ Important Limitations

This project is an educational Machine Learning project and is not intended to be used as a production cybersecurity system.

Some important limitations are:

The model is trained using the CIC-IDS-2017 dataset.
Real-world network traffic can be different from the training dataset.
The dataset contains significant class imbalance.
Some attack categories have very few examples.
The reported accuracy depends on the selected train/test split.
The system works with network-flow features rather than raw packet inspection.
The model should not be considered a replacement for professional Intrusion Detection Systems.
🔐 Security Note

The application is designed for educational and demonstration purposes.

Uploaded network-flow files should only be used when the user has permission to analyze the data.

Do not upload confidential or sensitive network information to an untrusted deployment of the application.

🚀 Future Improvements

The project can be improved in several ways in the future:

Use a larger and more balanced training dataset.
Improve detection of rare attack classes.
Compare Random Forest with other Machine Learning algorithms.
Add real-time network monitoring.
Add live packet/flow analysis.
Add confusion matrix visualization.
Add precision, recall and F1-score charts.
Add an alert system for detected threats.
Add database storage for detection history.
Add user authentication.
Deploy the application online.
Improve model validation using additional datasets.
Add explainable AI features to show why a flow was classified as a threat.
📈 Future Scope

The system can potentially be extended into a more complete AI-based Intrusion Detection System.

A future version could continuously monitor network traffic, process network flows in real time, detect suspicious activity, and generate alerts for security administrators.

The project can also be extended by combining Machine Learning with other cybersecurity techniques such as anomaly detection and behavioral analysis.

👨‍💻 Project Author

Pranav Arora

B.Tech Computer Science Engineering

Project-Based Experiential Learning / Virtual Internship Project

📜 Disclaimer

This project was developed for educational and academic purposes.

The Machine Learning results shown in this repository are based on the CIC-IDS-2017 dataset and the specific training/testing methodology used in this project.

The system should not be considered a production-ready cybersecurity solution without further testing, validation, and security evaluation.

⭐ Acknowledgement

I would like to acknowledge the creators of the CIC-IDS-2017 dataset for providing the network traffic data used for this project.

I also acknowledge the learning resources and tools that helped me understand Machine Learning, Python, cybersecurity, and application development during this project.

⭐ Project Status

Status: Completed – Academic/Virtual Internship Project

The current version includes:

✅ Data preprocessing
✅ Training dataset creation
✅ Machine Learning model
✅ Model evaluation
✅ Saved trained model
✅ Streamlit web application
✅ CSV-based threat detection
✅ Threat distribution
✅ Prediction results


