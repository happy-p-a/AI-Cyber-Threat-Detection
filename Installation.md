💻 System Requirements

The project can run on a normal personal computer.

Recommended:

Python 3.10+
RAM: 8 GB or more recommended
Storage: At least 5 GB free
Operating System: Windows / Linux / macOS

The project was also developed and tested on a system with limited RAM by using a reduced training dataset.

⚙️ Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Open the project folder
cd AI-Cyber-Threat-Detection
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment
Windows
.venv\Scripts\activate

If PowerShell execution policy prevents activation, Command Prompt can be used instead.

5. Install dependencies
pip install -r requirements.txt

▶️ Running the Application

After installing the dependencies and activating the virtual environment, run:

streamlit run app.py

The Streamlit application will open in the browser.

🧪 Training the Model

If the training dataset has already been created, the model can be trained using:

python src/train_model.py

The trained files will be saved in:

models/
📊 Testing the Model

The trained model can be tested using the project test script:

python src/test_environment.py

This verifies that the required environment and model files are working correctly.