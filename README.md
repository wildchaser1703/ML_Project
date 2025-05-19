# Student Performance Prediction 🧠📊

This project aims to build a machine learning pipeline that predicts student performance based on demographic and educational attributes. The pipeline covers everything from data ingestion to model training, packaging, and evaluation.

---

## 🚀 Project Features

- Custom logging and exception handling
- Modular pipeline: Data ingestion, transformation, and training
- Reproducible training artifacts (train/test CSVs, models)
- Configurable structure using `dataclasses`
- Well-documented, extensible codebase
- CI-ready with requirements and setup script

---

## 📁 Project Structure

```yaml
ML_Project/
├── .ebextensions/             # AWS Elastic Beanstalk configuration files
├── .github/
│   └── workflows/             # GitHub Actions workflows
├── catboost_info/             # CatBoost training logs and metadata
├── notebook/                  # Jupyter notebooks for exploration and experimentation
├── src/                       # Source code for the ML pipeline
│   ├── components/            # Core components like data ingestion, transformation, and model training
│   ├── exception.py           # Custom exception classes
│   ├── logger.py              # Logging configuration and utilities
│   ├── pipeline/
│   │   ├── predict_pipeline.py  # Prediction pipeline logic
│   │   └── train_pipeline.py    # Training pipeline logic
│   ├── utils.py               # Utility functions
│   └── __init__.py            # Package initializer
├── templates/                 # HTML templates for the Flask web application
│   ├── home.html              # Home page template
│   └── index.html             # Index page template
├── .gitignore                 # Specifies files and directories to be ignored by Git
├── Procfile                   # Specifies the command to run the application on Heroku or similar platforms
├── README.md                  # Project overview and documentation
├── application.py             # Flask application entry point
├── requirements.txt           # Python dependencies
└── setup.py                   # Package installation script

```

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/wildchaser1703/ML_Project.git
cd ML_Project
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Environment
```bash
**On Windows:**
venv\Scripts\activate
**On macOS/Linux:**
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Running the Pipeline
### Step 1: Run Data Ingestion
```bash
python src/components/data_ingestion.py
```
- Reads `data/stud.csv`
- Splits into train and test datasets
- Saves files in the `artifacts/` folder

### Step 2: Run Data Transformation
```bash
python src/components/data_transformation.py
```
- Encodes categorical features
- Applies feature scaling
- Saves numpy arrays and transformer pipeline

### Step 3: Run Model Training
```bash
python src/components/model_trainer.py
```
- Trains a regression/classification model
- Evaluates performance
- Saves the final model in `artifacts/`

---

## ✅ Best Practices Followed

- Modular, testable components
- Detailed logging and tracebacks
- Clean artifacts and reproducibility
- Consistent file paths with `os.path.join`
- Uses `@dataclass` for configuration

---

## 🛠 Common Issues and Fixes

| Problem | Fix |
|--------|-----|
| `None` treated as `NaN` | Convert column to `category` using `.astype('category')` |
| `Module cannot be used as a type` | Use `from dataclasses import dataclass` (Python ≥ 3.7) |
| `tb_lineno not known` | Make sure `sys.exc_info()` returns valid traceback |
| `dill not installed` | Add `dill` to `requirements.txt` and run `pip install -r requirements.txt` |
| `string indices must be integers` | Likely trying to index a string instead of a list or array |

---

## 📄 License
This project is licensed under the MIT License.

⭐ If you found this project useful, consider starring the repo and sharing it!






