Subject: README.md – Movie Recommendation System

# 🎬 Movie Recommendation System

## 📌 Project Description

This project implements a **Movie Recommendation System** using Machine Learning techniques.
The system recommends movies to users based on similarity between movies using content-based filtering.

The project includes:

* Data preprocessing and feature extraction
* Similarity-based recommendation logic
* A **Streamlit web application** for interactive movie recommendations

This project is developed as a **mini project** to understand recommendation systems and real-world ML applications.

---

## 📁 Dataset Information

* **Dataset Used:** Movie dataset (movies and metadata)

The dataset typically contains:

* Movie titles
* Genres
* Overview / description
* Keywords / tags
* Cast and crew information

---

## 🛠️ Technologies & Libraries Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
Movies_Recommendation
│
├── movies.csv
├── similarity.pkl
├── movie_recommendation.ipynb
├── app.py
├── requirements.txt
└── README.md
```

*(File names may vary slightly based on implementation)*

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Selvaganapathy-k/Movies_Recommendation
cd Movies_Recommendation
```

---

### 2️⃣ (Optional) Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Streamlit Application Locally

```bash
streamlit run app.py
```

---

## 🌐 Live Application

🔗 **Streamlit App URL:**
👉 [https://moviesrecommendation-b2f6uqwkgwqbk3y5mduesh.streamlit.app/](https://moviesrecommendation-b2f6uqwkgwqbk3y5mduesh.streamlit.app/)

---

## 🔍 Recommendation Approach

* Recommendation Type: **Content-Based Filtering**
* Similarity Metric: **Cosine Similarity**
* Feature Representation:

  * Text vectorization using **CountVectorizer / TF-IDF**
* Output:

  * List of recommended movies similar to the selected movie

---

## 📈 Features

* Simple and user-friendly interface
* Recommends similar movies instantly
* Content-based recommendation logic
* No user login required

---

## 🎓 Learning Outcomes

* Understanding recommendation systems
* Text preprocessing and vectorization
* Similarity measures in machine learning
* Building interactive ML apps using Streamlit
* Structuring end-to-end ML projects on GitHub

---

## 📌 Notes

* Virtual environment folders (`venv`, `myvenv`) are not included in the repository.
* All required dependencies are listed in `requirements.txt`.

---

## ✍️ Author

**Selvaganapathy K**
Computer Science Student

---

## 🏁 Conclusion

This project demonstrates how machine learning techniques can be used to build a **movie recommendation system** that provides personalized suggestions based on content similarity.
