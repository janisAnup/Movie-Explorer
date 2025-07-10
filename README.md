```markdown
# 🎬 Movie Explorer

A sleek and interactive movie recommender and explorer app built using **Streamlit** and **Python**.

This app allows users to:

- 🔍 Explore movies by genre  
- 🎭 View key movie details like rating, popularity, summary, tags, etc.  
- 🧠 Learn from hands-on integration with datasets and Streamlit design

---

## 🚀 How to Run

### 📥 Clone the repository

```bash
git clone https://github.com/janisAnup/Movie-Explorer.git
cd Movie-Explorer
```

### 🛠️ (Optional) Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows
```

### 📦 Install the dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the app

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```plaintext
Movie-Explorer/
│
├── app.py                 # Main Streamlit app
├── recommender.py         # Core recommendation logic
├── keywords.csv           # Contains keyword tags
├── links.csv              # TMDB/IMDB mapping
├── movies_metadata.csv    # Main movie dataset
├── requirements.txt       # All Python dependencies
├── README.md              # This file
└── .venv/ (optional)      # Virtual environment
```

---

## 🌟 Features

- Clean dark-themed UI
- Genre-based movie filtering
- Movie cards showing:
  - Title
  - Genres, tags
  - Rating, popularity
  - Summary
- Responsive layout using columns
- Markdown + emoji styling

---

## 💼 Internship Info

This project is part of my internship with **Next24Tech**, under **Task 2: Building a Movie Explorer GUI** using **Streamlit in Python**.  
The aim was to gain hands-on experience in:

- 🧩 GUI design using Streamlit
- 📊 Working with real-world datasets (Kaggle’s Movies Dataset)
- 🌐 Building and deploying web-based Python applications

---

## 🙌 Acknowledgements

- Kaggle: [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
- Streamlit documentation
- My mentors and peers at **Next24Tech**

---

> ⚠️ Note: The `credits.csv` file was excluded due to GitHub’s 100MB file size limit. This project works without it.
```
