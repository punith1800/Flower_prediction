# 🌸 Iris Flower Prediction System

**Machine Learning Based Iris Flower Classification**

## 📌 Project Overview

The **Iris Flower Prediction System** is a Machine Learning-based web application that predicts the species of an Iris flower based on its physical measurements.

The system uses a Machine Learning classification algorithm trained on the famous Iris dataset to identify three different flower species:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

Users can enter flower measurements through a simple web interface and receive an instant prediction.

## 🎯 Project Objectives

- Develop a simple Machine Learning prediction system.
- Understand the fundamentals of supervised learning.
- Classify Iris flower species based on input measurements.
- Build an interactive web interface for predictions.
- Understand the complete workflow of data preprocessing, model training, and prediction.

## 🚀 Key Features

- User-friendly web interface.
- Input flower measurements manually.
- Predict Iris flower species instantly.
- Machine Learning-based classification.
- Dataset preprocessing and model training.
- Accurate and fast prediction results.
- Beginner-friendly implementation.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Machine Learning | Flower classification |
| Scikit-learn | Model training and prediction |
| Pandas | Dataset handling |
| NumPy | Numerical operations |
| HTML5 | Webpage structure |
| CSS3 | User interface design |
| Flask | Backend web framework |
| VS Code | Development environment |

## 🌺 Iris Dataset

The project uses the Iris dataset, which contains 150 flower samples belonging to three species.

Each flower is classified using four input features:

| Feature | Description |
|---|---|
| Sepal Length | Length of the sepal in cm |
| Sepal Width | Width of the sepal in cm |
| Petal Length | Length of the petal in cm |
| Petal Width | Width of the petal in cm |

### Iris Flower Species

1. **Setosa** – Typically has smaller petals.
2. **Versicolor** – Has medium-sized petals.
3. **Virginica** – Generally has larger petals.

## 📂 Project Structure

```text
Iris-Flower-Prediction/
│
├── app.py
├── model.py
├── train_model.py
├── iris.csv
├── iris_model.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

*Note: Modify the structure according to your actual project files.*

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd Iris-Flower-Prediction
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python app.py
```

### Step 6: Open in Browser

```text
http://127.0.0.1:5000/
```

## 🔍 How It Works

The application follows these steps:

1. User enters the four flower measurements.
2. The frontend sends the input to the Python backend.
3. The backend processes the input.
4. The trained Machine Learning model predicts the flower species.
5. The predicted flower name is displayed on the webpage.

## 🧠 Machine Learning Algorithm

The project can use the **K-Nearest Neighbors (KNN)** classification algorithm or another suitable classifier.

The model learns patterns from the Iris dataset and predicts the flower species based on the input measurements.

### Prediction Inputs

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Prediction Output

One of the following:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

## 📸 Application Preview

Add your project screenshots here:

```markdown
![Iris Prediction Home Page](screenshots/home.png)

![Prediction Result](screenshots/result.png)
```

## 🔮 Future Enhancements

- Improve prediction performance through model comparison.
- Add graphical data visualization.
- Display prediction confidence.
- Add a responsive mobile-friendly interface.
- Deploy the application on AWS or other cloud platforms.
- Add more machine learning classification algorithms.

## 👨‍💻 Project Developers

**Punith V A**

**Team Members:**
- Umesh D G
- Shashank A
- Mohan A
- Shreyas R A

**Department:** Computer Science

**College:** Best Degree College

**University:** Bengaluru North University

## 🎓 Academic Project

This project is developed as a Computer Science mini-project to demonstrate practical knowledge of Python programming, Machine Learning, data preprocessing, and web application development.

## ⭐ Support

If you find this project useful, give this repository a ⭐ on GitHub!

---

**Iris Flower Prediction System**

*Learn. Train. Predict. Innovate.* 🌸
