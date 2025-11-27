Real Estate Market Analysis Chatbot
A Django + React + Groq LLM powered Real Estate Insights Dashboard

This project is an AI-powered real estate analysis assistant.
Users can ask questions like:

✔ “Analyze Wakad”
✔ “Compare Baner and Aundh”
✔ “Show trend for Hinjewadi”

The system loads a structured dataset, analyzes trends (Price, Demand, Size), and returns:

📌 AI-generated market summary (Groq LLM)

📊 Interactive charts (Recharts.js)

📄 Filtered data tables

⬇️ Excel download for analyzed data

Both single-area and multi-area analysis is supported.

🚀 Features
🔍 1. Natural Language Queries

Users can ask in plain English:

“Analyze Wakad”

“Compare Baner and Aundh”

“Show trend for Hinjewadi from dataset”

🧠 2. AI Summary using Groq LLM

Uses Groq API → llama-3.1-70b-versatile

Produces market insights in 5–7 sentences

📊 3. Trend Visualization

Line charts built using Recharts

Shows:

Price vs Year

Demand vs Year

📑 4. Dynamic Data Table

Displays the filtered dataset for each analysis

Works for both single & multi-area queries

⬇️ 5. Excel Download

Export filtered results using POST /download/

📁 6. Dataset Handling

Uses dataset.xlsx

Supports dynamic updates using upload API

🛠️ Tech Stack
Backend (Django + DRF)

Python 3

Django REST Framework

Pandas

Groq LLM API

Frontend (React)

React 18

Axios

Recharts

Custom dark theme UI

📦 Project Structure
RealEstateChatbot/
│
├── backend/
│   ├── api/
│   │   ├── views.py
│   │   ├── chatbot.py
│   │   ├── excel_loader.py
│   │   ├── urls.py
│   ├── realestate_backend/
│   ├── dataset.xlsx
│   └── .env
│
└── frontend/
    ├── src/
    │   ├── App.js
    │   ├── api.js
    │   ├── components/
    │   │   ├── TrendChart.js
    │   │   ├── DataTable.js
    │   │   └── ChatInput.js
    ├── public/
    ├── package.json

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/nandini-mahadik/Real-Estate-Chatbot-with-integrates-ai.git
cd RealEstateChatbot

2. Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Create .env:
GROQ_API_KEY=your_groq_key_here
GROQ_MODEL=llama-3.1-70b-versatile

Run server:
python manage.py runserver

3. Frontend Setup
cd frontend
npm install
npm start

🧪 How to Use the Chatbot

Type queries like:

Analyze Wakad
Compare Baner and Aundh
Show trend for Hinjewadi


You will receive:

AI Summary

Price + Demand charts

Filtered dataset

Excel download option

📊 Example Output
User Query:
Analyze Wakad

System Returns:

AI Summary (Groq)

Trend Chart (2020 → 2024)

Table:

year | price | demand | size


Download Excel button

🎯 Future Enhancements

Add property-type filtering

Add map visualization

Implement user authentication

Add “predict next year price” using ML
