💻 System Requirements

The project can run on a normal personal computer.

Recommended:

Python 3.10+
RAM: 8 GB or more recommended
Storage: At least 5 GB free
Operating System: Windows / Linux / macOS

The project was also developed and tested on a system with limited RAM by using a reduced training dataset.

⚙️ Installation
1. Clone the Repository
git clone https://github.com/happy-p-a/AI-Cyber-Threat-Detection.git
cd AI-Cyber-Threat-Detection
2. Create a Virtual Environment

Windows:

python -m venv .venv

Activate:

.venv\Scripts\activate

If PowerShell prevents activation, the environment's Python executable can be used directly.

3. Install Dependencies
pip install -r requirements.txt
4. Configure Generative AI

Create a local .env file:

GROQ_API_KEY=your_api_key_here

Do not upload the .env file to GitHub.

5. Run the Application
streamlit run app.py

Then upload a network-flow CSV file and click:

🔍 Detect Threats
