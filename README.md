# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System built using Python and Streamlit.
This app suggests similar movies based on user selection and displays movie posters.

---

## 🚀 Features

* 🎥 Recommend similar movies
* 🧠 Machine Learning (Cosine Similarity)
* ⚡ Fast performance with caching
* 🖼️ Movie posters using TMDB API
* 💻 Interactive UI using Streamlit

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Requests

---

## 📂 Project Structure

Movie recommendation/
│── main.py
│── movies.pkl
│── similarity.pkl (not included in GitHub due to large size)
│── requirements.txt
│── README.md

---

## ⚠️ Important Note

The file `similarity.pkl` is not uploaded to GitHub because it is too large.
You need to generate it manually.

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Generate similarity file

Run your Jupyter Notebook or script where the model is trained:

```
pickle.dump(similarity, open('similarity.pkl', 'wb'))
```

### 4. Run the app

```
streamlit run main.py
```

---

## 🔑 API Setup

* Get API key from TMDB (The Movie Database)
* Replace in code:

```
api_key = "YOUR_API_KEY"
```

---

## 📸 Screenshots

(Add your app screenshots here)

---

## 📌 Future Improvements

* 🎨 Better UI (Netflix-style design)
* 🔍 Search optimization
* ☁️ Deployment on Streamlit Cloud
* 📊 More advanced recommendation models

---

## 👨‍💻 Author

* Aman

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
