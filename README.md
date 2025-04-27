# 🚀 NASA Near-Earth Object (NEO) Tracking & Insights Dashboard

A Streamlit-powered dashboard that fetches real-time asteroid data from NASA's public API, processes and stores it in an SQLite database, and allows users to explore near-earth objects and their close approaches through interactive queries.

---

## 🔢 Features

- **Data Fetching**: Connects to NASA's NeoWs (Near Earth Object Web Service) API.
- **Data Cleaning**: Parses essential asteroid fields and close approach parameters.
- **Database Storage**: Saves structured data into an SQLite database (`asteroids.db`) with two tables: `asteroids` and `close_approach`.
- **Streamlit Dashboard**: Interactive web interface to run predefined SQL queries and visualize asteroid insights.

---

## 🔍 Queries Supported

- Number of close approaches per asteroid.
- Top 10 fastest asteroids.
- Hazardous asteroids with more than 3 close approaches.
- Closest asteroid approaches (by miss distance).

*More queries can be added easily!*

---

## 📁 Project Structure

```bash
/
|-- app.py               # Streamlit app entry point
|-- asteroids.db          # SQLite database with asteroids and close approach data
|-- README.md             # Project documentation
```

---

## 🔄 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/nasa-asteroid-dashboard.git
   cd nasa-asteroid-dashboard
   ```

2. **Install required packages**
   ```bash
   pip install streamlit pandas requests
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. **Access the dashboard**
   Open your browser at: `http://localhost:8501`

---

## 🌐 Deploy on Streamlit Cloud

- Push your code to a public GitHub repository.
- Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and click "New app".
- Select your repository and `app.py` as entry point.
- Deploy!

---

## 🌌 Technologies Used

- **NASA NeoWs Public API**
- **Python 3**
- **SQLite**
- **Streamlit**
- **Pandas**

---

## 📊 Future Improvements (Optional)

- Add charts (e.g., speed vs distance scatterplots).
- Allow user-defined date range selection.
- Hazardous asteroid highlighting.
- Dashboard dark/light themes.

---

## 💪 Author

- Developed with passion by Nethaji

*Built as part of learning project for real-time API interaction, data engineering, and frontend visualization!* 🚀

