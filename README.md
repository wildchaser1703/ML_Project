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
├── artifacts/               # Stores train.csv, test.csv, and final model.pkl
├── data/
│   └── stud.csv             # Raw dataset
├── notebooks/
│   └── student-performance.ipynb  # EDA and experimentation
├── src/
│   ├── components/
│   │   ├── data_ingestion.py      # Reads and splits the dataset
│   │   ├── data_transformation.py # Transforms categorical & numerical data
│   │   └── model_trainer.py       # Model training logic
│   ├── exception.py               # Custom exception handling
│   ├── logger.py                  # Logger for debugging and tracking
│   └── utils.py                   # Utility functions
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup file
└── README.md                # You're reading it!
```

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally:

### 1. Clone the Repository
git clone https://github.com/wildchaser1703/ML_Project.git
cd ML_Project


### 2. Create a Virtual Environment
python -m venv venv


### 3. Activate the Environment
**On Windows:**
venv\Scripts\activate
**On macOS/Linux:**


### 4. Install Dependencies
pip install -r requirements.txt


---

## 🧪 Running the Pipeline
### Step 1: Run Data Ingestion
python src/components/data_ingestion.py

- Reads `data/stud.csv`
- Splits into train and test datasets
- Saves files in the `artifacts/` folder

### Step 2: Run Data Transformation
python src/components/data_transformation.py

- Encodes categorical features
- Applies feature scaling
- Saves numpy arrays and transformer pipeline

### Step 3: Run Model Training

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

## 👩‍💻 Author

**Toshali Mohapatra**  
📧 toshalimohapatra1@gmail.com  
🔗 [GitHub: wildchaser1703](https://github.com/wildchaser1703)

---
## 📄 License
### This project is licensed under the MIT License.
---
⭐ If you found this project useful, consider starring the repo and sharing it!






