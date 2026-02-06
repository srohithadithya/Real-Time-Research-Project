# Real-Time-Research-Project 🚗💰

[![Python V3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/framework-Django-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional-grade machine learning application designed to provide high-precision resale value valuations for vehicles. This project integrates a robust Data Science pipeline with a premium, high-performance web interface.
.

---

## 🌟 Visual Preview
*The application features a modern "Glassmorphism" interface with a sleek dark-mode aesthetic, utilizing high-contrast typography and subtle micro-animations for a premium user experience.*

---

## 🚀 Key Features
- **High-Precision Intelligence**: Utilizing Random Forest ensembles for accurate price estimation.
- **Micro-Animation Engine**: Smooth interface transitions and interactive hover effects.
- **End-to-End Pipeline**: Includes full data cleaning, feature engineering, model training, and web deployment.
- **Responsive Layout**: Designed for seamless use across desktops, tablets, and smartphones.
- **AI Analytics**: Processes complex engine variables like Torque (RPM) and Power (BHP) in real-time.

---

## 🔬 Data Science & Machine Learning
### The "Engine" (Model Science)
The model is a **Random Forest Regressor** optimized via cross-validation. 
- **Training Accuracy**: ~99.18%
- **Testing Accuracy**: ~97.06%
- **Estimators**: 300 Decision Trees working in parallel.

### Feature Engineering
The AI considers 15+ complex parameters to determine value:
- **Vehicle Age**: Calculated from the manufacturing year.
- **Usage Metrics**: Distance driven in kilometers.
- **Engine Specs**: Engine capacity (CC), Max Power (BHP), and Torque (RPM).
- **Efficiency**: Detailed mileage (kmp/l) extraction.
- **Social Factors**: Seller type (Individual/Dealer) and Ownership history (1st, 2nd, etc.).

---

## 📁 Project Architecture
```text
📦 Car Selling Price Prediction
 ┣ 📂 Code/                   # Core Logic
 ┃ ┣ 📂 mysite/               # Django Web Application Source
 ┃ ┃ ┣ 📂 polls/              # Main App Module
 ┃ ┃ ┃ ┣ 📜 CarSelling.pickle # The "AI Brain" (Serialized Model)
 ┃ ┃ ┃ ┣ 📂 static/           # CSS, Images (logo.jpg), JS
 ┃ ┃ ┃ ┗ 📂 templates/        # Premium UI (index.html)
 ┃ ┣ 📜 Car details.csv       # Training Dataset
 ┃ ┣ 📜 train_model.py        # Automated Training Script
 ┃ ┗ 📜 car_selling_price.ipynb # Research & Exploration Notebook
 ┣ 📜 run_app.bat             # One-click Master Launcher
 ┗ 📜 README.md               # Project Documentation
```

---

## 🛠️ Technical Stack
- **Languages**: Python (Core Science & Logic), JavaScript (UI Interactions)
- **Frameworks**: Django (Web Server)
- **ML libraries**: Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn
- **UI Design**: CSS3 Vanilla (Glassmorphism), FontAwesome 6.4, Google Fonts (Outfit)

---

## 🔧 Installation & Usage
### Prerequisites
- Python 3.12.0+
- Modern Web Browser (Chrome/Edge/Safari)

### Quick Start
1.  **Clone the Repo**:
    ```bash
    git clone https://github.com/srohithadithya/Real-Time-Research-Project.git
    ```
2.  **Launch**:
    Double-click the **`run_app.bat`** file in the root directory. This script will:
    - Create a Virtual Environment (`venv`).
    - Install all dependencies from `requirements.txt`.
    - Apply database migrations.
    - Start the server on `http://127.0.0.1:8000/`.

---

## 🤝 Contribution
Contributions are welcome! If you have suggestions for improving model accuracy or UI enhancements, feel free to open a Pull Request.


