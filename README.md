# 🍿 Netflix Movie Recommender — Streamlit App

This project is a **content-based movie recommender system** that suggests similar movies based on cosine similarity of feature vectors. The UI is designed in a Netflix-style layout using Streamlit and custom CSS.

## 🎯 Features

- Movie similarity using cosine similarity
- Content-based recommendation system
- Netflix-style interface & card design
- Movie posters, genre & overview display
- High-quality poster upscaling
- Interactive UI with Streamlit

## 🧠 Tech Stack

Python, Streamlit, NumPy, Pandas, Scikit-Learn

## 🚀 How to Run

1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

2️⃣ Place `movie_dict.pkl` in the project folder  
(contains feature vectors + dataframe)

3️⃣ Run the app

```bash
streamlit run app.py
```

## 📦 Project Files

| File | Description |
|------|-----------|
| `app.py` | Main Streamlit app |
| `movie_dict.pkl` | Movie vectors + dataframe |
| `requirements.txt` | Dependencies |
| `README.md` | Project documentation |

---

## 📦 Model / Data File Download

The file `movie_dict.pkl` is larger than GitHub’s upload limit, so it’s hosted externally.

👉 **Download here:**  
https://drive.google.com/file/d/1GcMO4Wf2OPD6q4CoTnpAQ5Mkcn3usasX/view?usp=sharing

After downloading, place the file in the same folder as `app.py` before running the app.

