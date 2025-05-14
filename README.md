This project aims to predict student performance based on various attributes such as gender, parental education level, and test preparation course status. It follows a structured approach with separate modules for each stage of the machine learning workflow, ensuring clarity and maintainability.

ML_Project/
├── artifacts/                 # Stores generated artifacts like trained models and datasets
├── data/                      # Contains the raw dataset (e.g., stud.csv)
├── notebooks/                 # Jupyter notebooks for exploratory data analysis
├── src/
│   ├── components/            # Core components: data ingestion, transformation, model training
│   ├── exception.py           # Custom exception handling
│   ├── logger.py              # Logging utility
│   └── utils.py               # Utility functions
├── requirements.txt           # Project dependencies
├── setup.py                   # Package setup script
└── README.md                  # Project documentation

📊 Dataset
Source: data/stud.csv

Description: Contains student performance data with features like gender, parental education level, and test preparation course status.

🛠️ Installation
Clone the repository:

bash
git clone https://github.com/wildchaser1703/ML_Project.git
cd ML_Project


Create a virtual environment:
bash
python -m venv venv
source venv/bin/activate  
# On Windows: venv\Scripts\activate


Install dependencies:

bash
pip install -r requirements.txt

📈 Usage
Data Ingestion:
bash
python src/components/data_ingestion.py
This script reads the raw data, performs train-test split, and saves the datasets in the artifacts/ directory.

Data Transformation:
bash
python src/components/data_transformation.py
Applies necessary preprocessing steps to the data.

Model Training:
bash
python src/components/model_trainer.py
Trains the machine learning model and saves it for future predictions.

🧪 Testing
To be added: Unit tests for each component to ensure reliability and correctness.

📌 Features
Modular codebase for scalability
Custom exception handling for better error tracking
Comprehensive logging for monitoring pipeline execution
Clear separation of concerns across different modules
