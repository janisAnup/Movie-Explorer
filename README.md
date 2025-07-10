Hey Janis here <br>
This is my 2nd task as an intern at Next24Tech<br>
🎬 Movie Explorer<br>
A sleek and interactive web application built using Streamlit that allows users to explore movies by genre and view key movie details such as rating, popularity, tags, and more. This was developed as part of Task 2 for my internship at Next24Tech.<br>

📌 Features<br>
🔍 Filter movies based on genre<br>

🎥 View movie details like:<br>
Title & release date<br>
Genre and tags<br>
Rating and popularity<br>
Overview (short summary)<br>
🧠 Caching for better performance<br>
📁 Data processed from CSV files (movies_metadata.csv, keywords.csv, links.csv)<br>

🛠️ Technologies Used<br>
Python 3<br>
Streamlit<br>
Pandas<br>
AST (Abstract Syntax Trees)<br>

📂 Folder Structure
<pre>
Movie Explorer/
├── app.py              # Main Streamlit application
├── recommender.py      # Core logic for movie extraction & filtering
├── keywords.csv        # Movie tags data
├── links.csv           # Mapping of movie IDs to TMDb
├── movies_metadata.csv # Main movie dataset
├── .gitignore
└── README.md
</pre>


🚀 How to Run<br>

Clone the repository
<pre> 
git clone https://github.com/janisAnup/Movie-Explorer.git
cd Movie-Explorer</pre>
	
(Optional) Create and activate a virtual environment
<pre>
python -m venv .venv
.venv\Scripts\activate</pre>

Install the dependencies
<pre>
pip install -r requirements.txt
</pre>

Run the app
<pre>
streamlit run app.py</pre>


📚 Internship Info<br>

This project is part of my internship with Next24Tech, under Task 2: Building a Movie Explorer GUI using Streamlit in Python. The aim was to gain hands-on experience in GUI design, working with datasets, and web-based data exploration.
